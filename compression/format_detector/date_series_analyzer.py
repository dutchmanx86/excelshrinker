"""Analyze date series to detect patterns and intervals"""

from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
import re


class DateSeriesAnalyzer:
    """Analyze sequences of dates to detect regular intervals"""
    
    @staticmethod
    def parse_iso_date(date_str: str) -> Optional[datetime]:
        """Parse ISO date string to datetime"""
        try:
            return datetime.fromisoformat(date_str)
        except:
            return None
    
    @staticmethod
    def analyze_date_range(dates: List[str]) -> Dict[str, Any]:
        """
        Analyze a list of ISO date strings to detect patterns.

        Args:
            dates: List of ISO date strings (e.g., ["2024-01-01", "2024-04-01"])

        Returns:
            Dictionary with:
            - first_date: Earliest date in the range
            - last_date: Latest date in the range
            - count: Number of dates
            - interval_type: "ascending", "descending", or "unordered"
            - interval_name: "quarterly", "monthly", "yearly", "daily", "weekly", or None
            - interval_days: Average days between dates, or None if unordered
        """
        if not dates or len(dates) < 2:
            return {
                "first_date": dates[0] if dates else None,
                "last_date": dates[0] if dates else None,
                "count": len(dates),
                "interval_type": None,
                "interval_name": None,
                "interval_days": None
            }

        # Parse all dates
        parsed_dates = [DateSeriesAnalyzer.parse_iso_date(d) for d in dates]
        parsed_dates = [d for d in parsed_dates if d is not None]

        if len(parsed_dates) < 2:
            return {
                "first_date": dates[0],
                "last_date": dates[-1],
                "count": len(dates),
                "interval_type": None,
                "interval_name": None,
                "interval_days": None
            }

        # Get original order for checking ascending/descending
        original_dates = parsed_dates.copy()

        # Sort dates to find first and last
        sorted_dates = sorted(parsed_dates)

        # Remove consecutive duplicates from sorted dates
        unique_dates = []
        for date in sorted_dates:
            if not unique_dates or date != unique_dates[-1]:
                unique_dates.append(date)

        # Need at least 2 unique dates
        if len(unique_dates) < 2:
            return {
                "first_date": sorted_dates[0].date().isoformat(),
                "last_date": sorted_dates[-1].date().isoformat(),
                "count": len(parsed_dates),
                "interval_type": None,
                "interval_name": None,
                "interval_days": None
            }

        # Check if dates are in ascending or descending order
        is_ascending = original_dates == sorted(original_dates)
        is_descending = original_dates == sorted(original_dates, reverse=True)

        if not is_ascending and not is_descending:
            # Dates are unordered
            return {
                "first_date": unique_dates[0].date().isoformat(),
                "last_date": unique_dates[-1].date().isoformat(),
                "count": len(unique_dates),
                "interval_type": "unordered",
                "interval_name": None,
                "interval_days": None
            }

        # Dates are ordered - calculate intervals
        intervals = []
        for i in range(len(unique_dates) - 1):
            delta = unique_dates[i + 1] - unique_dates[i]
            intervals.append(delta.days)

        # Check if intervals are regular (all the same or very close)
        if not intervals:
            interval_type = "ascending" if is_ascending else "descending"
            interval_name = None
            avg_interval = None
        else:
            avg_interval = sum(intervals) / len(intervals)
            max_interval = max(intervals)
            min_interval = min(intervals)

            # Determine tolerance based on interval type
            # For monthly intervals (28-32 days), use 4 day tolerance (accounts for month variations)
            # For quarterly (88-95 days), use 7 day tolerance
            # For others, use 10% of average interval
            if 28 <= avg_interval <= 32:
                # Monthly - allow for 28-31 day months
                tolerance = 4
            elif 88 <= avg_interval <= 95:
                # Quarterly - allow for varying quarter lengths
                tolerance = 7
            elif 60 <= avg_interval <= 65:
                # Bimonthly
                tolerance = 5
            else:
                # General tolerance: 10% of average
                tolerance = max(2, avg_interval * 0.1)

            is_regular = (max_interval - min_interval) <= tolerance

            # Determine interval type
            interval_type = "ascending" if is_ascending else "descending"

            # Classify interval name if regular enough
            if is_regular:
                interval_name = DateSeriesAnalyzer._classify_interval(avg_interval)
            elif avg_interval > 0 and (max_interval - min_interval) / avg_interval < 0.15:
                # Approximately regular
                interval_name = DateSeriesAnalyzer._classify_interval(avg_interval)
            else:
                # Irregular spacing
                interval_name = None

        return {
            "first_date": unique_dates[0].date().isoformat(),
            "last_date": unique_dates[-1].date().isoformat(),
            "count": len(unique_dates),
            "interval_type": interval_type,
            "interval_name": interval_name,
            "interval_days": round(avg_interval) if avg_interval else None
        }
    
    @staticmethod
    def _classify_interval(days: float) -> str:
        """
        Classify interval in days to a named period.
        
        Args:
            days: Average number of days between dates
        
        Returns:
            Interval name: "daily", "weekly", "monthly", "quarterly", "semi-annual", "yearly"
        """
        if days <= 1:
            return "daily"
        elif 6 <= days <= 8:
            return "weekly"
        elif 13 <= days <= 16:
            return "biweekly"
        elif 28 <= days <= 32:
            return "monthly"
        elif 60 <= days <= 65:
            return "bimonthly"
        elif 88 <= days <= 95:
            return "quarterly"
        elif 175 <= days <= 185:
            return "semi-annual"
        elif 360 <= days <= 370:
            return "yearly"
        else:
            return f"custom_{round(days)}_days"