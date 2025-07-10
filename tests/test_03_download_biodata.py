import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Download_Biodata import download_bio_data

def test_run_download_biodata():
    """Test case for running download biodata functionality."""
    print("Running test_run_download_biodata")
    download_bio_data()