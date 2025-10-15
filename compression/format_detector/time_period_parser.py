"""Parser for time period strings (quarters, fiscal years, etc.)"""

import re
from typing import Optional, Dict, Any
from datetime import date


class TimePeriodParser:
    """
    Parser for time period strings commonly found in financial spreadsheets.
    
    Supported formats:
    - Quarters: 1Q24, 2Q24, Q1 24, Q2-24, Q3 2024
    - Fiscal Years: FY24, FY2024, FY 24
    - Calendar Years: CY24, CY2024, CY 24
    """
    
    # Quarter mapping to month (start of quarter)
    QUARTER_TO_MONTH = {
        1: 1,   # Q1 starts in January
        2: 4,   # Q2 starts in April
        3: 7,   # Q3 starts in July
        4: 10   # Q4 starts in October
    }
    
    # Regex patterns for different time period formats
    PATTERNS = {
        'quarter_prefix': re.compile(r'^([1-4])Q[- ]?(\d{2,4})$', re.IGNORECASE),  # 1Q24, 2Q2024
        'quarter_q_prefix': re.compile(r'^Q([1-4])[- ]?(\d{2,4})$', re.IGNORECASE),  # Q1 24, Q2-24
        'fiscal_year': re.compile(r'^FY[- ]?(\d{2,4})$', re.IGNORECASE),  # FY24, FY2024
        'calendar_year': re.compile(r'^CY[- ]?(\d{2,4})$', re.IGNORECASE),  # CY24, CY2024
    }
    
    @staticmethod
    def _normalize_year(year_str: str) -> int:
        """
        Convert 2-digit or 4-digit year string to 4-digit year.
        
        Args:
            year_str: Year as string (e.g., "24" or "2024")
        
        Returns:
            4-digit year as integer
        
        Examples:
            >>> TimePeriodParser._normalize_year("24")
            2024
            >>> TimePeriodParser._normalize_year("2024")
            2024
        """
        year = int(year_str)
        
        if year < 100:
            # 2-digit year - assume 2000s if < 50, else 1900s
            if year < 50:
                year += 2000
            else:
                year += 1900
        
        return year
    
    @classmethod
    def is_time_period(cls, value: str) -> bool:
        """
        Check if a string matches any time period pattern.
        
        Args:
            value: String to check
        
        Returns:
            True if the string matches a time period pattern
        
        Examples:
            >>> TimePeriodParser.is_time_period("1Q24")
            True
            >>> TimePeriodParser.is_time_period("Q2 2024")
            True
            >>> TimePeriodParser.is_time_period("Revenue")
            False
        """
        if not isinstance(value, str):
            return False
        
        value = value.strip()
        
        for pattern in cls.PATTERNS.values():
            if pattern.match(value):
                return True
        
        return False
    
    @classmethod
    def parse_to_date(cls, value: str, fiscal_year_start_month: int = 1) -> Optional[str]:
        """
        Parse time period string to ISO date string.
        
        Args:
            value: Time period string (e.g., "1Q24", "FY2024")
            fiscal_year_start_month: Month when fiscal year starts (default: 1 = January)
        
        Returns:
            ISO date string (YYYY-MM-DD) representing the start of the period,
            or None if parsing fails
        
        Examples:
            >>> TimePeriodParser.parse_to_date("1Q24")
            '2024-01-01'
            >>> TimePeriodParser.parse_to_date("Q3 2024")
            '2024-07-01'
            >>> TimePeriodParser.parse_to_date("FY24")
            '2024-01-01'
        """
        if not isinstance(value, str):
            return None
        
        value = value.strip()
        
        # Try quarter patterns (prefix like 1Q24)
        match = cls.PATTERNS['quarter_prefix'].match(value)
        if match:
            quarter = int(match.group(1))
            year = cls._normalize_year(match.group(2))
            month = cls.QUARTER_TO_MONTH[quarter]
            return date(year, month, 1).isoformat()
        
        # Try quarter patterns (Q prefix like Q1 24)
        match = cls.PATTERNS['quarter_q_prefix'].match(value)
        if match:
            quarter = int(match.group(1))
            year = cls._normalize_year(match.group(2))
            month = cls.QUARTER_TO_MONTH[quarter]
            return date(year, month, 1).isoformat()
        
        # Try fiscal year pattern
        match = cls.PATTERNS['fiscal_year'].match(value)
        if match:
            year = cls._normalize_year(match.group(1))
            return date(year, fiscal_year_start_month, 1).isoformat()
        
        # Try calendar year pattern
        match = cls.PATTERNS['calendar_year'].match(value)
        if match:
            year = cls._normalize_year(match.group(1))
            return date(year, 1, 1).isoformat()
        
        return None
    
    @classmethod
    def get_period_info(cls, value: str, fiscal_year_start_month: int = 1) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a time period string.
        
        Args:
            value: Time period string
            fiscal_year_start_month: Month when fiscal year starts (default: 1)
        
        Returns:
            Dictionary with period details, or None if not a valid time period
            
        Example return:
            {
                'period_type': 'quarter',
                'quarter': 1,
                'year': 2024,
                'start_date': '2024-01-01',
                'end_date': '2024-03-31'
            }
        """
        if not isinstance(value, str):
            return None
        
        value = value.strip()
        
        # Try quarter patterns (prefix like 1Q24)
        match = cls.PATTERNS['quarter_prefix'].match(value)
        if match:
            quarter = int(match.group(1))
            year = cls._normalize_year(match.group(2))
            start_month = cls.QUARTER_TO_MONTH[quarter]
            
            # Calculate end date (last day of quarter)
            if quarter < 4:
                end_month = cls.QUARTER_TO_MONTH[quarter + 1] - 1
                end_year = year
            else:
                end_month = 12
                end_year = year
            
            # Get last day of end month
            if end_month in [1, 3, 5, 7, 8, 10, 12]:
                end_day = 31
            elif end_month in [4, 6, 9, 11]:
                end_day = 30
            else:  # February
                # Simple leap year check
                if end_year % 4 == 0 and (end_year % 100 != 0 or end_year % 400 == 0):
                    end_day = 29
                else:
                    end_day = 28
            
            return {
                'period_type': 'quarter',
                'quarter': quarter,
                'year': year,
                'start_date': date(year, start_month, 1).isoformat(),
                'end_date': date(end_year, end_month, end_day).isoformat()
            }
        
        # Try quarter patterns (Q prefix like Q1 24)
        match = cls.PATTERNS['quarter_q_prefix'].match(value)
        if match:
            quarter = int(match.group(1))
            year = cls._normalize_year(match.group(2))
            # Reuse logic from above
            return cls.get_period_info(f"{quarter}Q{year}", fiscal_year_start_month)
        
        # Try fiscal year pattern
        match = cls.PATTERNS['fiscal_year'].match(value)
        if match:
            year = cls._normalize_year(match.group(1))
            start_month = fiscal_year_start_month
            
            # Fiscal year typically runs for 12 months
            if start_month == 1:
                end_month = 12
                end_year = year
            else:
                end_month = start_month - 1
                end_year = year + 1
            
            # Get last day of end month
            if end_month in [1, 3, 5, 7, 8, 10, 12]:
                end_day = 31
            elif end_month in [4, 6, 9, 11]:
                end_day = 30
            else:  # February
                if end_year % 4 == 0 and (end_year % 100 != 0 or end_year % 400 == 0):
                    end_day = 29
                else:
                    end_day = 28
            
            return {
                'period_type': 'fiscal_year',
                'year': year,
                'start_date': date(year, start_month, 1).isoformat(),
                'end_date': date(end_year, end_month, end_day).isoformat()
            }
        
        # Try calendar year pattern
        match = cls.PATTERNS['calendar_year'].match(value)
        if match:
            year = cls._normalize_year(match.group(1))
            return {
                'period_type': 'calendar_year',
                'year': year,
                'start_date': date(year, 1, 1).isoformat(),
                'end_date': date(year, 12, 31).isoformat()
            }
        
        return None