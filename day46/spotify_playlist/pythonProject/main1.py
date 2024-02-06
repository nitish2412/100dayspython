from bs4 import BeautifulSoup
import requests

#date = input("Please choose a date:")
#date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

#url = "https://www.billboard.com/charts/hot-100/2000-08-12"
url = "https://www.billboard.com/charts/hot-100/2024-01-07/"

response = requests.get(url=url)
web_data = response.text

soup = BeautifulSoup(web_data, "html.parser")
header_tag = soup.find_all(name="h3", class_="c-title")
print(header_tag[0].text.strip())
print(len(header_tag))
song_list = []
c = 1
for i in range(6, len(header_tag)):
    title = header_tag[i].text.strip()
    if title[len(title)-1] != ':' and c <= 100:
        print(c, title)
        song_list.append(title)
        c +=1
print(song_list)

