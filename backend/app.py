import os
import spotipy
from flask import Flask, request, url_for, session, redirect
from spotify_client import SpotifyClient

app = Flask(__name__)
# app.secret_key = 'ASD27DWT312GJKD'
# app.config['SESSION_COOKIE_NAME'] = 'Ty Cookie Session'
AUTH_TOKEN_INFO = "auth_token_info"

@app.route('/')
def login():
   oauth = SpotifyClient.create_spotify_oauth()
   auth_url = oauth.get_authorize_url()
   print(auth_url)
   return redirect(auth_url)

@app.route('/redirect')
def redirectApplication():
   oauth = SpotifyClient.create_spotify_oauth()
   # session.clear()
   auth_code = request.args.get('code')
   auth_token_info = oauth.get_access_token(auth_code)
   # session[AUTH_TOKEN_INFO] = auth_token_info
   return redirect(url_for('processPlaylist', _external=True))

@app.route('/playlists')
def processPlaylist():
   #generatePlaylist()
   return 'Some Drake songs'


def generatePlaylist():
   playlist_name = 'AUTOPLAY'
   description = 'Automatically generated playlist. Check for new songs you may like.'
   isPublic = True

   # Get auth token
   auth_token = SpotifyClient.get_auth_token()

   # Create spotify client
   spotify_client = SpotifyClient(auth_token)
   
   # Collect random list of top edm songs
   random_edm_tracks = spotify_client.get_random_tracks(20)
   
   # Collect random list of top rap songs
   random_rap_tracks = spotify_client.get_random_tracks(20)

   # Collect random list of album songs
   #random_album_tracks = spotify_client.get_random_tracks_from_album('Whole Lotta Red')
   random_album_tracks = []

   # Combine these two lists together randomly
   playlist_tracks = random_edm_tracks + random_rap_tracks + random_album_tracks
   playlist_track_uris = ''
   for track in playlist_tracks:
      playlist_track_uris += (track['uri'] + ',')
   playlist_track_uris = playlist_track_uris[:-1]
   
   # Add combined tracks into Spotify playlist
   was_added = spotify_client.add_tracks_to_playlist(playlist_track_uris,
         playlist_name, description, isPublic)
   if was_added:
      for track in playlist_tracks:
         print(f"Added track: {track['name']}")

if __name__ == '__main__':
   app.run(port=5000, debug=True)
   #generatePlaylist()
