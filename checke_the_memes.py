from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://jbzd.com.pl/")
html_elm = browser.find_element_by_tag_name("html")
time.sleep(5)
browser.find_element_by_class_name("MuiTouchRipple-root").click()
time.sleep(5)
for i in range(5):
    html_elm.send_keys(Keys.PAGE_DOWN)
    time.sleep(10)
html_elm.send_keys(Keys.HOME)