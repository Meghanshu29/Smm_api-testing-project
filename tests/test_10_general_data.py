import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Generaldata import get_general_data

def test_run_general_data():
    """Test case for running general data functionality."""
    print("Running test_run_general_data")
    get_general_data()