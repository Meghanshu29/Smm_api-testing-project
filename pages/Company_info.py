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

    # Check if the response contains 'status' and it equals 'success'
    assert response_data.get('status') == 'success', f"Expected status 'success', but got {response_data.get('status')}"
    
    # Check if company information is present in the response
    assert 'data' in response_data, "Company data is missing in the response"
    
    company_data = response_data.get('data')
    assert company_data is not None, "Company information data is null"
    
    # Verify specific data fields exist
    assert 'email' in company_data, "Email field is missing"
    assert 'mobile' in company_data, "Mobile field is missing"
    assert 'subject' in company_data, "Subject field is missing"
    assert 'body' in company_data, "Body field is missing"
    
    # Verify fields are not empty
    assert company_data['email'], "Email field is empty"
    assert company_data['mobile'], "Mobile field is empty"
    assert company_data['subject'], "Subject field is empty"
    assert company_data['body'], "Body field is empty"
    
    # Verify message exists
    assert 'message' in response_data, "Message field is missing"
    assert response_data.get('message'), "Message field is empty"
    
    print("Company info retrieved and validated successfully!")
