import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Extract_pdf import extract_pdf

def test_run_extract_pdf():
    """Test case for running extract PDF functionality."""
    print("Running test_run_extract_pdf")
    extract_pdf()