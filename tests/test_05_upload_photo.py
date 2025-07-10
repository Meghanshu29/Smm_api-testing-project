import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Upload_photo import upload_photos

def test_run_upload_photo():
    """Test case for running photo upload functionality."""
    print("Running test_run_upload_photo")
    upload_photos()