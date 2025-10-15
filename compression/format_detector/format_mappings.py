"""Excel number format mappings and classification logic"""

from typing import Optional, Set


# Currency symbols that indicate currency formatting
CURRENCY_SYMBOLS: Set[str] = {
    '$', '€', '£', '¥', '₹', 'R$', 'kr', 'zł', 
    '₪', '₩', '₱', '฿', 'Rp', 'S$', '₦', '₡',
    'CHF', 'د.إ', 'ر.س', '₪', '₴', '₸', '₮'
}

# Built-in Excel format codes for currency
# Source: https://support.microsoft.com/en-us/office/number-format-codes-5026bbd6-04bc-48cd-bf33-80f18b4eae68
CURRENCY_FORMAT_CODES: Set[int] = {
    5, 6, 7, 8,      # Currency formats: $#,##0_);($#,##0), etc.
    41, 42, 43, 44   # Accounting formats
}

# Built-in Excel format codes for percentage
PERCENTAGE_FORMAT_CODES: Set[int] = {
    9, 10, 11, 12    # 0%, 0.00%, various percentage formats
}

# Built-in Excel format codes for dates
DATE_FORMAT_CODES: Set[int] = {
    14, 15, 16, 17,  # m/d/yy, d-mmm-yy, d-mmm, mmm-yy
    22,              # m/d/yy h:mm (date+time but primarily date)
    27, 28, 29, 30, 31, 32, 33, 34, 35, 36,  # Various date formats
    50, 57           # Additional date formats
}

# Built-in Excel format codes for time
TIME_FORMAT_CODES: Set[int] = {
    18, 19, 20, 21,  # h:mm AM/PM, h:mm:ss AM/PM, h:mm, h:mm:ss
    45, 46, 47       # mm:ss, [h]:mm:ss, mm:ss.0
}

# Built-in Excel format codes for numbers
NUMBER_FORMAT_CODES: Set[int] = {
    1, 2, 3, 4,      # 0, 0.00, #,##0, #,##0.00
    37, 38, 39, 40,  # #,##0;(#,##0), #,##0;[Red](#,##0), etc.
    48, 49           # Scientific notation
}

# Format code 0 is "General" - will be treated as number
GENERAL_FORMAT_CODE: int = 0

# Text format code
TEXT_FORMAT_CODE: int = 49


def classify_format(number_format: str, format_id: int) -> str:
    """
    Classify an Excel number format into one of our categories.
    
    Args:
        number_format: The Excel format string (e.g., "$#,##0.00", "0.00%")
        format_id: The Excel format ID number (0-49 are built-in, 164+ are custom)
    
    Returns:
        Format category: 'number', 'currency', 'percentage', 'string', 'date', 'time', 'other'
    
    Examples:
        >>> classify_format("$#,##0.00", 5)
        'currency'
        >>> classify_format("0.00%", 10)
        'percentage'
        >>> classify_format("m/d/yyyy", 14)
        'date'
    """
    # First check built-in format codes (most reliable)
    if format_id in CURRENCY_FORMAT_CODES:
        return 'currency'
    
    if format_id in PERCENTAGE_FORMAT_CODES:
        return 'percentage'
    
    if format_id in DATE_FORMAT_CODES:
        return 'date'
    
    if format_id in TIME_FORMAT_CODES:
        return 'time'
    
    if format_id in NUMBER_FORMAT_CODES:
        return 'number'
    
    if format_id == GENERAL_FORMAT_CODE:
        return 'number'
    
    # For custom formats (164+) or unknown built-ins, analyze the format string
    if number_format:
        format_lower = number_format.lower()
        
        # Check for currency symbols
        if any(symbol in number_format for symbol in CURRENCY_SYMBOLS):
            return 'currency'
        
        # Check for percentage
        if '%' in number_format:
            return 'percentage'
        
        # Check for date patterns (simplified - common patterns)
        date_patterns = ['d', 'm', 'y', 'mmm', 'ddd', 'yyyy', 'yy']
        if any(pattern in format_lower for pattern in date_patterns):
            # Distinguish between date and time
            time_patterns = ['h', 's', 'am', 'pm', 'a/p']
            has_time = any(pattern in format_lower for pattern in time_patterns)
            has_date = any(pattern in format_lower for pattern in ['d', 'mmm', 'yyyy', 'yy'])
            
            if has_date and not has_time:
                return 'date'
            elif has_time and not has_date:
                return 'time'
            elif has_date and has_time:
                # Date+time combo - classify as date (primary component)
                return 'date'
        
        # Check for time-only patterns
        if any(pattern in format_lower for pattern in ['h:mm', 'h:ss', '[h]', 'am/pm', 'a/p']):
            return 'time'
        
        # Check for text format
        if format_lower == '@' or format_lower == 'text':
            return 'string'
        
        # Check for number patterns
        if any(char in number_format for char in ['0', '#', ',']):
            # Could be a number format
            return 'number'
    
    # Default to 'other' for unrecognized formats
    return 'other'


def is_currency_format(number_format: str, format_id: int) -> bool:
    """
    Check if a format is a currency format.
    
    Args:
        number_format: The Excel format string
        format_id: The Excel format ID number
    
    Returns:
        True if the format is currency
    """
    return classify_format(number_format, format_id) == 'currency'


def is_percentage_format(number_format: str, format_id: int) -> bool:
    """
    Check if a format is a percentage format.
    
    Args:
        number_format: The Excel format string
        format_id: The Excel format ID number
    
    Returns:
        True if the format is percentage
    """
    return classify_format(number_format, format_id) == 'percentage'


def is_date_format(number_format: str, format_id: int) -> bool:
    """
    Check if a format is a date format.
    
    Args:
        number_format: The Excel format string
        format_id: The Excel format ID number
    
    Returns:
        True if the format is date
    """
    return classify_format(number_format, format_id) == 'date'


def is_time_format(number_format: str, format_id: int) -> bool:
    """
    Check if a format is a time format.
    
    Args:
        number_format: The Excel format string
        format_id: The Excel format ID number
    
    Returns:
        True if the format is time
    """
    return classify_format(number_format, format_id) == 'time'


def get_format_scale(number_format: str) -> Optional[int]:
    """
    Detect scaling in custom formats (e.g., thousands, millions).
    
    Format strings can include commas to scale numbers:
    - One comma (,): divide by 1,000 (thousands)
    - Two commas (,,): divide by 1,000,000 (millions)
    - Three commas (,,,): divide by 1,000,000,000 (billions)
    
    Args:
        number_format: The Excel format string
    
    Returns:
        Scale divisor (1000, 1000000, etc.) or None if no scaling
    
    Examples:
        >>> get_format_scale("$#,##0,")
        1000
        >>> get_format_scale("$#,##0,,")
        1000000
        >>> get_format_scale("$#,##0")
        None
    """
    if not number_format:
        return None
    
    # Count trailing commas after the last digit placeholder
    # Example: "$#,##0,," has 2 trailing commas
    trailing_commas = 0
    in_trailing = False
    
    for char in reversed(number_format):
        if char == ',':
            if in_trailing:
                trailing_commas += 1
            else:
                # First comma after digit placeholder
                in_trailing = True
                trailing_commas = 1
        elif char in '0#?':
            # Digit placeholder - continue checking
            continue
        elif in_trailing:
            # Hit non-comma, non-digit - stop counting
            break
    
    if trailing_commas > 0:
        return 1000 ** trailing_commas
    
    return None