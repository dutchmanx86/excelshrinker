# Project Overview: Excel Analysis and Compression Pipeline

This project provides a suite of tools to analyze, compress, and understand complex Excel spreadsheets. The pipeline is designed to process large files efficiently and generate structured, human-readable summaries of their contents. It consists of three main stages:

1.  **Boundary Detection**: Quickly finds the true data boundaries within a sheet.
2.  **Format Compression**: Intelligently compresses the structural and format information.
3.  **LLM Analysis**: Uses a Large Language Model to interpret the compressed data and create a structured overview.

---

## 1. Boundary Detection

**Purpose**: To efficiently determine the actual used range of a worksheet, avoiding unnecessarily scanning millions of empty cells.

**How it Works**:
-   It uses the high-performance `python-calamine` (Rust-based) library for rapid cell scanning.
-   It scans from top-to-bottom and left-to-right, stopping after it encounters a configurable number of consecutive empty rows or columns.
-   Optionally, it can also detect the location of charts on the worksheet.

**Key Benefit**: Massively speeds up subsequent processing steps by narrowing the scope to only the relevant data area. Processing an entire 86-sheet workbook takes ~6 seconds.

**Further Reading**: [`boundary_detector/API_REFERENCE.md`](boundary_detector/API_REFERENCE.md)

---

## 2. Compression

This stage involves two distinct types of compression applied sequentially.

### a) Format Compression

**Purpose**: To consolidate cell format information into a compact representation, reducing redundancy from individual cell formats.

**How it Works**:
-   It identifies the number format (`currency`, `percentage`, `date`, etc.) of each cell within the detected boundaries.
-   It groups adjacent cells with identical formats into continuous ranges (e.g., `A1:Z1` are all `currency`).
-   It has specialized logic to detect and consolidate common time series patterns (e.g., `Q1 2024`, `Q2 2024`, ...).

**Key Benefit**: Reduces the granularity of the data from per-cell to per-range, creating a much smaller and more manageable dataset that describes the sheet's structure.

### b) Inverted Index Compression

**Purpose**: To further compress the JSON output from the format compression step by deduplicating repeated string values.

**How it Works**:
-   It scans the JSON data for string values that appear multiple times (e.g., the label "Revenue" appearing in several locations).
-   It creates a dictionary (an "inverted index") where each repeated value is stored once, mapped to a list of all its locations.
-   The original locations are replaced with a simple reference to the dictionary entry.

**Key Benefit**: Significantly reduces the size of the final JSON output, often by 30-70%, making it cheaper to store and faster to transmit, especially for LLM analysis.

**Further Reading**: [`compression/API_REFERENCE.md`](compression/API_REFERENCE.md)

---

## 3. LLM Analysis

**Purpose**: To transform the technical, compressed JSON data into a structured, human-readable markdown document that explains the spreadsheet's layout and purpose.

**How it Works**:
-   It sends the compressed JSON data to a Large Language Model (e.g., GPT-5, GPT-4o) with a specialized prompt.
-   The prompt instructs the model to act as a data analyst, interpreting the format ranges and value dictionary to identify logical sections (e.g., "Income Statement," "Key Metrics").
-   The model generates a markdown report detailing these sections, their corresponding cell ranges, and any relevant time series information.

**Key Benefit**: Provides an automated, high-level "map" of the spreadsheet, enabling users to quickly understand its structure and locate important information without needing to manually inspect the file.

**Further Reading**: [`llm_analyzer/API_REFERENCE.md`](llm_analyzer/API_REFERENCE.md)