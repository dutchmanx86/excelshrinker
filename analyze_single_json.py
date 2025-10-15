"""
Run LLM inference on a single compressed JSON file.
Useful for testing the analysis on specific sheets.
"""
import json
import sys
from pathlib import Path

try:
    import vertexai
    from vertexai.generative_models import GenerativeModel
    VERTEXAI_AVAILABLE = True
except ImportError:
    VERTEXAI_AVAILABLE = False
    print("ERROR: google-cloud-aiplatform not installed.")
    print("Install with: pip install google-cloud-aiplatform")
    sys.exit(1)

# Paths
BASE_DIR = Path(__file__).parent
OUTPUT_BASE = BASE_DIR / "output" / "batch"
JSON_DIR = OUTPUT_BASE / "json"
MARKDOWN_DIR = OUTPUT_BASE / "markdown"
SERVICE_ACCOUNT_FILE = BASE_DIR / "gemini_service_account.json"

# The JSON file to analyze
JSON_FILE = JSON_DIR / "Historical Quota& Productivity_compressed.json"

# Gemini prompt (same as in gemini_full_pipeline.py)
ANALYSIS_PROMPT = """You are an expert financial analyst tasked with creating a high-level summary of an Excel spreadsheet's structure. Your goal is to identify and describe the key logical data sections (e.g., "Income Statement," "Balance Sheet," "KPI Dashboard") without listing every single row or label. The output must be a structured markdown document that enables a future AI to quickly understand the sheet's layout and retrieve specific sections by cell range.

# CORE OBJECTIVE
Identify major financial or data sections, describe their purpose, and define their precise boundaries and time series context.

# CRITICAL: MULTIPLE TIME SERIES DETECTION
Many spreadsheets have MULTIPLE time series sections side-by-side:
- **Annual columns** (e.g., columns showing years like 2015, 2016, 2017...)
- **Monthly/Quarterly columns** (e.g., columns showing monthly dates like 2015-01-31, 2015-02-28... or quarters like Q1 2024, Q2 2024...)

When analyzing time series:
1. Look for MULTIPLE date header rows or columns with different frequencies
2. Check if there are gaps between column groups (suggesting separate time series)
3. Identify if data spans different date column groups
4. Report ALL time series horizons found, not just one

# OUTPUT REQUIREMENTS
Generate a markdown document with the following EXACT structure:

## 1. Spreadsheet Overview
- **Sheet Name**: The name of the analyzed sheet.
- **Key Sections Identified**: A bulleted list of the main sections you discovered (e.g., "Header," "Income Statement," "Cash Flow Projections").

## 2. Detailed Section Analysis
For EACH logical section identified, create a subsection.

### Section Name (e.g., "Income Statement")
- **Section Type**: Classify the section. Examples: `Standard P&L`, `Custom P&L`, `Balance Sheet`, `Waterfall Chart Data`, `Key Metrics Table`.
- **Description & Purpose**: Briefly explain what this section represents and its business purpose.
- **Cell Range**: The exact and complete cell range for this entire logical section (e.g., `A5:FS88`). This is critical for future data retrieval.
- **Layout Structure**:
    - **Row Headers Location**
    - **Column Headers Location**
    - **Data Range**: The cell range containing the actual numeric values/formulas. If there are multiple time series, specify each:
      - Annual data: `E7:Q24` (numeric values for annual periods)
      - Monthly data: `T7:FS24` (numeric values for monthly periods)
- **Time Series Details**:
    - **Date Range**: The start and end dates/periods covered for EACH time series:
      - Annual: 2015 to 2027 (example)
      - Monthly: 2015-01-31 to 2027-12-31 (example)
    - **Frequency**: The time interval for EACH series (e.g., `Annual`, `Monthly`, `Quarterly`)
- **Key Components**: List the major row labels/metrics in this section (e.g., Revenue, COGS, Gross Profit, EBITDA). DO NOT list every single row.
- **Notes & Customizations**: Mention any deviations from standard reports, or special calculations.

# GUIDING PRINCIPLES
- **High-Level, Not Granular**: Focus on the forest, not the trees. Summarize sections, don't transcribe them.
- **Precision is Key**: Cell ranges and date locations must be exact for future retrieval.
- **Context Over Content**: Explain the *purpose* of a section, not just what's in it.
- **Resolve References**: Use the actual string values from the `inverted_index` section of the JSON, not `{"$ref": ...}` placeholders.
- **Multiple Time Series**: If you see evidence of multiple date columns with different frequencies, report them ALL.

Now, analyze the provided compressed JSON and generate the complete, high-level structured documentation."""


