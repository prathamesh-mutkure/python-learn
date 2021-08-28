from bs4 import BeautifulSoup, Tag
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

article_tags = soup.select(".storylink")
articles = []

for article_tag in article_tags:
    article = {
        "title": article_tag.get_text(),
        "link": article_tag.get("href"),
    }

    articles.append(article)

scores = [int(score.get_text().split()[0]) for score in soup.select(".score")]

max_score = max(scores)
max_index = scores.index(max_score)
max_article = articles[max_index]

print(max_article["title"])
print(max_article["link"])
print(max_score)
