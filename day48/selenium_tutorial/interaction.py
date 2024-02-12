from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
print(driver.title)

articles_div = driver.find_element(By.ID, value="articlecount")
article_tag= articles_div.find_element(By.TAG_NAME, "a")
article_count = article_tag.text
print(article_count)

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")  # #is used for id
print(article_count.text)
#article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()

search = driver.find_element(By.NAME, value="search")
#search.send_keys("python")
search.send_keys("python", Keys.ENTER)

driver.quit()