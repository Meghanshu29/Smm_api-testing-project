import os
import pytest
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global variable to store registered user data
registered_user = {}
registered_matrimonial_user = {}
token = {}

# pytest fixture for setup and teardown
@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    global registered_user  # Ensure you're updating the global variable
    global registered_matrimonial_user
    global token
    print('🌍 Registering user with email:', os.getenv('EMAIL_ADDRESS'))

    try:
        # Register user using the requests library
        response = requests.post(
            f"{os.getenv('BASE_URL')}/register",
            json={
                'phoneNumber': os.getenv('PHONE_NUMBER'),
                'emailAddress': os.getenv('EMAIL_ADDRESS'),
                'googleToken': 'xtweQ9aVTcbMWLjnTno4bkwpvZ02',
                'appVersion': 'Testing',
                'platform': 'web'
            }
        )

        # Log the registration response for debugging
        print('Registration response:', response.json())

        if response.status_code == 200 and response.json().get('status') == 'success':
            # Extract token from response and store it in the global token variable
            token = response.json().get('token')
            registered_user.update(response.json())
            registered_matrimonial_user.update(response.json())  # Store matrimonial user data as well
            registered_user['emailAddress'] = os.getenv('EMAIL_ADDRESS')
            registered_user['phoneNumber'] = os.getenv('PHONE_NUMBER')
            print('✅ Registered:', registered_user)
      

        else:
            print(f"❌ Registration failed: {response.json().get('message')}")

        # Yield to run the tests
        yield

    except Exception as e:
        print('❌ Registration failed:', str(e))
        raise e

    # finally:
    #     # Cleanup (optional, as per your test needs)
    #     print('🧹 Cleaning up test user...')
    #     try:
    #         user_id = registered_user.get('userid')
    #         email = registered_user.get('emailAddress')

    #         deletion_status = False

    #         if user_id:
    #             # Delete user by ID
    #             requests.delete(f"{os.getenv('BASE_URL')}/users/{user_id}")
    #             deletion_status = True
    #         elif email:
    #             # Delete user by email
    #             requests.delete(f"{os.getenv('BASE_URL')}/users?email={email}")
    #             deletion_status = True

    #         if deletion_status:
    #             print('✅ User deleted successfully.')
    #         else:
    #             print('⚠️ No identifier found to delete user.')

    #     except Exception as err:
    #         print('❌ Failed to delete user:', str(err))