def analyze_json_file(json_path: Path, project_id: str, output_path: Path = None) -> str:
    """
    Analyze a single compressed JSON file with Gemini.

    Args:
        json_path: Path to compressed JSON file
        project_id: Google Cloud project ID
        output_path: Optional path to save markdown output

    Returns:
        Generated markdown analysis
    """
    print(f"\n{'='*80}")
    print(f"ANALYZING: {json_path.name}")
    print(f"{'='*80}\n")

    # Load JSON
    print("Loading JSON...")
    with open(json_path, 'r', encoding='utf-8') as f:
        compressed_json = json.load(f)

    json_size = json_path.stat().st_size
    print(f"  File size: {json_size:,} bytes ({json_size/1024:.1f} KB)")

    # Show some stats
    stats = compressed_json.get('compression_stats', {})
    if stats:
        print(f"  Original size: {stats.get('original_size_bytes', 0):,} bytes")
        print(f"  Compression ratio: {stats.get('compression_ratio', 0):.1%}")

    # Convert to string for prompt
    json_str = json.dumps(compressed_json, indent=2)

    # Create full prompt
    full_prompt = f"{ANALYSIS_PROMPT}\n\n# Compressed JSON Data\n\n```json\n{json_str}\n```"

    print(f"\nInitializing Vertex AI...")
    vertexai.init(project=project_id, location="us-central1")

    print(f"Generating analysis with Gemini 2.0 Flash...")
    model = GenerativeModel("gemini-2.0-flash-exp")

    response = model.generate_content(
        full_prompt,
        generation_config={
            "max_output_tokens": 8192,
            "temperature": 0.3,
        }
    )

    analysis = response.text

    if not analysis or len(analysis.strip()) == 0:
        raise ValueError("Empty response from Gemini")

    print(f"  Generated {len(analysis)} characters")

    # Save if output path provided
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(analysis)
        print(f"\nSaved markdown to: {output_path}")

    return analysis


def main():
    """Run analysis on single JSON file"""

    if not VERTEXAI_AVAILABLE:
        return

    # Verify JSON file exists
    if not JSON_FILE.exists():
        print(f"ERROR: JSON file not found: {JSON_FILE}")
        print(f"\nAvailable JSON files:")
        if JSON_DIR.exists():
            for f in sorted(JSON_DIR.glob("*.json")):
                print(f"  - {f.name}")
        return

    # Set up service account
    import os
    if not SERVICE_ACCOUNT_FILE.exists():
        print(f"ERROR: Service account file not found: {SERVICE_ACCOUNT_FILE}")
        return

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(SERVICE_ACCOUNT_FILE)

    # Load project ID
    with open(SERVICE_ACCOUNT_FILE, 'r') as f:
        sa_data = json.load(f)
    project_id = sa_data['project_id']

    # Determine output filename
    output_filename = JSON_FILE.stem.replace("_compressed", "_analysis.md")
    output_path = MARKDOWN_DIR / output_filename

    try:
        analysis = analyze_json_file(JSON_FILE, project_id, output_path)

        print(f"\n{'='*80}")
        print("ANALYSIS COMPLETE")
        print(f"{'='*80}\n")

        # Show first few lines of analysis
        lines = analysis.split('\n')
        preview_lines = lines[:20]
        print("Preview (first 20 lines):")
        print("-" * 80)
        for line in preview_lines:
            print(line)
        if len(lines) > 20:
            print(f"\n... ({len(lines) - 20} more lines)")
        print("-" * 80)

    except Exception as e:
        print(f"\n{'='*80}")
        print(f"ERROR: {e}")
        print(f"{'='*80}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
