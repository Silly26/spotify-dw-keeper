# Spotify Discover Weekly Keeper

This script will allow you to add all of your (temporary) Discover Weekly tracks into a permanent playlist. It uses the [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) library to make use of the Spotify API. 
You will need to edit `values.py` with your own information for this script to work. 


# Usage

This script will require [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) and Python to be installed. After Python is installed, from the command line, you can run: 
```pip install spotipy```

Once this has installed, you will need to visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and set up a new App:
    
    - Select "Create App" on the front page of the dashboard.
    - This can be named whatever you want, e.g. DiscoverWeekly
    - Write a brief description, e.g. "This script is used to automate my Discover Weekly"
    - Website can be left blank.
    - For the Redirect URI, you can specify it as localhost. (http://localhost:8000/callback is used already in values.py if you want to copy/paste)

After the app has been created in your Spotify Developer Dashboard, we will need to input our values in `values.py`:

    - From the dashboard, select your newly created app name
    - From here, we will need to copy and paste our Client ID and Client Secret. 
    - The client ID and secret can be found in the first box, with the secret being hidden by default. 
    - You can select "view client secret" under the client ID to reveal this. Do not provide this secret ID to anyone else!

Now that you have copied your values into `values.py`, you will need to make a decision on how you'd like to proceed. 
Discover Weekly Keeper has two functions: 

    Collective playlist - This will let the script take all of the current songs and append it to a single playlist. 
    Create new playlist - This allows the script to create new playlists with a date code appended (e.g. Discover Weekly - June-28-2023)

Depending on which mode you choose, you will need to either uncomment or input one final value. 

# Running on "Collective playlist" mode

To add all of your songs into one giant playlist, you will need to create a new playlist from Spotify itself. This can be named whatever you like. After you have created your playlist, select `Share > Copy link to playlist`
After you have your playlist link copied, you will need to copy the string after /playlists/ (only use the first characters before the ?)

For example, we'd use `https://open.spotify.com/playlist/37i9dQZF1DZ06evO05tE88?si=d921512c62bc464c` selecting the `37i9dQZF1DZ06evO05tE88` before `?si=`
Use this value to input into `values.py` under `playlist_id`.
Run the script! It should open a browser window for Spotify which will allow you to authorize it to run. The permissions needed are set in the `scope` variable of `main.py`.

# Running on "Create new playlist" mode

For creating a new playlist for each time the script is run, you will need to comment the `create_playlist` function AND uncomment `create_new_playlist`. This does not require any specific playlist IDs, as it will generate new ones. By default, these playlists will be set to Public. If you would like to make them Private on creation, change `public=True` to `public=False` on line 40 of `main.py`.