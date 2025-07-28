import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None


def login_user():
  
    print("Running test_login_user")
    client = TokenClient()
    User = "U331751695202"
    Password = "Pass12345" 
    extract_pdf_url = f"{BASE_URL}/login"
    login_data = {
        'user': User,
        'password': Password
    }
    response = client.post(extract_pdf_url, json=login_data)
    assert response.status_code == 200, f"Login failed with status code: {response.status_code}"
    print(f"Response: {response.text}")  
    response_data = response.json()
    assert 'success' in response_data.get('status', '').lower(), f"Login failed: {response_data.get('message')}"
