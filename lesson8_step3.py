from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum(x, y):
  return str (x + y)

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    time.sleep(2)
    num1 = browser.find_element_by_id("num1")
    x = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    y = int(num2.text)
    z = sum(x, y)
    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector("[value='" + z + "']").click()
    button = browser.find_element_by_css_selector("body > div.container > form > button").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}') 

finally:
    time.sleep(10)
    browser.quit()
    