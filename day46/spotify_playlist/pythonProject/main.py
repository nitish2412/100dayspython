from bs4 import BeautifulSoup
import requests

CLIENT_ID = "f46662b2e7fe4825bb7d0d8bafdf7a54"
CLIENT_SECRET="6e6a3675e63e4e4bb2aabc3e06d9190e"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = "https://www.billboard.com/charts/hot-100/"+date

response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
#print(len(song_names))
#print(song_names)


soup = BeautifulSoup(response.text, "html.parser")
header_tag = soup.find_all(name="h3", class_="c-title")
#print(header_tag[0].text.strip())
#print(len(header_tag))
song_list = []
c = 1
for i in range(6, len(header_tag)):
    title = header_tag[i].text.strip()
    if title[len(title)-1] != ':' and c <= 100:
        #print(c, title)
        song_list.append(title)
        c +=1
print(song_names)
print(song_list)


