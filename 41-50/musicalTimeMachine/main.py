from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=billboard_url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

# Spotify Authentication
try:
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="https://example.com/",
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt",
        )
    )
    user_id = sp.current_user()["id"]
    print(f"User ID: {user_id}")
except spotipy.exceptions.SpotifyException as e:
    print(f"Spotify authentication failed: {e}")
    exit()

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify search failed: {e}")
        continue

# Creating a new private playlist in Spotify
try:
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    print(playlist)
except spotipy.exceptions.SpotifyException as e:
    print(f"Failed to create playlist: {e}")
    exit()

# Adding songs found into the new playlist
try:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
except spotipy.exceptions.SpotifyException as e:
    print(f"Failed to add items to playlist: {e}")