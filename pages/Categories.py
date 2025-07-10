import os
import sys
sys.path.append('..')
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None

def categories():
    """
    Test case for verifying the categories response from the /get-categories endpoint.
    This ensures that the status, message, and categories data are correctly returned.
    """
    print("Running test_get_categories")
    client = TokenClient()
    

    # The API URL for fetching categories
    categories_url = f"{BASE_URL}/categories"  # Replace with your actual endpoint

    # Send the GET request to fetch categories
    response = client.get(categories_url)

    # Debug: Print the response for inspection
    print(f"Response: {response.json()}")

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

   
    categories = response_data.get('Categories')
    assert categories is not None, "Expected 'Categories' key in response"

    # Define expected data
    expected_categories = [
        {"CategoryId": 1, "CategoryName": "Personality Insights"},
        {"CategoryId": 2, "CategoryName": "Lifestyle Preferences"},
        {"CategoryId": 3, "CategoryName": "Family Values"},
        {"CategoryId": 4, "CategoryName": "Bride-Specific Questions"},
        {"CategoryId": 5, "CategoryName": "Groom-Specific Questions"},
        {"CategoryId": 6, "CategoryName": "Shared Questions"}
    ]

    # Assert data matches expected categories
    assert categories == expected_categories, f"Expected categories do not match. Got: {categories}"