import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')

def company_info():
    """
    Test case for verifying the company information response from the /get-company-info endpoint.
    This ensures that the status, message, and company information data are correctly returned.
    """
    print("Running test_get_categories")
    client = TokenClient()

    # The API URL for fetching categories
    company_url = f"{BASE_URL}/company-info"  # Replace with your actual endpoint

    # Send the GET request to fetch categories
    response = client.get(company_url)

    # Debug: Print the response for inspection
    print(f"Response: {response.json()}")

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains 'status' and it equals 'success'
    assert response_data.get('status') == 'success', f"Expected status 'success', but got {response_data.get('status')}"
