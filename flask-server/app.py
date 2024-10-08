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
   genres = request.args.getlist('genres[]')
   genre_types = []
   for genre in genres:
      genre_types.append(genre)
   print(genre_types)
   added_track_names = generatePlaylist(access_token, genre_types)
   return jsonify(added_tracks=added_track_names)

def generatePlaylist(access_token, genre_types):
   playlist_name = 'AUTOPLAY'
   description = 'Automatically generated playlist. Check for new songs you may like.'
   isPublic = True

   # Create spotify client
   spotify_client = SpotifyClient(access_token)
   
   # Collect random list songs
   if not genre_types:
      playlist_tracks = spotify_client.get_random_tracks(10, None)
   elif len(genre_types) <= 1:
      playlist_tracks = spotify_client.get_random_tracks(10, genre_types[0])
   else:
      playlist_tracks = spotify_client.get_random_tracks(5, genre_types[0])
      playlist_tracks += spotify_client.get_random_tracks(5, genre_types[1])

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
