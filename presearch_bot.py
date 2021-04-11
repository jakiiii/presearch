from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# TODO: Make a Long List of keyword
all_keys = ["american legends", "income", "funny videos", "python for kids"]


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://engine.presearch.org")
print(input("Enter your Username and Password Menually then enter 1: "))

search_query = driver.find_element_by_name('q')
search_query.send_keys(random.choice(all_keys))
search_query.send_keys(Keys.RETURN)

sleep(5)
driver.execute_script("window.scrollBy(0, 800);")
sleep(3)
driver.execute_script("window.scrollBy(0, -750);")
sleep(2)

links = driver.find_elements_by_xpath('//h3/a[@href]')
link = driver.find_elements_by_xpath('//h3/a[@href]')[0]
url = link.get_attribute('href')

actions = ActionChains(driver)
tab = actions.send_keys(Keys.TAB * 20)
tab.perform()
new = tab.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.ENTER)
new.perform()
driver.switch_to.window(driver.window_handles[1])
sleep(10)
driver.close()
driver.switch_to.window(driver.window_handles[0])


# ctrl + shift + enter => open new tab with link

'''
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get(url)
sleep(10)
driver.close()
driver.switch_to.window(driver.window_handles[0])
'''

'''
sel = Selector(text=driver.page_source)
link = sel.xpath('//h3/a/@href').extract()[0]
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get(link)
sleep(10)
driver.close()
driver.switch_to.window(driver.window_handles[0])
'''

sleep(20)
driver.close()
driver.quit()


'''
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

all_keys = ["american legends", "income", "funny videos", "python for kids"]

driver = webdriver.Chrome()
driver.get("https://engine.presearch.org")

search_query = driver.find_element_by_name('q')
search_query.send_keys(random.choice(all_keys))
search_query.send_keys(Keys.RETURN)
'''