import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')


def get_stage():
    """
    Test case for verifying the stage response from the /get-stage endpoint.
    This ensures that the status, message, and registrationStage data are correctly returned.
    """
    print("Running test_get_stage")
    client = TokenClient()
    # Ensure the userId is available in the registered_user
    user_id = registered_user.get('userId', None)
    assert user_id is not None, "User registration failed, userId is missing."

    # The API URL for fetching stage data
    get_stage_url = f"{BASE_URL}/get-stage"

    # Prepare the payload with the userId
    params = {
        'userId': user_id
    }

    # Send the GET request
    response = client.get(get_stage_url, params=params)

    # Debug: Print response
    print(f"Response: {response.json()}")

    # Assertions
    assert response.status_code == 200
    response_data = response.json()

    assert response_data.get('status') == 'success', f"Expected status 'success', but got {response_data.get('status')}"
    assert response_data.get('message') == 'found user stage', f"Expected message 'found user stage', but got {response_data.get('message')}"

    registration_stage = response_data.get('registrationStage')
    assert registration_stage is not None, "'registrationStage' not found in the response."
    assert isinstance(registration_stage, int), "'registrationStage' should be an integer."
    assert registration_stage > 0, f"Expected 'registrationStage' to be a positive number, but got {registration_stage}"

    # ✅ Save globally
    registered_user['registrationStage'] = registration_stage

    # Debug: Print for verification
    print(f"Registration stage saved globally: {registered_user['registrationStage']}")
    
    return response_data  # Return the response data for further processing if needed