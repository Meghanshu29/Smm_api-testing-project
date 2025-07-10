import os
import pytest
import requests
from conftest import registered_user
import json
from client import TokenClient


BASE_URL = os.getenv('BASE_URL')


def download_bio_data():
    """
    Test case for downloading biodata using matrimonialId.
    This ensures that the biodata is successfully downloaded for the registered user.
    """
    print("Running test_download_bio_data")
    client = TokenClient()

    # Ensure the matrimonialId is available in the registered_user
    matrimonial_id = registered_user.get('matrimonialId', None)  # Fetching matrimonialId
    assert matrimonial_id is not None, "User registration failed, matrimonialId is missing."

    # The API URL for downloading biodata
    download_bio_data_url = f"{BASE_URL}/download-bio-data"

    # Prepare the parameters with the matrimonialId for the GET request
    params = {
        'matrimonialId': matrimonial_id  # Matrimonial ID to fetch biodata for the user
    }

    # Send the GET request to download biodata
    response = client.get(download_bio_data_url, params=params)  # Use params for GET requests

    # Debugging: Print the response for inspection
    print(f"Response: {response.json()}")

    # Assertions to verify the response
    assert response.status_code == 200  # Expecting a 200 OK response
    response_data = response.json()

    # Check if the response contains a success message or the downloaded file URL
    assert 'success' in response_data.get('status', '').lower(), f"Bio-data download failed: {response_data.get('message')}"

    # Optional: Print the response for debugging
    print(f"Response: {response.json()}")

    # If the response contains a file URL, you can verify if the file is available
    if 'fileUrl' in response_data:
        print(f"Bio-data available for download at: {response_data['fileUrl']}")
        
    return response_data