import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None

def get_categories():
    """
    Test case for verifying the categories response from the /get-categories endpoint.
    This ensures that the status, message, and categories data are correctly returned.
    """
    print("Running test_get_categories")
    client = TokenClient()
    # The API URL for fetching categories
    categories_url = f"{BASE_URL}/get-categories"  # Replace with your actual endpoint

    # Send the GET request to fetch categories
    response = client.get(categories_url)

    # Debug: Print the response for inspection
    print(f"Response: {response.json()}")

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains 'status' and it equals 'success'
    assert response_data.get('status') == 'success', f"Expected status 'success', but got {response_data.get('status')}"

    # Check if the response contains the correct 'message'
    assert response_data.get('message') == 'Categories fetched successfully', f"Expected message 'Categories fetched successfully', but got {response_data.get('message')}"

    # Check if 'data' contains 'categories'
    data = response_data.get('data')
    assert data is not None, "Expected 'data' to be present in the response."

    # Check if 'categories' exists in 'data'
    categories = data.get('categories')
    assert categories is not None, "'categories' not found in 'data'."

    # Verify that each category contains 'name' and 'attributes'
    for category in categories:
        assert 'name' in category, f"Category {category} is missing 'name'."
        assert 'attributes' in category, f"Category {category} is missing 'attributes'."
        
        # Verify that attributes is a list
        assert isinstance(category['attributes'], list), f"Attributes for category {category['name']} should be a list."
        
        # Check that each attribute contains 'name' and 'description'
        for attribute in category['attributes']:
            assert 'name' in attribute, f"Attribute {attribute} is missing 'name'."
            assert 'description' in attribute, f"Attribute {attribute} is missing 'description'."

    # Optional: Print the response for debugging
    print(f"Response Data: {response_data}")