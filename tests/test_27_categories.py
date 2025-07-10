import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Categories import categories

def test_categories():
    """Test case for categories functionality."""
    print("Running test_categories")
    categories()