from bs4 import BeautifulSoup
import requests

#url = "https://news.ycombinator.com/"
url = "https://news.ycombinator.com/news"

response = requests.get(url=url)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_text = []
article_link =[]


for span_tag in articles:
    anchor_tag = span_tag.find("a")
    link = anchor_tag.get("href")
    text = anchor_tag.getText()
    article_link.append(link)
    article_text.append(text)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",  class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(article_text[largest_index])
print(article_link[largest_index])
print(article_upvotes[largest_index])

#print(articles)
#print(article_link)
#print(article_text)
#print(article_upvotes)
print(len(articles), len(article_upvotes))