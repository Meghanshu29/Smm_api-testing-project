import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.GetVersion import get_Version_data_and_verify_json

def test_run_version():
    """Test case for running version functionality."""
    print("Running test_run_version")
    get_Version_data_and_verify_json()