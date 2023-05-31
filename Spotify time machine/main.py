from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


date = input("Which year would like to travel to? Type date in YYYY-MM-DD format: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
billboard_html = response.text

soup = BeautifulSoup(billboard_html, 'html.parser')

top_100 = soup.select(".o-chart-results-list-row-container li h3")
top_100_song_names = [song.getText().strip() for song in top_100]

Client_ID = "ee6e2e6bf8cb4a80a784ad233d4e2292"
Client_secret = "feae9711e8a64d97aaedccb85e1680cf"

sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyOAuth(
        client_id=Client_ID,
        client_secret=Client_secret,
        redirect_uri="http://localhost:8888/callback",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]

for song in top_100_song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

new_playlist = sp.user_playlist_create(user=user_id, public=False, name=f"{date} Billboard 100")

sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)