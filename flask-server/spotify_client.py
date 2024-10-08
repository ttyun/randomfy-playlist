import random
import string
import requests
import urllib
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect

class SpotifyClient(object):
   def __init__(self, auth_token):
      self.auth_token = auth_token
   
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
   def get_random_tracks(self, limit, genre_type):
      wildcard = f"%{random.choice(string.ascii_lowercase)}%"
      if genre_type and genre_type != 'any':
         genre_q = f"genre: {genre_type}"
         wildcard += f" {genre_q}"
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
      url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
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
      
