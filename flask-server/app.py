from flask import Flask, request, jsonify
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

@app.route('/playlists', methods=['GET'])
def processPlaylist():
   access_token = request.headers.get('Authorization')
   added_track_names = generatePlaylist(access_token)
   return jsonify(added_tracks=added_track_names)

def generatePlaylist(access_token):
   playlist_name = 'AUTOPLAY'
   description = 'Automatically generated playlist. Check for new songs you may like.'
   isPublic = True

   # Create spotify client
   spotify_client = SpotifyClient(access_token)
   
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
   added_songs = []
   
   if was_added:
      for track in playlist_tracks:
         added_song = {}
         added_song['name'] = track['name']
         artists = ''
         for artist in track['artists']:
            artists += artist['name'] + ', '
         added_song['artist'] = artists[:-2]
         added_song['album'] = track['album']['name']
         added_songs.append(added_song)
         print(f"Added track: {added_song['name']}")

   return added_songs

if __name__ == '__main__':
   app.run(debug=True, port=5000)
