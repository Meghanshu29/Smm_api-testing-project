import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.Platform import platform_get, platform_post

def test_platform():
    """Test case for getting platform data."""
    print("Running test_platform_get")
    # Call the function to get platform data
    platform_get()
    platform_post()
    

    