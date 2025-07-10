import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Get_Prefernce_data import get_Prefernce_data_and_verify_json_length

def test_run_get_data():
    """Test case for running get data functionality."""
    print("Running test_run_get_data")
    get_Prefernce_data_and_verify_json_length()