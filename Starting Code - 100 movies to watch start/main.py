import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
web_html = response.text

soup = BeautifulSoup(web_html, 'html.parser')
movies = soup.select(".article-title-description__text .title")
titles = [movie.getText() for movie in movies]
titles.reverse()

with open("movies.txt", "w") as file:
    for title in titles:
        file.write(f"{title}\n")



