import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Get_categories import get_categories

def test_run_categories():
    """Test case for running categories functionality."""
    print("Running test_run_categories")
    get_categories()