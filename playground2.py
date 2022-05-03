from bs4 import BeautifulSoup
from urllib.request import urlopen
import lxml
import requests
import re


response = (requests.get("https://news.ycombinator.com/")).text
soup = BeautifulSoup(response, "lxml")


news = soup.find_all(class_="score")
list_points = []

for item in news:
    # print(item)
    points = item.text.split()
    list_points.append(int(points[0]))

max_points = max(list_points)
# print(max_points)

for item in news:
    points = item.text.split()
    if max_points == int(points[0]):
        max_rated = item["id"]

max_rated_id = re.findall(r'\d+', max_rated)
max_rated_news = int(max_rated_id[0])

rated_news = soup.find(id=f"{max_rated_news}")

titlelink_news = rated_news.find(class_="titlelink")
news_title = titlelink_news.text
news_url = titlelink_news["href"]

print(news_title)
print(news_url)


