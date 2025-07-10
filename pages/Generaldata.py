import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None

def get_general_data():
    """
    Test case for verifying the general data response from the /general-data endpoint.
    This ensures that the status, message, and general data are correctly returned.
    """
    print("Running test_get_general_data")
    client = TokenClient()

    # The API URL for fetching general data
    general_data_url = f"{BASE_URL}/general-data"  # Replace with your actual endpoint

    # Send the GET request to fetch the general data
    response = client.get(general_data_url)

    # Debug: Print the response for inspection
    print(f"Response: {response.json()}")

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains 'status' and it equals 'success'
    general_data = response_data.get('generalData')
    assert general_data is not None, "Expected 'generalData' to be present in the response."

    # Verify 'subCaste' field is in 'generalData' and contains values
    assert 'subCaste' in general_data, "'subCaste' not found in 'generalData'."
    assert isinstance(general_data['subCaste'], list), "'subCaste' is not a list."
    assert len(general_data['subCaste']) > 0, "'subCaste' is empty."

    # Verify 'gotra' field is in 'generalData' and contains values
    assert 'gotra' in general_data, "'gotra' not found in 'generalData'."
    assert isinstance(general_data['gotra'], list), "'gotra' is not a list."
    assert len(general_data['gotra']) > 0, "'gotra' is empty."

    # Verify 'profession' field is in 'generalData' and contains values
    assert 'profession' in general_data, "'profession' not found in 'generalData'."
    assert isinstance(general_data['profession'], list), "'profession' is not a list."
    assert len(general_data['profession']) > 0, "'profession' is empty."

    # Verify 'hobbies' field is in 'generalData' and contains values
    assert 'hobbies' in general_data, "'hobbies' not found in 'generalData'."
    assert isinstance(general_data['hobbies'], list), "'hobbies' is not a list."
    assert len(general_data['hobbies']) > 0, "'hobbies' is empty."

    # Verify 'qualification' field is in 'generalData'
    assert 'qualification' in general_data, "'qualification' not found in 'generalData'."

    # Verify 'language' field is in 'generalData'
    assert 'language' in general_data, "'language' not found in 'generalData'."

    # Optional: Check if 'dietary' is present in 'generalData' if required
    if 'dietary' in general_data:
        assert general_data['dietary'] in ['Vegan', 'Vegetarian', 'Non-Vegetarian'], f"Unexpected dietary value: {general_data['dietary']}"

    # Optional: Print the response data for debugging
    print(f"Response Data: {json.dumps(response_data, indent=2)}")