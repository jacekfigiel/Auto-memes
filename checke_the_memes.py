from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://memes.com/")
html_elm = browser.find_element_by_tag_name("html")
time.sleep(5)
browser.fullscreen_window()
time.sleep(5)
for i in range(900):
    html_elm.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.4)
