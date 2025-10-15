# Excel Shrinker v6

A high-performance Excel analysis toolkit for boundary detection, format detection, and LLM-powered analysis.

## Project Structure

```
ExcelShrinkerv6/
├── boundary_detector/          # Boundary detection module
│   ├── core/
│   ├── models/
│   └── ...
├── compression/                # Format and inverted index compression
│   ├── format_detector/
│   └── ...
├── llm_analyzer/               # LLM analysis module
│   └── ...
├── sample_data/                # Sample Excel files
│   └── sample_excerpt_fin.xlsx
│
├── pipeline.py                 # Main pipeline script
├── requirements.txt            # Python dependencies
└── README.md
```

## Pipeline Overview

This toolkit provides a complete, end-to-end pipeline for analyzing complex Excel files. The process is executed by a single script and consists of four main stages:

1.  **Boundary Detection**: Identifies the true used range of a worksheet to avoid processing millions of empty cells.
2.  **Format Compression**: Consolidates cell format information into a compact, range-based representation.
3.  **Inverted Index Compression**: Further compresses the data by deduplicating repeated string values, significantly reducing JSON size.
4.  **LLM Analysis**: Uses a Large Language Model (e.g., GPT-5, GPT-4o) to interpret the compressed data and generate a human-readable markdown report detailing the spreadsheet's structure.

## Installation

1.  Clone the repository.
2.  Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Quick Start

The entire analysis pipeline is run from the command line via `pipeline.py`.

**Usage:**

```bash
python pipeline.py [FILE_PATH] --api_key [YOUR_API_KEY] [OPTIONS]
```

**Example:**

To analyze the `Fin` sheet in the sample file and save the output to `Financial_Analysis.md`, run:

```bash
python pipeline.py "sample_data/sample_excerpt_fin.xlsx" \
    --sheet "Fin" \
    --api_key "sk-..." \
    --model "gpt-5" \
    --output_file "Financial_Analysis.md"
```

### Arguments

-   `FILE_PATH`: (Required) Path to the Excel file.
-   `--api_key`: (Required) Your OpenAI API key.
-   `--sheet`: (Optional) The name of the sheet to analyze. If omitted, the first sheet is used.
-   `--model`: (Optional) The LLM model to use (e.g., `gpt-5`, `gpt-4o`). Defaults to `gpt-5`.
-   `--output_file`: (Optional) The path to save the markdown report. Defaults to `analysis_output.md`.

## Dependencies

- `python-calamine` - Fast Excel reading (Rust-based)
- `openpyxl` - Excel format code extraction
- `openai` - LLM analysis (optional)

## License

MIT
