import os
import google.generativeai as genai

# --- Configuration ---
# For ease of use in this testing script, the API key is hardcoded.
# In a production environment, use a secure method like environment variables.
API_KEY = "AIzaSyBkVdzBlXlNqQRIpK0cUXBc8QVdwTYx2mM"
MODEL_NAME = "gemini-2.5-pro"
MARKDOWN_FILE = r"output\batch\MASTER_WORKBOOK_ANALYSIS.md"

BASE_PROMPT = """
You are an expert data-analysis lookup assistant. You will receive a markdown document that describes an Excel model: sheets, sections (e.g., “Income Statement”), and time-series ranges.

Retrieval Objective
Return cell ranges for the smallest valid block that actually exists in the document, prioritizing summary output sheets. When a user asks for a metric that belongs to a section (e.g., Income Statement) 
and the markdown does not specify row-level line items, you must:
 - Retrieve the entire section block that contains the metric,
 - Clip that block to the requested date range (with buffer), and
 - Do not invent row labels or sub-ranges that are not explicitly documented.

Absolutely Do / Never Do
 - Do return block-level ranges when labels are unspecified.
 - Do include three ranges per answer:
   * Row Label Range
   * Column Label Range
   * Data Range: the interior data cells of the section.
 - Never infer or fabricate specific line items (e.g., “Gross Margin”) unless the markdown explicitly lists them.
 - Never narrow to a single row if the markdown only names a section.

Time Series Rules (with Buffer)
 - Detect the section’s full time axis (e.g., T2:FS2) and its frequency + start (e.g., “Monthly starting Jan 2015”).
 - There may be multiple time series of data.  Use the one most relevant to the user's query.
 - Compute the column/row subset for the requested date window.
 - Add a buffer of two periods before and after.
 - Clip Row Label Range, Column Label Range, and Data Range to that subset.
 - If the requested window partially falls outside the available series, return the intersecting subset and note the truncation in a one-line remark.

Orientation & Section Boundary Detection
 - Orientation: Determine if the time axis is columns (dates across a header row) or rows (dates down a header column). Choose ranges accordingly.
 - Section boundaries: A section starts at its named header (e.g., “Income Statement”) and ends at the next section header or a clearly defined boundary in the markdown. Use that rectangle as the section block.
 - If the markdown gives only a sheet name + section name (no cell coords), return the sheet + computed block based on the section’s described span and time axis.

Output Format (max 3 sections)

Return at most the 3 most relevant sections. For each, output only the following JSON object:

{
  "sheet": "SheetName",
  "section": "SectionName",
  "row_label_range": "A6:A40",
  "column_label_range": "F3:K3",
  "data_range": "F6:K40",
  "full_time_range": "C3:N3",
  "notes": "Clipped to requested window + 2-period buffer. No row-level labels specified; returned full section block."
}

Selection Rules
 - Summary sheets first (e.g., Executive Summary, Consolidated Summary).
 - If multiple matching sections exist, pick the highest aggregation level unless the query specifies otherwise.
 - If the query names a specific line item and the markdown lists it, return its row sub-range; otherwise, fall back to the section block.

Sanity Checks Before Responding
 - If row or column labels are not explicitly provided, confirm notes explains that you returned the full section block without fabricated labels.
 - Verify ranges are contiguous rectangles and align with the orientation.

Ensure time clipping + buffer is reflected in all ranges.
"""

def main():
    """
    Main function to run the CLI-based Excel workbook analyzer.
    """
    print("--- Excel Workbook Analyzer ---")

    # --- Initialize Gemini ---
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)
        chat = model.start_chat(history=[])
        print(f"Successfully initialized model: {MODEL_NAME}")
    except Exception as e:
        print(f"Error initializing Gemini: {e}")
        return

    # --- Load Markdown File ---
    try:
        with open(MARKDOWN_FILE, "r", encoding="utf-8") as f:
            markdown_content = f.read()
        print(f"Successfully loaded '{MARKDOWN_FILE}'.")
    except FileNotFoundError:
        print(f"Error: The file '{MARKDOWN_FILE}' was not found.")
        return

    # --- Initial Prompt with Markdown Content ---
    print("\nSending initial context to the model. This may take a moment...")
    initial_prompt = f"{BASE_PROMPT}\n\nHere is the content of the markdown file:\n\n{markdown_content}"
    chat.send_message(initial_prompt)
    print("Context loaded. You can now ask questions about the workbook.")

    # --- Main Interaction Loop ---
    while True:
        try:
            query = input("\nEnter your question (or 'quit' to exit): ")
            if query.lower() in ["quit", "exit"]:
                print("Exiting analyzer. Goodbye!")
                break

            if not query.strip():
                continue
            
            # Formulate the user's turn
            user_prompt = f"The user's query is: '{query}'. Find the 3 most relevant ranges as per the base prompt, please."

            print("\nSending query to the model...")
            response = chat.send_message(user_prompt)

            print("\n--- Model Response ---")
            print(response.text)
            print("----------------------")

        except KeyboardInterrupt:
            print("\nExiting analyzer. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break

if __name__ == "__main__":
    main()