from selenium import webdriver
import time
import math 

link = "http://suninjuly.github.io/simple_form_find_task.html"

def link():
    return str(math.ceil(math.pow(math.pi, math.e)*10000))
    

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #l = link()
    link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    time.sleep(1)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(30)

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла