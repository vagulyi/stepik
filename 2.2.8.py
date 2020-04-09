from selenium import webdriver
import os
import time


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser  = webdriver.Chrome()
    browser.get(link)

    fields = browser.find_elements_by_css_selector('[type=text]')
    for x in fields:
    	x.send_keys('OK')

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, '2.2.8.txt')
    element = browser.find_element_by_xpath('//*[@id="file"]')
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
	time.sleep(3)

	browser.quit()
	

