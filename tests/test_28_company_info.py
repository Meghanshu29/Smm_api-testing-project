import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.Company_info import company_info

def test_company_info():
    """Test case for company information functionality."""
    print("Running test_company_info")
    company_info()