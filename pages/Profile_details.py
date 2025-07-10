import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')


def load_profile_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def profile_details():
  
    print("Running test_profile_details")
    client = TokenClient()
    user_id = registered_user.get('userId', None) 
    assert user_id is not None, "User registration failed, userId is missing."
    MatrimonialId = registered_user.get('matrimonialId', None) 
    assert MatrimonialId is not None, "User registration failed, matrimonialId is missing."
    profile_data = load_profile_data("profile_data.json")
    print(f"Registered User ID: {user_id}")
    print(f"Registered User Data: {registered_user}")
    profile_data["preference"]["userId"] = user_id
    profile_data["preference"]["matrimonialId"] = MatrimonialId
    profile_data["matrimonial"]["matrimonialId"] = MatrimonialId
    profile_details_url = f"{BASE_URL}/profile-details"
    response = client.post(profile_details_url, json=profile_data)
    assert response.status_code == 201  
    response_data = response.json()
    assert 'success' in response_data.get('status', '').lower(), f"Profile details submission failed: {response_data.get('message')}"
    print(f"Response: {response.json()}")


