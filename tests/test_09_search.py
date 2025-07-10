import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Search_Data import search

def test_run_search():
    """Test case for running search functionality."""
    print("Running test_run_search")
    search()