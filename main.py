from bs4 import BeautifulSoup
import requests
import lxml
import re

# url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# response = requests.get(url)
# with open('file.txt', 'w') as file:
#     file.write(response.text)

with open('file.txt', 'r') as file:
    web_site = file.read()

soup = BeautifulSoup(web_site, "lxml")
movies = soup.find(class_="gallery").find_all(class_="title")

list_of_movies = []
for movie in movies:
    list_of_movies.append(movie.text)

best_movies = list_of_movies[::-1]
for movie in best_movies:
    print(movie)
 
# for movie in best_movies:
#     with open('movies.txt', 'a') as file:
#         file.write(movie + '\n')
