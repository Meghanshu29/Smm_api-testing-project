import os
import pytest
import requests
from conftest import registered_user
from pages.Get_Stage import get_stage
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')


def update_stage_with_higher_value():
    """
    Sends a new registration stage that is greater than or equal to the currently saved one.
    """
    print("Running test_update_stage_with_higher_value")
    client = TokenClient()
    Data= get_stage()  # Fetch the current stage data
    current_stage= Data.get('registrationStage', None)
    assert current_stage is not None, "Current registration stage is not set."
    user_id = registered_user.get('userId')
    current_stage = registered_user.get('registrationStage')

    assert user_id is not None, "userId is missing"
    assert current_stage is not None, "registrationStage is not set globally"

    # ✅ Ensure new stage is only updated if not equal to 6 and less than 6
    if current_stage != 6 and current_stage < 6:
        new_stage = current_stage + 1  # Apply your logic for increment
    else:
        new_stage = current_stage  # Do nothing if stage is 6 or > 6

    # Endpoint to update the stage
    update_stage_url = f"{BASE_URL}/stages"

    payload = {
        "userId": user_id,
        "registrationStage": new_stage
    }

    response = client.post(update_stage_url, json=payload)
    print(f"Update Response: {response.json()}")

    assert response.status_code == 200
    response_data = response.json()
    assert response_data.get('status') == 'success', "Failed to update stage"

    # ✅ Save new stage globally
    registered_user['registrationStage'] = new_stage
    print(f"Updated stage saved globally: {new_stage}")
