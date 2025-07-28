import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')

def company_info():
    """
    Test case for verifying the company information response from the /company-info endpoint.
    This ensures that the status, message, and company information data are correctly returned.
    """
    print("Running test_company_info")
    client = TokenClient()

    # The API URL for fetching company information
    company_url = f"{BASE_URL}/company-info"

    # Send the GET request to fetch company information
    response = client.get(company_url)

    # Debug: Print the response for inspection
    print(f"Response: {response.json()}")

    # Assertions to verify the response
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    response_data = response.json()
    assert 'status' in response_data, "'status' key missing in response"
    assert 'message' in response_data, "'message' key missing in response"
    assert 'data' in response_data, "'data' key missing in response"

    # Validate top-level values
    assert response_data['status'] == 'success', f"Expected status 'success', got {response_data['status']}"
    assert response_data['message'], "Message field is empty or null"

    # Validate nested 'data' fields
    data = response_data['data']
    expected_fields = ['body', 'email', 'mobile', 'subject']
    for field in expected_fields:
        assert field in data, f"'{field}' field missing in 'data'"
        assert data[field], f"'{field}' field is empty"

    print("✅ Company info retrieved and validated successfully.")