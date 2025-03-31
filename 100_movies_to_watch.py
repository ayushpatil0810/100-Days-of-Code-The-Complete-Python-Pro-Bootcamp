import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


website = requests.get(URL)
website_html = website.text

soup = BeautifulSoup(website_html, "html.parser")

tags = soup.find_all(name="h3", class_="title")

movies = []
for tag in tags:
    movie_name = tag.getText()
    movies.insert(0, movie_name + "\n")

with open("movies.txt", "w", encoding="utf-8") as file:
    file.writelines(movies)

