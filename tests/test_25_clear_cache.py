import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Clear_Cache import clear_cache

def test_clear_cache():
    """Test case for clearing cache functionality."""
    print("Running test_clear_cache")
    clear_cache()