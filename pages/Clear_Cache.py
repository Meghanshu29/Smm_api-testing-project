import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
def clear_cache():
    """
    Test case for clearing the cache via the DELETE method.
    """
    print("Running test_clear_cache")
    client = TokenClient()

    # API URL for clearing the cache
    clear_cache_url = f"{BASE_URL}/clean-cache"
    
    # Send the DELETE request
    response = client.delete(clear_cache_url)
    print(f"response: {response.text}   ")  # Debugging output
    # Verify the response status code
    assert response.status_code == 200, f"Failed to clear cache, status code: {response.status_code}"
    
    # Verify the JSON response
    response_data = response.json()
    assert response_data.get("status") == "success", "Status is not success."
    assert response_data.get("message") == "Cache cleared successfully.", "Message mismatch."
    
    # Optional: Print the response for debugging
    print(f"Response: {response.json()}")