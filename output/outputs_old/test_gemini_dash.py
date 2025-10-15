"""
Test improved Gemini prompt on Dash tab to detect multiple time series (annual + monthly)
"""
import json
from pathlib import Path
import vertexai
from vertexai.generative_models import GenerativeModel

# Paths
BASE_DIR = Path(__file__).parent
JSON_FILE = BASE_DIR / "output" / "batch" / "sample_gpt-5-nano" / "json" / "Dash_compressed.json"
SERVICE_ACCOUNT_FILE = BASE_DIR / "gemini_service_account.json"
OUTPUT_FILE = BASE_DIR / "test_dash_improved.md"

# Improved prompt with explicit instructions for multiple time series
IMPROVED_PROMPT = """You are an expert financial analyst tasked with creating a high-level summary of an Excel spreadsheet's structure. Your goal is to identify and describe the key logical data sections (e.g., "Income Statement," "Balance Sheet," "KPI Dashboard") without listing every single row or label. The output must be a structured markdown document that enables a future AI to quickly understand the sheet's layout and retrieve specific sections by cell range.

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
- **Key Sections Identified**: A bulleted list of the main sections you discovered (e.g., “Header,” "Income Statement," "Cash Flow Projections").

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
- **Resolve References**: Use the actual string values from the `inverted_index` section of the JSON, not `{\"$ref\": ...}` placeholders.
- **Multiple Time Series**: If you see evidence of multiple date columns with different frequencies, report them ALL.

Now, analyze the provided compressed JSON and generate the complete, high-level structured documentation."""



def main():
    # Load service account info
    with open(SERVICE_ACCOUNT_FILE, 'r') as f:
        sa_data = json.load(f)
    project_id = sa_data['project_id']

    # Load compressed JSON
    with open(JSON_FILE, 'r') as f:
        compressed_json = json.load(f)

    # Convert to string
    json_str = json.dumps(compressed_json, indent=2)

    # Create full prompt
    full_prompt = f"{IMPROVED_PROMPT}\n\n# Compressed JSON Data\n\n```json\n{json_str}\n```"

    print("Analyzing Dash tab with improved prompt...")
    print(f"JSON file: {JSON_FILE}")
    print(f"Output: {OUTPUT_FILE}\n")

    # Initialize Vertex AI
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(SERVICE_ACCOUNT_FILE)
    vertexai.init(project=project_id, location="us-central1")

    # Create model
    model = GenerativeModel("gemini-2.0-flash-exp")

    # Generate response
    print("Calling Gemini API...")
    response = model.generate_content(
        full_prompt,
        generation_config={
            "max_output_tokens": 8192,
            "temperature": 0.3,
        }
    )

    # Extract text
    analysis = response.text

    # Save output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(analysis)

    print(f"\nDONE! Output saved to: {OUTPUT_FILE}")
    print(f"\nFirst 500 characters:\n{analysis[:500]}...")


if __name__ == "__main__":
    main()