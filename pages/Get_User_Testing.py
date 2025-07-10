import sys
import os
import pytest
from conftest import registered_user
from client import TokenClient
import json


BASE_URL = os.getenv('BASE_URL')

def get_user_testing():
    
    client = TokenClient()
    matrimonial_id = registered_user.get('matrimonialId', None)  
    assert matrimonial_id is not None, "Matrimonial ID is missing. Make sure the user is registered."
    
    response =client.get(f"{BASE_URL}/get-users-testing?matrimonialId={matrimonial_id}")
    assert response.status_code == 200, f"Failed to get user testing data with status code: {response.status_code}"
    response_data = response.json()
    Data = response_data.get('data', None)
    assert Data is not None, "No data found in the response."
    assert response_data.get('status') == 'success', f"Expected status 'success', but got {response_data.get('status')}"
    assert response_data.get('message') == 'Users data fetched successfully', f"Expected message 'Users data fetched successfully', but got {response_data.get('message')}"
