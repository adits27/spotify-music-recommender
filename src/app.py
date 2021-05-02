import json
import dotenv
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from dotenv import load_dotenv
import os
from os.path import join, dirname
from pathlib import Path

try:
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
except FileNotFoundError as fileError:
    print("Could not find file ", fileError)
except ValueError as valueError:
    print("Error while loading the .env files ", valueError)


clientID = os.environ.get('CLIENT_ID')
clientSecret = os.environ.get('CLIENT_SECRET')
username = os.environ.get('USERNAME')
scope = os.environ.get('SCOPE')
redirectURI = os.environ.get('REDIRECT_URI')

clientCredentialsManager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
spotify = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)

token = util.prompt_for_user_token(username, scope, clientID, clientSecret, redirectURI)

try:
    spotify = spotipy.Spotify(auth=token)
except ValueError as error:
    print("Could not get token for ID ", username)

reco = spotify.recommendations(seed_artists=["enter something here"], seed_genres=["enter something here"], seed_tracks=["enter something here"], limit='enter something here')
apiResponse = []

for track in reco["tracks"]:
    recommendations = {
        "Title": track['album']['name'],
        "Artist": track['album']['artists'][0]['name'],
        "Album Art": track['album']['images'][0]['url']
    }

    apiResponse.append(recommendations)

print("Recommendations from the Spotify API - ", apiResponse)