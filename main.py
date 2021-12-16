from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\satven\\chromedriver\\chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get(
    "https://www.amazon.in/Logitech-Multi-Device-Bluetooth-Keyboard-Black/dp/B00MUTWLW4/ref=sr_1_5?keywords=keyboard+for+ipad+air+4&qid=1638032643&s=computers&sr=1-5")

price = driver.find_element(By.ID,"priceblock_ourprice")
print(price.text)

form = driver.find_element(By.NAME,"field-keywords")
print(form.get_attribute("value"))

print(driver.find_element(By.CSS_SELECTOR,"._p13n-desktop-sims-fbt_fbt-desktop_item-details-per-asin__3DtF1 a").get_attribute("href"))

print(driver.find_element(By.XPATH,'//*[@id="nav-logo-sprites"]/span[1]').tag_name)



driver.close()
