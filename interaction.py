from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("C:\\Users\\satven\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page")


# readers_count = driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
#
# print(readers_count.text)

username = driver.find_element(By.NAME,"wpName")
username.send_keys("username")

password = driver.find_element(By.NAME,"wpPassword")
password.send_keys("password")

submit = driver.find_element(By.CSS_SELECTOR,"div button")
submit.click()