import os

from spotify_client import SpotifyClient

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
   generatePlaylist()
