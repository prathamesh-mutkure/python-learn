from bs4 import BeautifulSoup
import requests

# response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# response.raise_for_status()

with open("100_movies_site.html") as file:
    web_content = file.read()

soup = BeautifulSoup(web_content, "html.parser")

movie_tags = soup.select(".listicle-item h3.jsx-4245974604")
movie_names = [movie_tag.get_text() + "\n" for movie_tag in movie_tags]
movie_names.reverse()

movie_names[0] = "1) " + movie_names[0]

with open("100_movies_list", "w") as file:
    file.writelines(movie_names)
