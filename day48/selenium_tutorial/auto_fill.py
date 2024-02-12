from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = "http://secure-retreat-92358.herokuapp.com/"


driver.get(url=url)
print(driver.title)

f_name = driver.find_element(By.NAME,value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
f_name.send_keys("dhkjshkh")
l_name.send_keys("ltuyue")
email.send_keys("dhkjshkh@gmail.com",)

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()


#driver.quit()