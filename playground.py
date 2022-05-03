from bs4 import BeautifulSoup
import lxml

# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "lxml")

# list_li = soup.find_all("li")
#
# for item in list_li:
#     print(item.text)

# list_href = soup.find_all("a", href=True)
# for item in list_href:
#     print(item["href"])
#     print(item.get("href"))

# find_by_id = soup.find(name="h1", id="name")
# print(find_by_id.text)

# find_by_class = soup.find(name="h3", class_="heading")
# print(find_by_class.text)

# company_url = soup.select_one("p a")
# print(company_url["href"])

# name_url = soup.select_one("#name") #for ID search
# print(name_url.text)

# heading_url = soup.select_one(".heading") # for class search
# print(heading_url.text)
