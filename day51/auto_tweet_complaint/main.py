from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

from internetspeed import InternetSpeedTwitterBot


PROMISED_DOWN = 150
PROMISED_UP = 50
CHROME_DRIVER_PATH = ""
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

bot = InternetSpeedTwitterBot(chrome_options)
print(bot.up)
print(bot.down)
#bot.get_internet_speed()
bot.tweet_at_provider()

#bot.driver.quit()