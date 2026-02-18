import json
import requests
from requests.exceptions import HTTPError

class KeycloakAuth:
    def __init__(self, server_url, realm, client_id, client_secret):
        self.server_url = server_url
        self.realm = realm
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

    def get_token(self, username, password):
        url = f'{self.server_url}/auth/realms/{self.realm}/protocol/openid-connect/token'
        payload = { 'grant_type': 'password', 'client_id': self.client_id, 'client_secret': self.client_secret, 'username': username, 'password': password }

        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()  # Raise an error for HTTP errors
            self.token = response.json()['access_token']  # Save the access token
            return self.token
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return None

    def validate_token(self):
        if not self.token:
            print('No token to validate.')
            return False

        url = f'{self.server_url}/auth/realms/{self.realm}/protocol/openid-connect/userinfo'
        headers = { 'Authorization': f'Bearer {self.token}' }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()  # Return user information if token is valid
        except HTTPError as http_err:
            print(f'HTTP error when validating token: {http_err}')
        except Exception as err:
            print(f'Other error occurred during token validation: {err}')
        return None

# Example of using the KeycloakAuth class
# keycloak_auth = KeycloakAuth('http://localhost:8080', 'myrealm', 'myclient', 'mysecret')
# token = keycloak_auth.get_token('user', 'password')
# if token:
#     user_info = keycloak_auth.validate_token()  
#     print(user_info)  
