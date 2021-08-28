from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"
sp_oauth = SpotifyOAuth(scope=scope, cache_path="token.txt")
sp = spotipy.Spotify(auth_manager=sp_oauth)
user_id = sp.current_user()["id"]


date = input("Which year do you want to travel to? (YYYY-MM-DD): ")

if date == "":
    date = "2017-08-21"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_titles = [title_tag.get_text() for title_tag in soup.select("span.chart-element__information__song")]
year = date.split("-", 3)[0]
uri_list = []

for song in song_titles[:10]:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{song} not found")
    else:
        uri_list.append(uri)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)
