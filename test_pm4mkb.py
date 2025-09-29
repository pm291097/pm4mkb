"""
test_pm4mkb.py - Test script for renamed PM4MKB library
"""

import sys
from pathlib import Path

# Add PM4MKB to path (renamed from sberpm)
sys.path.insert(0, str(Path(r"C:\Users\polos\Downloads\sberpm-3.4.0\sberpm-3.4.0")))

# Import from pm4mkb instead of sberpm
from pm4mkb.visualization_v2 import ConformanceAnalyzer, ProcessStandard

print("=" * 60)
print("TESTING PM4MKB LIBRARY (formerly SberPM)")
print("=" * 60)

# Create analyzer
analyzer = ConformanceAnalyzer()

# Simple test
print("\nRunning conformance analysis with PM4MKB...")
result = analyzer.analyze(
    r"C:\Users\polos\Downloads\data.xlsx",
    case_col="DOC_ID",
    activity_col="NAM",
    timestamp_col="START_TIME",
    case_id="123456789",
    mark_as_optional=["PAUSE"],
    show=True
)

print(f"\n✅ PM4MKB library working!")
print(f"Analysis complete: {result}")
