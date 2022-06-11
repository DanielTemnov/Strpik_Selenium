from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def mat(x):
  return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    time.sleep(2)
    button = browser.find_element_by_css_selector("form > div > div > button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x = browser.find_element_by_id("input_value")
    y = int(x.text)
    result0 = mat(y)
    result1 = str(result0)
    insert_result = browser.find_element_by_id("answer")
    insert_result.send_keys(result1)
    button = browser.find_element_by_css_selector("form > div > div > button")
    button.click()
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}') 

finally:
    time.sleep(10)
    browser.quit()
    