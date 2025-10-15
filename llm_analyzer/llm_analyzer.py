"""LLM-based analysis of compressed Excel format detection results"""

import json
import os
import time
from typing import Optional, Dict, Any


# Prompt for analyzing compressed JSON - Optimized for consistent structured output
ANALYSIS_PROMPT = """You are an expert financial analyst tasked with creating a high-level summary of an Excel spreadsheet's structure. Your goal is to identify and describe the key logical data sections (e.g., "Income Statement," "Balance Sheet," "KPI Dashboard") without listing every single row or label. The output must be a structured markdown document that enables a future AI to quickly understand the sheet's layout and retrieve specific sections by cell range.

# CORE OBJECTIVE
Identify major financial or data sections, describe their purpose, and define their precise boundaries and time series context.

# OUTPUT REQUIREMENTS
Generate a markdown document with the following EXACT structure:

## 1. Spreadsheet Overview
- **Sheet Name**: The name of the analyzed sheet.
- **Key Sections Identified**: A bulleted list of the main sections you discovered (e.g., "Income Statement," "Cash Flow Projections").

## 2. Detailed Section Analysis
For EACH logical section identified, create a subsection.

### Section Name (e.g., "Income Statement")
- **Section Type**: Classify the section. Examples: `Standard P&L`, `Custom P&L`, `Balance Sheet`, `Waterfall Chart Data`, `Key Metrics Table`.
- **Description & Purpose**: Briefly explain what this section represents and its business purpose.
- **Cell Range**: The exact and complete cell range for this entire logical section (e.g., `A5:Q88`). This is critical for future data retrieval.
- **Time Series Horizon**:
    - **Dates Location**: The cell range containing the primary date or period labels (e.g., `C8:Q8` for columns, `B9:B40` for rows).
    - **Date Range**: The start and end dates covered (e.g., `Q1 2022` to `Q4 2025`).
    - **Frequency**: The time interval (e.g., `Quarterly`, `Monthly`, `Annual`).
- **Key Components**: Identify the major sub-components or labels that define the structure of this section. DO NOT list every label.
- **Notes & Customizations**: Mention any deviations from a standard report. Is it a custom P&L? Are there unusual metrics included?

# GUIDING PRINCIPLES
- **High-Level, Not Granular**: Focus on the forest, not the trees. Summarize sections, don't transcribe them.
- **Precision is Key**: Cell ranges and date locations must be exact for future retrieval.
- **Context Over Content**: Explain the *purpose* of a section, not just what's in it.
- **Resolve References**: Use the actual string values from the `dictionary` section of the JSON, not `{"$ref": ...}` placeholders.

Now, analyze the provided compressed JSON and generate the complete, high-level structured documentation."""


def create_llm_analysis(
    compressed_json: Dict[str, Any],
    api_key: str,
    model: str = "gpt-5",
    temperature: float = 0.3
) -> str:
    """
    Analyze compressed Excel JSON using ChatGPT API.
    
    Args:
        compressed_json: The compressed format detection result
        api_key: OpenAI API key
        model: Model to use (default: gpt-5)
        temperature: Temperature for generation (default: 0.3 for factual output)
    
    Returns:
        Markdown analysis string
    
    Raises:
        ImportError: If openai package not installed
        Exception: If API call fails
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError(
            "OpenAI package not installed. Install with: pip install openai"
        )
    
    # Initialize client
    client = OpenAI(api_key=api_key)
    
    # Convert JSON to string for prompt
    json_str = json.dumps(compressed_json, indent=2)
    
    # Create the full prompt
    full_prompt = f"{ANALYSIS_PROMPT}\n\n# Compressed JSON Data\n\n```json\n{json_str}\n```"
    
    try:
        # Call the API
        # Note: gpt-5 does not support temperature parameter, only default value of 1
        print(f"Using model: {model}")
        print("Sending request to OpenAI API...")
        
        api_params = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a precise Excel data structure analyst. "
                        "You create well-structured, consistent markdown documentation that maps "
                        "spreadsheet layouts for data retrieval. You follow templates exactly and "
                        "provide complete, accurate cell range mappings. You always resolve dictionary "
                        "references to their actual values for clarity."
                    )
                },
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            "max_completion_tokens": 64000,  # Increased to allow for reasoning + detailed output
            "timeout": 600  # 10 minute timeout for longer processing
        }
        
        # Only add temperature for models that support it (not gpt-5)
        if not model.startswith("gpt-5"):
            api_params["temperature"] = temperature
        
        print("Waiting for response (this may take a while for gpt-5)...")
        start_time = time.time()
        response = client.chat.completions.create(**api_params)
        elapsed_time = time.time() - start_time
        print(f"Response received! (took {elapsed_time:.1f} seconds)")
        
        # Extract the analysis
        analysis = response.choices[0].message.content
        finish_reason = response.choices[0].finish_reason
        
        # Debug: Check response details
        print(f"Finish reason: {finish_reason}")
        print(f"Tokens used - Prompt: {response.usage.prompt_tokens}, Completion: {response.usage.completion_tokens}")
        if hasattr(response.usage.completion_tokens_details, 'reasoning_tokens'):
            print(f"Reasoning tokens: {response.usage.completion_tokens_details.reasoning_tokens}")
        
        # Check if content is empty or truncated
        if not analysis or len(analysis.strip()) == 0:
            print("\nWARNING: Received empty response from API!")
            print(f"This likely means the model used all tokens for reasoning with none left for output.")
            print(f"Consider using a model without extended reasoning (like gpt-4o) or increasing max_completion_tokens further.")
            raise Exception("API returned empty content. Model may have used all tokens for reasoning.")
        
        if finish_reason == 'length':
            print(f"\nWARNING: Response was truncated due to token limit!")
            print(f"The analysis may be incomplete. Consider increasing max_completion_tokens.")
        
        print(f"Analysis generated successfully ({len(analysis)} characters)")
        return analysis
        
    except Exception as e:
        raise Exception(f"OpenAI API call failed: {str(e)}")


def analyze_compressed_file(
    compressed_file_path: str,
    api_key: str,
    output_file_path: Optional[str] = None,
    model: str = "gpt-5"
) -> str:
    """
    Analyze a compressed JSON file and optionally save the result.
    
    Args:
        compressed_file_path: Path to compressed JSON file
        api_key: OpenAI API key
        output_file_path: Optional path to save markdown output
        model: Model to use
    
    Returns:
        Markdown analysis string
    """
    # Load compressed JSON
    with open(compressed_file_path, 'r') as f:
        compressed_json = json.load(f)
    
    # Generate analysis
    print("Calling ChatGPT API to analyze spreadsheet structure...")
    start_time = time.time()
    analysis = create_llm_analysis(compressed_json, api_key, model)
    total_time = time.time() - start_time
    
    # Save if requested
    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(analysis)
        print(f"Analysis saved to: {output_file_path}")
    
    print(f"Total processing time: {total_time:.1f} seconds ({total_time/60:.1f} minutes)")
    
    return analysis


def analyze_from_env(
    compressed_file_path: str = "format_detection_compressed.json",
    output_file_path: str = "spreadsheet_analysis.md",
    model: str = "gpt-5"
) -> str:
    """
    Analyze using API key from environment variable OPENAI_API_KEY.
    
    Args:
        compressed_file_path: Path to compressed JSON
        output_file_path: Path to save output
        model: Model to use
    
    Returns:
        Markdown analysis
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable not set. "
            "Set it with: export OPENAI_API_KEY=your-key-here"
        )
    
    return analyze_compressed_file(compressed_file_path, api_key, output_file_path, model)