from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def mat(num):
  return math.log(abs(12*math.sin(num)))

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    time.sleep(2)
    num_0 = browser.find_element_by_id("input_value")
    num = int(num_0.text)
    func_0 = mat(num)
    func = str(func_0)
    func_field = browser.find_element_by_id("answer")
    func_field.send_keys(func)
    irobot = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", irobot)
    irobot.click()
    robot_rule = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
    robot_rule.click()
    #browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
    button = browser.find_element_by_css_selector("body > div.container > form > button").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}') 

finally:
    time.sleep(10)
    browser.quit()
    