import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

doc_url = "DOC_URL"

house_url = "https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(url=house_url)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
house_tag_list = soup.find_all(name="div", class_="StyledPropertyCardDataWrapper")
#print(house_tag)
house_address_list = []
house_price_list = []
house_link_list = []
i=0
for house_tag in house_tag_list:
    house_link = house_tag.find(name="a", class_="StyledPropertyCardDataArea-anchor")
    house_address = house_tag.find(name="address").getText().strip()
    house_price = house_tag.find(name="span")
    house_price = house_price.getText().split('/')[0].split('+')[0]
    #print(house_link.get("href"))
    #print(house_address)
    #print(house_price)
    house_address_list.append(house_address)
    house_link_list.append(house_link.get("href"))
    house_price_list.append(house_price)
    i += 1
    #print("++++++++++++++++", i)
print(len(house_address_list))
print(len(house_link_list))
print(len(house_price_list))


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


print(driver.title)
time.sleep(3)
for i in range(len(house_link_list)):
    driver.get(url=doc_url)
    address_field = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_field = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_field = driver.find_element(By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address_field.send_keys(house_address_list[i])
    price_field.send_keys(house_price_list[i])
    link_field.send_keys(house_link_list[i])
    submit_button.click()
    time.sleep(1)
