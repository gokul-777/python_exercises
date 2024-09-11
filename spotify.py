import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Step 1: Set up credentials
client_id = '4baee96852ae4f0eb85d7b3585582290'
client_secret = 'd3e9dce28e6d4a6391b506b21f720762'
redirect_uri = 'https://ubiquitous-space-tribble-q7965w7xpw9vc64j9-8080.app.github.dev/'  # Or any other redirect URI you specified

# Step 2: Authenticate using OAuth (User-specific)
scope = 'user-library-read user-top-read user-read-recently-played playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))


# Get recently played tracks
recent_tracks = sp.current_user_recently_played(limit=50)

# Create a list to store the track data
track_data = []

# Loop through the recently played tracks
for item in recent_tracks['items']:
    track = item['track']
    track_data.append({
        'Track Name': track['name'],
        'Artists': ', '.join([artist['name'] for artist in track['artists']]),
        'Album': track['album']['name'],
        'Played At': item['played_at']
    })

# Create a DataFrame from the list
df = pd.DataFrame(track_data)

# Display the DataFrame
df.to_excel('spotify_mg.xlsx',index=False)
