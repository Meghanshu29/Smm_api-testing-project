import os
import pytest
import requests
from conftest import registered_user
from client import TokenClient

BASE_URL = os.getenv('BASE_URL')



def upload_photos():
    print("Running test_upload_photos")
    
    # Ensure matrimonialId is available
    matrimonial_id = registered_user.get('matrimonialId', None)
    assert matrimonial_id is not None, "User registration failed, matrimonialId is missing."
    client = TokenClient()
    # API URL for uploading photos
    upload_photos_url = f"{BASE_URL}/profile/upload-photos"
    
    # File paths for photos
    photo_file_1 = 'C:\\Users\\RaDhey\\Downloads\\pic1.jpg'  # Replace with the correct file path
    photo_file_2 = 'C:\\Users\\RaDhey\\Downloads\\pic2.jpg'  # Replace with the correct file path

    # Check if the photo files exist
    if not os.path.isfile(photo_file_1):
        print(f"File not found at path: {photo_file_1}")
        assert False, f"File not found at path: {photo_file_1}"
    
    if not os.path.isfile(photo_file_2):
        print(f"File not found at path: {photo_file_2}")
        assert False, f"File not found at path: {photo_file_2}"

    # Prepare the files in the required format
    with open(photo_file_1, 'rb') as file1, open(photo_file_2, 'rb') as file2:
        file_list = [
            ('photos', (os.path.basename(photo_file_1), file1, 'image/jpeg')),
            ('photos', (os.path.basename(photo_file_2), file2, 'image/jpeg'))
        ]
        data = {'matrimonialId': matrimonial_id}
        
        # Send the POST request to upload the photos
        response = client.post(upload_photos_url, data=data, files=file_list)
        print(f"Response: {response.json()}")  # Debugging output

    # Assertions to verify the response
    assert response.status_code == 201  
    response_data = response.json()

    # Ensure 'success' is in the response status
    assert 'success' in response_data.get('status', '').lower(), f"Photo upload failed: {response_data.get('message')}"
    print(f"Response: {response.json()}")

    # Assuming the response contains URLs in the response_data, extract them
    uploaded_photos_urls = []
    if 'photos' in response_data:
        for photo in response_data['photos']:  # Assuming 'photos' contains a list of uploaded photo data
            photo_url = photo.get('url', None)  # Assuming each photo has a 'url' key
            if photo_url:
                uploaded_photos_urls.append(photo_url)

    # Print and save the uploaded photo URLs
    print(f"Uploaded Photo URLs: {uploaded_photos_urls}")

    # You can save the URLs to a file or store them globally
    # For example, saving to a file:
    with open('uploaded_photos_urls.txt', 'w') as f:
        for url in uploaded_photos_urls:
            f.write(f"{url}\n")

