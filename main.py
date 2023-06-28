import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
import values

# Set required scope and permissions for script
scope = "playlist-modify-public playlist-read-private playlist-modify-private"

# Set up Spotipy authentication
# Make sure to input your values in config.py
auth_manager = SpotifyOAuth(
    scope=scope,
    client_id=values.client_id,
    client_secret=values.client_secret,
    redirect_uri=values.redirect_uri
)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_discover_weekly():
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if playlist['name'] == 'Discover Weekly':
            return playlist['id']
    print("Discover Weekly playlist not found.")
    return None


def fetch_user_playlists():
    playlists = sp.current_user_playlists()
    print("Your playlists:")
    for playlist in playlists['items']:
        print(f" - {playlist['name']} (ID: {playlist['id']})")

# This function is for creating separate playlists for each week, with a date code appended 

def create_new_playlist():
    today = datetime.date.today()
    playlist_name = f"Discover Weekly - {today.strftime('%m-%d-%Y')}"
# Change public=True to False if you'd like to change visibility of the generated playlist
    sp.user_playlist_create(user=sp.current_user()['id'], name=playlist_name, public=True)
    playlist_id = sp.current_user_playlists(limit=1)['items'][0]['id']
    discover_weekly_id = get_discover_weekly()
    if discover_weekly_id:
        tracks = sp.playlist_items(discover_weekly_id)['items']
        track_uris = [track['track']['uri'] for track in tracks]
        sp.playlist_add_items(playlist_id, track_uris)
        print(f"Added {len(track_uris)} tracks to the playlist.")
    else:
        print("Unable to retrieve Discover Weekly playlist.")


def create_playlist():
    playlist_id = values.playlist_id
    tracks = sp.playlist_items(get_discover_weekly())['items']
    track_uris = [track['track']['uri'] for track in tracks]
    sp.playlist_add_items(playlist_id, track_uris)
    print(f"Added {len(track_uris)} tracks to the playlist.")

# Add a # to the line below, and uncomment the next function if you want to switch between "modes". 
create_playlist()

# Uncomment this line if you'd like to run in "create new playlist" mode.
#create_new_playlist()

# Uncomment the line below to fetch the IDs of your existing playlists. This can help identify which ID you need for values.py
#fetch_user_playlists()