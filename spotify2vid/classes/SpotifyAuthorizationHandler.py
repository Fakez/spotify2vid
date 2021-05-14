import requests
import json
from .EnvVarsHandler import EnvVarsHandler

class SpotifyAuthorizationHandler():

    def __init__(self):
        self.env_vars_handler = EnvVarsHandler()
        self.client_id = self.env_vars_handler.get_env_var('SPOTIFY_CLIENT_ID')
        self.client_secret = self.env_vars_handler.get_env_var('SPOTIFY_CLIENT_SECRET')

    def refreshToken(self):
        url = 'https://accounts.spotify.com/api/token'
        params = {
                'grant_type': 'refresh_token',
                "refresh_token": self.env_vars_handler.get_env_var('SPOTIFY_REFRESH_TOKEN'),
                'client_id': self.client_id,
                'client_secret': self.client_secret,
        }

        response = requests.post(url, data=params)
        responseJson = json.loads(response.text)
        #print(responseJson)
        access_token = responseJson['access_token']
        return access_token