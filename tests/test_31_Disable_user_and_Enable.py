import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Disable_User import disable_user
from pages.Enable_User import enable_user

def test_Disable_And_Enable_User():
    """Test case for disabling a user."""
    print("Running test_disable_user")
    # Call the function to disable a user
    disable_user()
    print("Running test_enable_user")
    """Test case for enabling a user."""
    print("Running test_enable_user")
    # Call the function to enable a user
    enable_user()
    
   