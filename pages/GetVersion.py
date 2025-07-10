import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None

def get_Version_data_and_verify_json():
    """
    Test case for verifying the JSON response from the GET request.
    This ensures that the status, message, and result data are correctly returned.
    """
    print("Running test_get_Version_data_and_verify_json")
    client = TokenClient()
    # The API URL for fetching the data
    api_url = f"{BASE_URL}//get-version-info"  # Replace with the actual endpoint

    # Send the GET request to fetch the data
    response = client.get(api_url)

    # Debug: Print the response for inspection
    print(f"Response: {response.json()}")

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains 'status' and it equals 'success'
    assert response_data.get('status') == 'success', f"Expected status 'success', but got {response_data.get('status')}"

    # Check if the response contains the correct 'message'
    assert response_data.get('message') == 'data fetched successfully', f"Expected message 'data fetched successfully', but got {response_data.get('message')}"

    # Check if 'result' contains 'version' and 'release'
    result = response_data.get('result')
    assert result is not None, "Expected 'result' to be present in the response."
    assert 'version' in result, "'version' not found in 'result'."
    assert 'release' in result, "'release' not found in 'result'."

    # Verify the version and release data (optional based on expected values)
    assert result.get('version') == '1.0.2', f"Expected version '1.0.2', but got {result.get('version')}"
    assert result.get('release') == 'latest', f"Expected release 'latest', but got {result.get('release')}"

    # Optional: Print the response for debugging
    print(f"Response Data: {response_data}")
    