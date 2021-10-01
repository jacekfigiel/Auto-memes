from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard

browser = webdriver.Chrome()
browser.get("https://memes.com/")
html_elm = browser.find_element_by_tag_name("html")
browser.fullscreen_window()
time.sleep(5)
while True:
    if keyboard.is_pressed("q"):
        browser.close()
    elif keyboard.is_pressed("0"):
        time.sleep(1)
    else:
        html_elm.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.4)


