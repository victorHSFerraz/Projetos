from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_id('bigCookie')
sleep(10)
while True:
    cookie.click()