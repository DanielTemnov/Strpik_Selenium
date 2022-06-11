from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def mat(x):
  return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element_by_id("book")
    button1.click()
    x = browser.find_element_by_id("input_value")
    y = int(x.text)
    result0 = mat(y)
    result1 = str(result0)
    insert_result = browser.find_element_by_id("answer")
    insert_result.send_keys(result1)
    button = browser.find_element_by_id("solve")
    button.click()
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}') 

finally:
    time.sleep(10)
    browser.quit()
    