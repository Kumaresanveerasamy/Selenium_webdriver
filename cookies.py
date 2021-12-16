from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# starting selenium services:
s = Service("C:\\Users\\satven\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

button = driver.find_element(By.ID, "cookie")

# getting items from the menu :
products = driver.find_elements(By.CSS_SELECTOR, "#store div")
product_ids = [product.get_attribute("id") for product in products]

# defining timeouts:
five_sec_timeout = time.time() + 5
five_min_timeout = time.time() + 300

while True:
    button.click()

    # after 5 seconds :
    if time.time() > five_sec_timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        product_prices = []

        # getting item prices :
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                product_prices.append(cost)

        # items and their prices:
        cookies_upgrades = {product_prices[n]: product_ids[n] for n in range(len(product_prices))}

        # getting current cookies count:
        money = driver.find_element(By.ID,"money").text

        if "," in money:
            money = money.replace(",","")
        cookies_count = int(money)

        # finding Upgrades we can buy:
        affordable_upgrades = {cost: id for cost,id in cookies_upgrades.items() if cookies_count > cost}

        # purchasing the expensive upgrades:

        expensive_product_price = max(affordable_upgrades)
        expensive_product_id = affordable_upgrades[expensive_product_price]

        expensive_product_element = driver.find_element(By.ID,expensive_product_id)
        expensive_product_element.click()

        five_sec_timeout = time.time() + 5

        # checking for five minutes:
        if time.time() > five_min_timeout:
            cookies_per_sec = driver.find_element(By.ID,"cps")
            print(cookies_per_sec)
            break



