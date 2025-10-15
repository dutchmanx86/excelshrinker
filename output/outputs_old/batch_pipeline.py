"""
Batch Excel analysis pipeline for processing all sheets in a workbook.

Two-phase approach:
  Phase 1: Boundary detection + compression → save JSONs (sequential)
  Phase 2: LLM analysis on saved JSONs (parallel with rate limiting)

This design ensures no work is lost if rate limits are hit during LLM processing.
"""
import sys
import json
import time
import argparse
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure project modules are importable
sys.path.append(str(Path(__file__).parent))

from boundary_detector.core.batch_detector import BatchBoundaryDetector
from boundary_detector.models.detection_config import DetectionConfig
from compression.format_compression import compress_formats
from compression.inverted_index_compression import compress_format_result_json
from llm_analyzer.llm_analyzer import create_llm_analysis

try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
    print("Note: tqdm not installed. Install with 'pip install tqdm' for progress bars.")

# Output directories
BASE_OUTPUT_DIR = Path(__file__).parent / "output" / "batch"
JSON_OUTPUT_DIR = BASE_OUTPUT_DIR / "json"
MARKDOWN_OUTPUT_DIR = BASE_OUTPUT_DIR / "markdown"


class BatchPipelineProgress:
    """Track progress across pipeline runs"""

    def __init__(self, workbook_name: str, progress_file: Path):
        self.workbook_name = workbook_name
        self.progress_file = progress_file
        self.data = self._load()

    def _load(self) -> Dict:
        """Load existing progress file or create new"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {
            "workbook": self.workbook_name,
            "started": datetime.now().isoformat(),
            "phase1_complete": False,
            "phase2_complete": False,
            "sheets_compressed": [],
            "sheets_analyzed": [],
            "errors": {}
        }

    def save(self):
        """Save progress to disk"""
        self.progress_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.progress_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def mark_sheet_compressed(self, sheet_name: str):
        """Mark a sheet as compressed"""
        if sheet_name not in self.data["sheets_compressed"]:
            self.data["sheets_compressed"].append(sheet_name)
        self.save()

    def mark_sheet_analyzed(self, sheet_name: str):
        """Mark a sheet as analyzed"""
        if sheet_name not in self.data["sheets_analyzed"]:
            self.data["sheets_analyzed"].append(sheet_name)
        self.save()

    def mark_phase1_complete(self):
        """Mark phase 1 as complete"""
        self.data["phase1_complete"] = True
        self.data["phase1_completed"] = datetime.now().isoformat()
        self.save()

    def mark_phase2_complete(self):
        """Mark phase 2 as complete"""
        self.data["phase2_complete"] = True
        self.data["phase2_completed"] = datetime.now().isoformat()
        self.save()

    def record_error(self, sheet_name: str, phase: str, error: str):
        """Record an error for a sheet"""
        self.data["errors"][f"{sheet_name}_{phase}"] = {
            "sheet": sheet_name,
            "phase": phase,
            "error": error,
            "timestamp": datetime.now().isoformat()
        }
        self.save()


def sanitize_filename(name: str) -> str:
    """Convert sheet name to safe filename"""
    # Replace problematic characters
    safe = name.replace('/', '_').replace('\\', '_').replace(':', '_')
    safe = safe.replace('*', '_').replace('?', '_').replace('"', '_')
    safe = safe.replace('<', '_').replace('>', '_').replace('|', '_')
    return safe


def phase1_compress_all_sheets(
    file_path: str,
    workbook_name: str,
    config: DetectionConfig,
    progress: BatchPipelineProgress
) -> Dict[str, Path]:
    """
    Phase 1: Detect boundaries and compress all sheets to JSON files.

    Returns:
        Dictionary mapping sheet names to their JSON file paths
    """
    print(f"\n{'='*80}")
    print(f"PHASE 1: BOUNDARY DETECTION & COMPRESSION")
    print(f"{'='*80}\n")

    # Create output directory for this workbook
    json_dir = JSON_OUTPUT_DIR / workbook_name
    json_dir.mkdir(parents=True, exist_ok=True)

    # Detect boundaries for all sheets
    print("Step 1: Detecting boundaries for all sheets...")
    batch_detector = BatchBoundaryDetector(config)
    boundary_results = batch_detector.detect_all_sheets(
        file_path=file_path,
        detect_charts=False,  # Skip charts for speed
        parallel=False  # Sequential is more stable
    )

    print(f"\nStep 2: Compressing {len(boundary_results)} sheets...")
    json_files = {}

    sheets_to_process = [s for s in boundary_results.keys()
                        if s not in progress.data["sheets_compressed"]]

    iterator = tqdm(sheets_to_process) if TQDM_AVAILABLE else sheets_to_process

    for sheet_name in iterator:
        if not TQDM_AVAILABLE:
            print(f"  Processing: {sheet_name}...")

        try:
            boundary_result = boundary_results[sheet_name]

            # Format compression
            format_result = compress_formats(
                file_path=file_path,
                sheet_name=sheet_name,
                boundary_result=boundary_result,
                config=config
            )

            # Inverted index compression
            format_json = json.loads(format_result.to_json())
            compressed_result = compress_format_result_json(format_json, min_occurrences=2)

            # Save to file
            safe_name = sanitize_filename(sheet_name)
            json_file = json_dir / f"{safe_name}_compressed.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(compressed_result, f, indent=2)

            json_files[sheet_name] = json_file
            progress.mark_sheet_compressed(sheet_name)

            if not TQDM_AVAILABLE:
                stats = compressed_result['compression_stats']
                print(f"    Saved: {json_file.name} ({stats['space_saved_percent']:.1f}% compression)")

        except Exception as e:
            error_msg = f"Error compressing sheet: {str(e)}"
            progress.record_error(sheet_name, "phase1", error_msg)
            if not TQDM_AVAILABLE:
                print(f"    ERROR: {error_msg}")

    progress.mark_phase1_complete()
    print(f"\nPhase 1 complete! {len(json_files)} sheets compressed to: {json_dir}")
    return json_files


def phase1_compress_all_sheets_custom(
    file_path: str,
    json_dir: Path,
    config: DetectionConfig,
    progress: BatchPipelineProgress
) -> Dict[str, Path]:
    """
    Phase 1: Detect boundaries and compress all sheets to JSON files (custom directory).

    Returns:
        Dictionary mapping sheet names to their JSON file paths
    """
    print(f"\n{'='*80}")
    print(f"PHASE 1: BOUNDARY DETECTION & COMPRESSION")
    print(f"{'='*80}\n")

    # Create output directory
    json_dir.mkdir(parents=True, exist_ok=True)

    # Detect boundaries for all sheets
    print("Step 1: Detecting boundaries for all sheets...")
    batch_detector = BatchBoundaryDetector(config)
    boundary_results = batch_detector.detect_all_sheets(
        file_path=file_path,
        detect_charts=False,  # Skip charts for speed
        parallel=False  # Sequential is more stable
    )

    print(f"\nStep 2: Compressing {len(boundary_results)} sheets...")
    json_files = {}

    sheets_to_process = [s for s in boundary_results.keys()
                        if s not in progress.data["sheets_compressed"]]

    iterator = tqdm(sheets_to_process) if TQDM_AVAILABLE else sheets_to_process

    for sheet_name in iterator:
        if not TQDM_AVAILABLE:
            print(f"  Processing: {sheet_name}...")

        try:
            boundary_result = boundary_results[sheet_name]

            # Format compression
            format_result = compress_formats(
                file_path=file_path,
                sheet_name=sheet_name,
                boundary_result=boundary_result,
                config=config
            )

            # Inverted index compression
            format_json = json.loads(format_result.to_json())
            compressed_result = compress_format_result_json(format_json, min_occurrences=2)

            # Save to file
            safe_name = sanitize_filename(sheet_name)
            json_file = json_dir / f"{safe_name}_compressed.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(compressed_result, f, indent=2)

            json_files[sheet_name] = json_file
            progress.mark_sheet_compressed(sheet_name)

            if not TQDM_AVAILABLE:
                stats = compressed_result['compression_stats']
                print(f"    Saved: {json_file.name} ({stats['space_saved_percent']:.1f}% compression)")

        except Exception as e:
            error_msg = f"Error compressing sheet: {str(e)}"
            progress.record_error(sheet_name, "phase1", error_msg)
            if not TQDM_AVAILABLE:
                print(f"    ERROR: {error_msg}")

    progress.mark_phase1_complete()
    print(f"\nPhase 1 complete! {len(json_files)} sheets compressed to: {json_dir}")
    return json_files


def analyze_single_sheet_with_retry(
    sheet_name: str,
    json_file: Path,
    api_key: str,
    model: str,
    markdown_dir: Path,
    max_retries: int = 3
) -> Tuple[str, bool, Optional[str]]:
    """
    Analyze a single sheet with exponential backoff retry.

    Returns:
        Tuple of (sheet_name, success, error_message)
    """
    safe_name = sanitize_filename(sheet_name)
    markdown_file = markdown_dir / f"{safe_name}_analysis.md"

    for attempt in range(max_retries):
        try:
            # Load compressed JSON
            with open(json_file, 'r') as f:
                compressed_json = json.load(f)

            # Generate analysis
            analysis = create_llm_analysis(
                compressed_json=compressed_json,
                api_key=api_key,
                model=model
            )

            # Save markdown
            with open(markdown_file, 'w', encoding='utf-8') as f:
                f.write(analysis)

            return (sheet_name, True, None)

        except Exception as e:
            error_msg = str(e)

            # Check if it's a rate limit error
            if "rate_limit" in error_msg.lower() or "429" in error_msg:
                if attempt < max_retries - 1:
                    # Exponential backoff: 2^attempt * 5 seconds
                    wait_time = (2 ** attempt) * 5
                    print(f"\n  Rate limit hit for {sheet_name}, waiting {wait_time}s...")
                    time.sleep(wait_time)
                    continue

            # If not rate limit or max retries reached, fail
            return (sheet_name, False, error_msg)

    return (sheet_name, False, "Max retries exceeded")


def phase2_analyze_with_llm(
    json_files: Dict[str, Path],
    workbook_name: str,
    api_key: str,
    model: str,
    progress: BatchPipelineProgress,
    max_workers: int = 5
) -> Dict[str, Path]:
    """
    Phase 2: Analyze all compressed JSONs with LLM in parallel.

    Returns:
        Dictionary mapping sheet names to their markdown file paths
    """
    print(f"\n{'='*80}")
    print(f"PHASE 2: LLM ANALYSIS (parallel, max {max_workers} workers)")
    print(f"{'='*80}\n")

    # Create output directory for markdown
    markdown_dir = MARKDOWN_OUTPUT_DIR / workbook_name
    markdown_dir.mkdir(parents=True, exist_ok=True)

    markdown_files = {}

    # Filter out already-analyzed sheets
    sheets_to_analyze = {
        name: path for name, path in json_files.items()
        if name not in progress.data["sheets_analyzed"]
    }

    if not sheets_to_analyze:
        print("All sheets already analyzed!")
        return markdown_files

    print(f"Analyzing {len(sheets_to_analyze)} sheets...")

    # Submit all tasks
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                analyze_single_sheet_with_retry,
                sheet_name,
                json_file,
                api_key,
                model,
                markdown_dir
            ): sheet_name
            for sheet_name, json_file in sheets_to_analyze.items()
        }

        # Use tqdm if available
        if TQDM_AVAILABLE:
            iterator = tqdm(as_completed(futures), total=len(futures), desc="Analyzing")
        else:
            iterator = as_completed(futures)

        # Collect results as they complete
        for future in iterator:
            sheet_name, success, error = future.result()

            if success:
                safe_name = sanitize_filename(sheet_name)
                markdown_file = markdown_dir / f"{safe_name}_analysis.md"
                markdown_files[sheet_name] = markdown_file
                progress.mark_sheet_analyzed(sheet_name)
                if not TQDM_AVAILABLE:
                    print(f"  OK {sheet_name}")
            else:
                progress.record_error(sheet_name, "phase2", error)
                if not TQDM_AVAILABLE:
                    print(f"  FAIL {sheet_name}: {error}")

    progress.mark_phase2_complete()
    print(f"\nPhase 2 complete! Markdown files saved to: {markdown_dir}")
    return markdown_files


def phase2_analyze_with_llm_custom(
    json_files: Dict[str, Path],
    markdown_dir: Path,
    api_key: str,
    model: str,
    progress: BatchPipelineProgress,
    max_workers: int = 5
) -> Dict[str, Path]:
    """
    Phase 2: Analyze all compressed JSONs with LLM in parallel (custom directory).

    Returns:
        Dictionary mapping sheet names to their markdown file paths
    """
    print(f"\n{'='*80}")
    print(f"PHASE 2: LLM ANALYSIS (parallel, max {max_workers} workers)")
    print(f"{'='*80}\n")

    # Create output directory for markdown
    markdown_dir.mkdir(parents=True, exist_ok=True)

    markdown_files = {}

    # Filter out already-analyzed sheets
    sheets_to_analyze = {
        name: path for name, path in json_files.items()
        if name not in progress.data["sheets_analyzed"]
    }

    if not sheets_to_analyze:
        print("All sheets already analyzed!")
        return markdown_files

    print(f"Analyzing {len(sheets_to_analyze)} sheets...")

    # Submit all tasks
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                analyze_single_sheet_with_retry,
                sheet_name,
                json_file,
                api_key,
                model,
                markdown_dir
            ): sheet_name
            for sheet_name, json_file in sheets_to_analyze.items()
        }

        # Use tqdm if available
        if TQDM_AVAILABLE:
            iterator = tqdm(as_completed(futures), total=len(futures), desc="Analyzing")
        else:
            iterator = as_completed(futures)

        # Collect results as they complete
        for future in iterator:
            sheet_name, success, error = future.result()

            if success:
                safe_name = sanitize_filename(sheet_name)
                markdown_file = markdown_dir / f"{safe_name}_analysis.md"
                markdown_files[sheet_name] = markdown_file
                progress.mark_sheet_analyzed(sheet_name)
                if not TQDM_AVAILABLE:
                    print(f"  OK {sheet_name}")
            else:
                progress.record_error(sheet_name, "phase2", error)
                if not TQDM_AVAILABLE:
                    print(f"  FAIL {sheet_name}: {error}")

    progress.mark_phase2_complete()
    print(f"\nPhase 2 complete! Markdown files saved to: {markdown_dir}")
    return markdown_files


def run_batch_pipeline(
    file_path: str,
    api_key: str,
    model: str = "gpt-5-nano",
    max_workers: int = 5,
    resume: bool = True
):
    """
    Run the complete batch pipeline for all sheets in a workbook.

    Args:
        file_path: Path to Excel file
        api_key: OpenAI API key
        model: LLM model to use
        max_workers: Maximum parallel workers for Phase 2
        resume: Whether to resume from progress file
    """
    start_time = time.time()

    # Get workbook name
    workbook_path = Path(file_path)
    workbook_name = workbook_path.stem

    # Create model-specific output directories
    model_output_dir = BASE_OUTPUT_DIR / f"{workbook_name}_{model}"
    json_dir = model_output_dir / "json"
    markdown_dir = model_output_dir / "markdown"

    print(f"\n{'='*80}")
    print(f"BATCH EXCEL ANALYSIS PIPELINE")
    print(f"{'='*80}")
    print(f"Workbook: {workbook_path.name}")
    print(f"LLM Model: {model}")
    print(f"Max Workers (Phase 2): {max_workers}")
    print(f"Output Directory: {model_output_dir}")
    print(f"{'='*80}")

    # Initialize progress tracking
    progress_file = model_output_dir / "_progress.json"
    progress = BatchPipelineProgress(workbook_name, progress_file)

    if resume and (progress.data["phase1_complete"] or progress.data["sheets_compressed"]):
        print(f"\nWARNING: Resuming from previous run:")
        phase1_status = "COMPLETE" if progress.data['phase1_complete'] else f"{len(progress.data['sheets_compressed'])} sheets compressed"
        phase2_status = "COMPLETE" if progress.data['phase2_complete'] else f"{len(progress.data['sheets_analyzed'])} sheets analyzed"
        print(f"  Phase 1: {phase1_status}")
        print(f"  Phase 2: {phase2_status}")

    config = DetectionConfig()

    # === Phase 1: Compression ===
    if not progress.data["phase1_complete"]:
        # Pass the custom json_dir instead of workbook_name
        json_files = phase1_compress_all_sheets_custom(
            file_path=file_path,
            json_dir=json_dir,
            config=config,
            progress=progress
        )
    else:
        print(f"\nPhase 1 already complete, loading JSON files...")
        json_files = {}
        for json_file in json_dir.glob("*_compressed.json"):
            # Extract original sheet name from filename
            sheet_name = json_file.stem.replace("_compressed", "")
            json_files[sheet_name] = json_file
        print(f"Loaded {len(json_files)} JSON files")

    # === Phase 2: LLM Analysis ===
    if not progress.data["phase2_complete"]:
        markdown_files = phase2_analyze_with_llm_custom(
            json_files=json_files,
            markdown_dir=markdown_dir,
            api_key=api_key,
            model=model,
            progress=progress,
            max_workers=max_workers
        )
    else:
        print(f"\nPhase 2 already complete!")
        markdown_files = {
            md.stem.replace("_analysis", ""): md
            for md in markdown_dir.glob("*_analysis.md")
        }

    # === Summary ===
    elapsed = time.time() - start_time
    print(f"\n{'='*80}")
    print(f"BATCH PIPELINE COMPLETE")
    print(f"{'='*80}")
    print(f"Total time: {elapsed:.1f}s ({elapsed/60:.1f} minutes)")
    print(f"Sheets processed: {len(json_files)}")
    print(f"Sheets analyzed: {len(markdown_files)}")

    if progress.data["errors"]:
        print(f"\nWARNING: Errors encountered: {len(progress.data['errors'])}")
        print(f"See progress file for details: {progress_file}")

    print(f"\nOutputs saved to:")
    print(f"  JSON: {json_dir}")
    print(f"  Markdown: {markdown_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Run batch Excel analysis pipeline for all sheets in a workbook."
    )
    parser.add_argument(
        "file_path",
        help="Path to the Excel file to analyze."
    )
    parser.add_argument(
        "--api_key",
        help="OpenAI API key (defaults to OPENAI_API_KEY environment variable).",
        default=os.getenv("OPENAI_API_KEY")
    )
    parser.add_argument(
        "--model",
        help="The LLM model to use (e.g., gpt-5, gpt-5-mini, gpt-5-nano, gpt-4o).",
        default="gpt-5-nano"
    )
    parser.add_argument(
        "--max_workers",
        help="Maximum parallel workers for LLM analysis (default: 5).",
        type=int,
        default=5
    )
    parser.add_argument(
        "--no-resume",
        help="Start fresh, ignoring any previous progress.",
        action="store_true"
    )

    args = parser.parse_args()

    try:
        run_batch_pipeline(
            file_path=args.file_path,
            api_key=args.api_key,
            model=args.model,
            max_workers=args.max_workers,
            resume=not args.no_resume
        )
    except Exception as e:
        print(f"\nERROR: Pipeline failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
