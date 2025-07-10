import sys
import os
import pytest

from conftest import registered_user
from client import TokenClient

BASE_URL = os.getenv('BASE_URL')

def enable_user():
    """
    Test case for enabling a user by sending a PUT request to the /enable-user endpoint.
    Raises an exception if the response status is not 'success' or status code is not 200.
    """
    print("Running test_enable_user")
    
    client = TokenClient()

    # Extract the user ID from the registered_user fixture
    user_id = registered_user.get('userId', None)
    print(f"User ID being sent: {user_id}")
    
    if user_id is None:
        raise ValueError("User ID is missing. Make sure the registration test ran first.")
    
    
    try:
           # Send the PUT request with userId as a query parameter
        response = client.put(f"{BASE_URL}enable-user?userId={user_id}")
        # Check if the response status code is 200 (OK)
        if response.status_code != 200:
            raise Exception(f"Expected status code 200, but got {response.status_code}.")
        
        # Parse and check the response data
        response_data = response.json()
        if 'success' not in response_data.get('status', '').lower():
            raise Exception(f"User enabling failed: {response_data.get('message')}")
        
        print(f"Response: {response.json()}")
        
    except Exception as e:
        # You can log the exception here or raise it again for the test framework to handle
        raise RuntimeError(f"Error occurred while enabling the user: {str(e)}")

