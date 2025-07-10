import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None

def publish_match():
    """
    Test case for publishing a match using userId and candidateUserId.
    This ensures that the match is successfully published.
    """
    print("Running test_publish_match")
    client = TokenClient()
    # Ensure the userId and candidateUserId are available from the registered_user (global variable)
    user_id = registered_user.get('userId', None)  # Replace with appropriate key if necessary
    candidate_user_id = "U391749470693"  # Assuming you have a candidate user ID available
    
    assert user_id is not None, "User ID is missing. Make sure the user is registered first."
    assert candidate_user_id is not None, "Candidate User ID is missing. Make sure the candidate is registered."

    # The API URL for publishing the match
    publish_match_url = f"{BASE_URL}/publish-match"

    # Prepare the JSON payload for publishing the match
    publish_match_data = {
        "userId": user_id,
        "candidateUserId": candidate_user_id
    }

    # Send the POST request to publish the match
    response = client.post(publish_match_url, json=publish_match_data)

    # Debug: Print the response
    print(f"Response Status: {response.status_code}")
    print(f"Response Body: {response.text}")

    # Assertions to verify the response
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    response_data = response.json()

    # Check if the response contains a success message
    assert 'success' in response_data.get('status', '').lower(), f"Publish match failed: {response_data.get('message')}"

    # Optional: Print the response for debugging
    print(f"Response: {response.json()}")
    
    