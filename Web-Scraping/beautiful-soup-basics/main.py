from bs4 import BeautifulSoup


def print_data(tag: str, data):
    print(tag + " : " + str(data))


with open("website.html") as website_file:
    website_content = website_file.read()

soup = BeautifulSoup(website_content, "html.parser")

print()
title = soup.title
print_data("title", title)
print_data("find", soup.find(name="h1", id="name"))
print_data("find_all", soup.find_all(name="h3"))
print_data("select", soup.select("#name"))
print_data("select_one", soup.select_one(".heading").get_text())
print_data("attr", soup.select_one("h3").attrs)
