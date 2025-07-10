import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')
pdf_link = None



def upload_biodata_success():
    user_id = registered_user.get('userId', None) 
    matrimonial_id = registered_user.get('matrimonialId', None) 
    assert user_id is not None, "User registration failed, userId is missing."
    client = TokenClient()
    print(f"Registered User ID: {user_id}")
    print(f"Registered User Data: {registered_user}")
    biodata_url = f"{BASE_URL}/upload-biodata"
    biodata_file = 'C:\\Users\\RaDhey\\Downloads\\Akshat.pdf'  
    if not os.path.isfile(biodata_file):
        print(f"File not found at path: {biodata_file}")
        assert False, f"File not found at path: {biodata_file}"
    biodata_data = {
        'matrimonialId': matrimonial_id, 
        'appVersion': 'TestingApp',  
    }
    with open(biodata_file, 'rb') as file: 
        files = {'file': (os.path.basename(biodata_file), file)}  
        response = client.post(biodata_url, data=biodata_data, files=files)
    assert response.status_code == 200
    response_data = response.json()
    
    global pdf_link
    pdf_link = response_data.get('filename', None)  
    assert pdf_link is not None, "PDF link not found in the response."
    
    assert 'success' in response_data.get('status', '').lower(), f"Biodata upload failed: {response_data.get('message')}"
    
    