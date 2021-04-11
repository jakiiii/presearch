#   Copyright (c) 2021.
#   Version : 0.0.1
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8

# This is Masud Rana, Does the task like this?

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

# TODO: 3 Make a Long List of keyword
all_keys = ["username", "password", "country", "income", "funny"]

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")

try:
    driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
except:
    driver = webdriver.Chrome()

chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds
# What will be searched

actions = ActionChains(driver)

# Time waiting for page
waiting_for_page = 10

driver.get("https://engine.presearch.org")
time.sleep(2)

# TODO: 2 Make a login strong system in environment veriable
print(input("Enter your Username and Password Menually then enter 1: "))
driver.get("https://presearch.org")
# print(input("Enter your Username and Password Menually then enter 1: "))
driver.find_element_by_id("search").send_keys(random.choice(all_keys))
driver.find_element_by_id("search").send_keys(Keys.ENTER)
# print(input("Enter your Username and Password Menually then enter 1: "))
time.sleep(2)

actions.send_keys(Keys.TAB * 10)
search_key = random.choice(all_keys)
actions.send_keys(search_key)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(20)
prev_search_key = search_key

while True:
    for i in range(len(prev_search_key)):
        actions.send_keys(Keys.BACK_SPACE)

    time.sleep(4)
    search_key = random.choice(all_keys)
    print(search_key)
    actions.send_keys(search_key)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    prev_search_key = search_key
    time.sleep(4)

    # Scrolling few times
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(random.randint(3, 5))
    driver.execute_script("window.scrollBy(0, -800);")
    time.sleep(random.randint(3, 5))

    # TODO: 1 Click the search request to make it more human
    tab = actions.send_keys(Keys.TAB * random.randint(15, 35))
    tab.perform()
    new = tab.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.ENTER)
    new.perform()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(random.randint(5, 10))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(random.randint(5, 35))


# driver.find_element_by_id("token-animation").click()
# print(driver.find_element_by_xpath("//button[@type='submit']"))
# driver.find_element_by_xpath("//input[@type='submit']").click();
# print(input("Enter your Username and Password Menually then enter 1: "))

# driver.execute_script("window.open('https://engine.presearch.org');")
# driver.close()
# driver.get("https://presearch.org")
# driver.find_element_by_id("search").send_keys("username")
# driver.find_element_by_id("search").send_keys(Keys.ENTER)

time.sleep(5)

# driver.quit()
