import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Upload_bio_data import upload_biodata_success

def test_run_upload_biodata():
    """Test case for running biodata upload functionality."""
    print("Running test_run_upload_biodata")
    upload_biodata_success()