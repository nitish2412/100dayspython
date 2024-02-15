from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL_ID = ""
Password = ""

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.linkedin.com/jobs/search/?alertAction=viewjobs&currentJobId=3750251927&origin=JOBS_HOME_JOB_ALERTS&savedSearchId=1736134074"
driver.get(url=url)
print(driver.title)


#time.sleep(2)
#sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
#sign_in_button.click()


password_field = driver.find_element(by=By.ID, value="password")

# email = driver.find_element(By.NAME, value="session_key")
email = driver.find_element(by=By.ID, value="username")
# password = driver.find_element(By.NAME, value="session_password")
password = driver.find_element(by=By.ID, value="password")

#button = driver.find_element(By.CLASS_NAME, value="login__form_action_container")

email.send_keys(EMAIL_ID)
password.send_keys(Password)
password.send_keys(Keys.ENTER)
#button.click()
time.sleep(5)
#save_button = driver.find_element(By.CLASS_NAME, value="artdeco-button__text")
#save_button.click()

#apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
#apply_button.click()

# saving job link
save_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
save_button.click()