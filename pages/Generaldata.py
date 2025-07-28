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
       # Check if the response contains 'generalData', 'message', and 'status'
    assert 'generalData' in response_data, "'generalData' is missing in the response."
    assert 'status' in response_data, "'status' is missing in the response."
    assert response_data['status'] == 'success', f"Expected status 'success', but got {response_data['status']}"

    general_data = response_data['generalData']

    # Define a helper function to check if a list field exists and has values
    def check_field(field_name):
        assert field_name in general_data, f"'{field_name}' not found in 'generalData'."
        assert isinstance(general_data[field_name], list), f"'{field_name}' is not a list."
        assert len(general_data[field_name]) > 0, f"'{field_name}' is empty."

    # Check required fields
    check_field('subCaste')
    check_field('gotra')
    check_field('profession')
    check_field('hobbies')

    # Verify 'qualification' and 'language' fields exist
    assert 'qualification' in general_data, "'qualification' not found in 'generalData'."
    assert 'language' in general_data, "'language' not found in 'generalData'."

    # Optional: Check if 'dietary' is present in 'generalData' if required
    if 'dietary' in general_data:
        assert general_data['dietary'] in ['Vegan', 'Vegetarian', 'Non-Vegetarian'], \
            f"Unexpected dietary value: {general_data['dietary']}"

    # Optional: Print the response data for debugging
    print(f"Response Data: {json.dumps(response_data, indent=2)}")