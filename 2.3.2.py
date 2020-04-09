from selenium import webdriver
import os
import time
import math


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser  = webdriver.Chrome()
    browser.get(link)

    fields = browser.find_element_by_tag_name('button')
    fields.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    value = browser.find_element_by_id("input_value")
    x = value.text
    y = calc(x)
    
    fname = browser.find_element_by_id('answer')
    fname.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
		time.sleep(3)

		#browser.quit()
	

