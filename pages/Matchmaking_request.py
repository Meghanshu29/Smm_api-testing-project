import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')



def matchmaking_request():
    """
    Test case for sending a matchmaking request.
    This ensures that the matchmaking request is successfully sent between the user and the candidate.
    """
    print("Running test_matchmaking_request")
    client = TokenClient()
    # Ensure userId and candidateId are available
    user_id = registered_user.get('userId', None)
    assert user_id is not None, "User ID is missing. Make sure the user is registered first."

    candidate_id = "U391749470693"  # Replace this with a valid candidate ID for the test
    assert candidate_id is not None, "Candidate ID is missing."

    # The API URL for sending matchmaking request
    matchmaking_request_url = f"{BASE_URL}/matchmaking/request"

    # Prepare the payload with userId and candidateId
    request_data = {
        'userId': user_id,           # User ID of the person sending the request
        'candidateId': candidate_id  # Candidate ID to whom the matchmaking request is being sent
    }

    # Send the POST request to send matchmaking request
    response = client.post(matchmaking_request_url, json=request_data)

    # Assertions to verify the response
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Verify that the response is valid JSON
    try:
        response_data = response.json()
    except ValueError as e:
        assert False, f"Response is not a valid JSON: {e}"

    # Check if the response contains 'status' and 'message'
    assert 'status' in response_data, "Response does not contain 'status'."
    assert 'message' in response_data, "Response does not contain 'message'."

    # Verify that the message indicates success or request status
    assert 'success' in response_data.get('status', '').lower(), f"Matchmaking request failed: {response_data.get('message')}"

    # Optional: Print the response for debugging purposes
    print(f"Response: {response.json()}")