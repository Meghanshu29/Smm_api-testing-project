import requests
from conftest import registered_user  # Import the global registered_user object

class TokenClient:
    def __init__(self):
        # Initialize the session and get the token from registered_user
        self.session = requests.Session()
        token = registered_user.get('token', None)  # Fetch the token from registered_user
        if token:
            self.session.headers.update({'Authorization': f'Bearer {token}'})
        else:
            raise ValueError("Token is not available. Please ensure the user is registered and token is set.")

    def get(self, url, params=None):
        """
        Wrapper for GET requests to automatically attach the Authorization token.
        """
        response = self.session.get(url, params=params)
        return response

    def post(self, url, data=None, json=None, files=None):
        """
        Wrapper for POST requests to automatically attach the Authorization token.
        """
        response = self.session.post(url, data=data, json=json, files=files)
        return response

    def put(self, url, data=None, json=None):
        """
        Wrapper for PUT requests to automatically attach the Authorization token.
        """
        response = self.session.put(url, data=data, json=json)
        return response

    def delete(self, url, params=None):
        """
        Wrapper for DELETE requests to automatically attach the Authorization token.
        """
        response = self.session.delete(url, params=params)
        return response
    def patch(self, url, data=None, json=None):
        """
        Wrapper for PATCH requests to automatically attach the Authorization token.
        """
        response = self.session.patch(url, data=data, json=json)
        return response
