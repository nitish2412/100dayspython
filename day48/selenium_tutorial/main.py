from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
url = "https://www.amazon.in/electric-Kettle-Double-Triple-Protection/dp/B0B2CZTCL2/ref=sr_1_1_sspa?crid=26TLRNW215NLE&keywords=electric+kettle&qid=1707365344&sprefix=kattle%2Caps%2C199&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
#driver.get(url=url)
driver.get("https://www.python.org")
print(driver.title)

#price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#print(f"This price is: {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
#print(search_bar)
#print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)
print(button.text)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


# extracting upcoming event from python.org
def upcoming_event(driver):
    events_list = driver.find_elements(By.CLASS_NAME, value="shrubbery")
    events = events_list[1].find_elements(By.TAG_NAME, "li")
    print(len(events))
    event_dict = {}
    c = 0
    for event in events:
        temp = {}
        time_obj = event.find_element(By.TAG_NAME, value="time")
        event_name = event.find_element(By.TAG_NAME, value="a")
        time = time_obj.get_attribute("datetime")
        date = time.split("T")[0]
        event_name = event_name.text
        print(date)
        print(event_name)
        temp["time"] = date
        temp["name"] = event_name
        event_dict[c] = temp
        c += 1
        print("++++++++++++++++++++++++")
    return event_dict


event_dict = upcoming_event(driver)
print(event_dict)
#print(len(events_list), events_list[1].text)


def upcoming_events(driver):
    event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
    event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
    event_dict = dict()
    c = 0
    for i in range(0, len(event_names)):
        event_dict[i] = {
            "time": event_times[i].text,
            "name": event_names[i].text
        }

    print(event_dict)


print(upcoming_events(driver))
#driver.close()
driver.quit()