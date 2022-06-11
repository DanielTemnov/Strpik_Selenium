from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    time.sleep(2)
    button1 = browser.find_element_by_css_selector("form > div > input:nth-child(2)")
    button1.send_keys('Dan')
    button2 = browser.find_element_by_css_selector("form > div > input:nth-child(4)")
    button2.send_keys('Dan')
    button3 = browser.find_element_by_css_selector("form > div > input:nth-child(6)")
    button3.send_keys('Dan')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector("form > button")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}') 

finally:
    time.sleep(10)
    browser.quit()
    