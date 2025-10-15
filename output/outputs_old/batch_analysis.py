"""Batch analysis of all sheets in an Excel file with compression metrics"""

import sys
import json
import time
import os
import concurrent.futures
from pathlib import Path
from tqdm import tqdm
sys.path.append(str(Path(__file__).parent))

from boundary_detector.core.boundary_detector import BoundaryDetector
from boundary_detector.models.detection_config import DetectionConfig
from compression.format_compression import compress_formats
from compression.inverted_index_compression import compress_format_result_json

# Worker function for parallel processing
def process_sheet(args):
    """
    Analyze a single sheet, save its JSON, and return metrics.
    This function is designed to be called by a multiprocessing pool.
    """
    file_path, sheet_name, config, output_folder, sheet_index = args
    
    try:
        # Step 1: Boundary Detection
        boundary_detector = BoundaryDetector(config)
        boundary_result = boundary_detector.detect(file_path, sheet_name, detect_charts=False)

        # Step 2: Format Compression
        format_result = compress_formats(
            file_path=file_path,
            sheet_name=sheet_name,
            boundary_result=boundary_result,
            config=config,
            verbose=False # Suppress output in parallel mode
        )

        # Convert to JSON and measure size
        format_json = json.loads(format_result.to_json())
        format_json_str = json.dumps(format_json)
        format_json_size = len(format_json_str)

        # Step 3: Inverted Index Compression
        compressed_result = compress_format_result_json(format_json, min_occurrences=2)
        compressed_json_str = json.dumps(compressed_result)
        inverted_size = len(compressed_json_str)

        # Choose smaller version
        if inverted_size < format_json_size:
            final_json = compressed_result
            final_size = inverted_size
            used_compression = True
        else:
            final_json = format_json
            final_size = format_json_size
            used_compression = False

        # Save the final JSON to a file
        safe_sheet_name = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in sheet_name)
        json_filename = f"{sheet_index:03d}_{safe_sheet_name}.json"
        json_path = os.path.join(output_folder, json_filename)
        with open(json_path, 'w') as f:
            json.dump(final_json, f, indent=2)

        # Return metrics (without the large JSON object)
        return {
            'sheet_name': sheet_name,
            'cells_analyzed': format_result.cells_analyzed,
            'format_ranges': len(format_result.format_ranges),
            'format_time_ms': format_result.processing_time_ms,
            'format_json_size': format_json_size,
            'inverted_size': inverted_size,
            'used_compression': used_compression,
            'final_size': final_size
        }
    except Exception as e:
        return {'sheet_name': sheet_name, 'error': str(e)}


def batch_analyze(file_path: str, output_folder: str = "output_json"):
    """
    Analyze all sheets in an Excel file in parallel and save JSON files.
    """
    print(f"\n{'='*100}")
    print(f"BATCH ANALYSIS: {file_path}")
    print(f"{'='*100}\n")

    from python_calamine import CalamineWorkbook
    workbook = CalamineWorkbook.from_path(file_path)
    sheet_names = workbook.sheet_names
    print(f"Found {len(sheet_names)} sheets\n")

    os.makedirs(output_folder, exist_ok=True)
    print(f"Output folder: {output_folder}\n")

    config = DetectionConfig()
    results = []
    
    tasks = [(file_path, name, config, output_folder, i+1) for i, name in enumerate(sheet_names)]

    total_start = time.time()
    
    # Use ProcessPoolExecutor to run tasks in parallel
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Use tqdm for a progress bar
        future_to_sheet = {executor.submit(process_sheet, task): task for task in tasks}
        
        for future in tqdm(concurrent.futures.as_completed(future_to_sheet), total=len(tasks), desc="Processing sheets"):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                sheet_name = future_to_sheet[future][1]
                results.append({'sheet_name': sheet_name, 'error': str(e)})

    total_time = (time.time() - total_start) / 60  # minutes
    
    # Post-process results
    results.sort(key=lambda x: sheet_names.index(x['sheet_name'])) # Maintain original order
    
    print(f"\n{'#':<4} {'Sheet Name':<35} {'Cells':<8} {'Ranges':<7} {'Time(ms)':<10} "
          f"{'JSON(KB)':<10} {'Method':<12} {'Final(KB)':<10}")
    print("="*105)
    
    total_format_size = 0
    total_final_size = 0
    sheets_using_compression = 0
    
    for i, metrics in enumerate(results, 1):
        if 'error' in metrics:
            print(f"{i:<4} {metrics['sheet_name']:<35} ERROR: {metrics['error']}")
            continue

        total_format_size += metrics['format_json_size']
        total_final_size += metrics['final_size']
        if metrics['used_compression']:
            sheets_using_compression += 1
            
        method = "Inverted" if metrics['used_compression'] else "Original"
        print(f"{i:<4} {metrics['sheet_name']:<35} "
              f"{metrics['cells_analyzed']:<8} "
              f"{metrics['format_ranges']:<7} "
              f"{metrics['format_time_ms']:<10.0f} "
              f"{metrics['format_json_size']/1024:<10.1f} "
              f"{method:<12} "
              f"{metrics['final_size']/1024:<10.1f}")


    # Summary statistics
    print("="*105)
    successful_results = [r for r in results if 'error' not in r]

    if successful_results:
        total_cells = sum(r['cells_analyzed'] for r in successful_results)
        total_ranges = sum(r['format_ranges'] for r in successful_results)
        total_saved = total_format_size - total_final_size
        total_saved_pct = (1 - total_final_size / total_format_size) * 100 if total_format_size > 0 else 0

        print(f"\nSUMMARY:")
        print(f"  Total sheets processed: {len(successful_results)}/{len(sheet_names)}")
        print(f"  Total cells analyzed: {total_cells:,}")
        print(f"  Total format ranges: {total_ranges:,}")
        print(f"  Original JSON size: {total_format_size/1024:.1f} KB")
        print(f"  Final JSON size: {total_final_size/1024:.1f} KB")
        print(f"  Sheets using inverted index: {sheets_using_compression}/{len(successful_results)}")
        print(f"  Total space saved: {total_saved/1024:.1f} KB ({total_saved_pct:.1f}%)")
        print(f"  Total processing time: {total_time:.1f} minutes")
        print(f"  JSON files saved to: {output_folder}/")

    # Save summary
    summary_file = os.path.join(output_folder, "_summary.json")
    output = {
        'file': file_path,
        'total_sheets': len(sheet_names),
        'processed_sheets': len(successful_results),
        'sheets_using_compression': sheets_using_compression,
        'total_format_size_bytes': total_format_size,
        'total_final_size_bytes': total_final_size,
        'space_saved_bytes': total_saved,
        'space_saved_percent': round(total_saved_pct, 1),
        'processing_time_minutes': round(total_time, 2),
        'results': results
    }

    with open(summary_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"  Summary saved to: {summary_file}")


if __name__ == "__main__":
    # Default to sample.xlsx
    file_path = "sample_data/sample.xlsx"

    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    output_folder = sys.argv[2] if len(sys.argv) > 2 else "output_json"

    batch_analyze(file_path, output_folder)
