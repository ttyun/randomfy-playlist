import random
import string
import requests
import urllib
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect
from spotify_credentials import refresh_token, encoded_spotify_client_id, client_id, client_secret, spotify_user_id

class SpotifyClient(object):
   def __init__(self, auth_token):
      self.auth_token = auth_token
   
   # Use refresh token to grab auth token
   @staticmethod
   def get_auth_token():
      url = "https://accounts.spotify.com/api/token"
      response = requests.post(
         url,
         headers={
            "Authorization": f"Basic {encoded_spotify_client_id}"
         },
         data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id
         }
      )
      response_json = response.json()
      return response_json["access_token"]

   @staticmethod
   def create_spotify_oauth():
      return SpotifyOAuth(
         client_id=client_id,
         client_secret=client_secret,
         redirect_uri=url_for('redirectApplication', _external=True)
         #scope='playlist-modify-public,playlist-read-public,user-library-read'
      )
   
   # Spotify Client - Search for Tracks
   def spotify_search_tracks(self, query, offset, limit):
      url = f"https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track&limit={limit}"
      response = requests.get(
         url,
         headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
         }
      )
      print(f'{url}={response}')
      response_json = response.json()
      tracks = [track for track in response_json['tracks']['items']]
      print(f'Found {len(tracks)} from your search.')
      return tracks
   
   # Get random tracks
   def get_random_tracks(self, limit):
      wildcard = f"%{random.choice(string.ascii_lowercase)}%"
      query = urllib.parse.quote(wildcard)
      offset = random.randint(0, 1000)

      return self.spotify_search_tracks(query, offset, limit)
   
   # Create a new playlist for the user and add specified tracks
   def add_tracks_to_playlist(self, track_uris, playlist_name, description, isPublic):
      # Get current user's profile
      url = 'https://api.spotify.com/v1/me'
      response = requests.get(
         url,
         headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
         }
      )
      response_json = response.json()
      user_id = response_json['id']

      # Create a playlist for user
      url = f'https://api.spotify.com/v1/users/{spotify_user_id}/playlists'
      response = requests.post(
         url,
         headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
         },
         json={
            "name": playlist_name,
            "description": description,
            "public": "true" if isPublic else "false" 
         }
      )
      response_json = response.json()
      if response.ok:
         print(f'Created new playlist: {playlist_name}')

      # Add tracks into created playlist
      playlist_id = response_json['id']
      url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={track_uris}'
      response = requests.post(
         url,
         headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
         }
      )
      return response.ok
   
   # Grab random tracks from an album name (case insensitive)
   # def get_random_tracks_from_album(self, album_name):
   #    wildcard = f"%{random.choice(string.ascii_lowercase)}%"
   #    offset = random.randint(0, 2000)
   #    query = urllib.parse.quote(wildcard)
   #    query += f'%20album:{album_name}'
   #    print(f'Query:{query}')
   #    print(f'Grabbing the random tracks for album: {album_name}')

   #    return self.spotify_search_tracks(query, offset)
      
