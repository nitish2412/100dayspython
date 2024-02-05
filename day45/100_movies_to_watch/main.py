import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")
movies_list = soup.find_all(name="h3", class_="title")
i=len(movies_list)-1
with open("movies.txt", "w") as fp:
    while i >= 0:
        print(movies_list[i].text)
        fp.write(movies_list[i].text+"\n")
        i -= 1


