from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element_by_id("num1")
    a_atr = value1.text
    value2 = browser.find_element_by_id("num2")
    b_atr = value2.text
    result = str(int(a_atr)+int(b_atr))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(result)
    
    submit = browser.find_element_by_xpath("/html/body/div/form/button")
    submit.click()


    
finally:
    time.sleep(5)
    browser.quit()


        
