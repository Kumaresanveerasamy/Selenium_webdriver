from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\satven\\chromedriver\\chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")

datelist = [date.text for date in driver.find_elements(By.CSS_SELECTOR, ".event-widget ul time")]
event_list = [event.text for event in driver.find_elements(By.CSS_SELECTOR, ".event-widget ul a")]

event_details = {i: {'date': datelist[i], 'event': event_list[i]} for i in range(len(datelist))}
print(event_details)

driver.close()
