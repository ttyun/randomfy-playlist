import os
import spotipy
from flask import Flask, request, url_for, session, redirect, jsonify
from flask_cors import CORS, cross_origin # Good to know in the future
from spotify_client import SpotifyClient

app = Flask(__name__)
CORS(app)

# *** Could add resources to above CORS constructor ***
# cors_config = {
#    "origins": ["http://localhost:3000/"],
#    "methods": ["OPTIONS", "GET"],
#    "allow_headers": ["Authorization"]
# }

# app.secret_key = 'ASD27DWT312GJKD'
# app.config['SESSION_COOKIE_NAME'] = 'Ty Cookie Session'

@app.route('/', methods=['GET'])
def login():
   oauth = SpotifyClient.create_spotify_oauth()
   auth_url = oauth.get_authorize_url()
   print(auth_url)
   return redirect(auth_url)

@app.route('/redirect', methods=['GET'])
def redirectApplication():
   oauth = SpotifyClient.create_spotify_oauth()
   # session.clear()
   auth_code = request.args.get('code')
   auth_token_info = oauth.get_access_token(auth_code)
   print(auth_token_info)
   # session[AUTH_TOKEN_INFO] = auth_token_info
   return redirect(url_for('processPlaylist', _external=True))

@app.route('/playlists', methods=['GET'])
def processPlaylist():
   added_track_names = generatePlaylist()
   return jsonify(added_tracks=added_track_names)


def generatePlaylist():
   playlist_name = 'AUTOPLAY'
   description = 'Automatically generated playlist. Check for new songs you may like.'
   isPublic = True

   # Get auth token
   auth_token = SpotifyClient.get_auth_token()

   # Create spotify client
   spotify_client = SpotifyClient(auth_token)
   
   # Collect random list of top edm songs
   random_edm_tracks = spotify_client.get_random_tracks(5)
   
   # Collect random list of top rap songs
   random_rap_tracks = spotify_client.get_random_tracks(5)

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
   added_track_names = []
   if was_added:
      for track in playlist_tracks:
         print(f"Added track: {track['name']}")
         added_track_names.append(track['name'])
   return added_track_names

if __name__ == '__main__':
   app.run(debug=True, port=5000)
