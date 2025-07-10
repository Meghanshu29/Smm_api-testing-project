import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None


def matchmaking_results():
    """
    Test case for getting matchmaking results using userId.
    This ensures that matchmaking results are successfully fetched for the user.
    """
    print("Running test_matchmaking_results")
    client = TokenClient()
    # Ensure userId is available from the registered_user (global variable)
    user_id = registered_user.get('userId', None)
    
    assert user_id is not None, "User ID is missing. Make sure the user is registered first."

    # The API URL for fetching matchmaking results
    matchmaking_results_url = f"{BASE_URL}/matchmaking-results"

    # Prepare the payload with userId
    params = {
        'userId': user_id
    }

    # Send the GET request to fetch matchmaking results
    response = client.get(matchmaking_results_url, params=params)

    # Assertions to verify the response
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Verify that the response contains valid JSON
    try:
        response_data = response.json()
    except ValueError as e:
        assert False, f"Response is not a valid JSON: {e}"
    
    # Check if the response contains 'status' and 'message'
    assert 'status' in response_data, "Response does not contain 'status'."
    assert 'message' in response_data, "Response does not contain 'message'."

    # Check if the response contains expected data (for example, 'results')
    assert 'results' in response_data, "Response does not contain 'results'."

    # Optional: Verify that the 'results' key contains data (you can add more checks here as per your response structure)
    results = response_data.get('results')
    assert len(results) > 0, "No matchmaking results found for the given user."

    # Print the response for debugging purposes
    print(f"Response: {response.json()}")