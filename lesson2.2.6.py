from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

#image = browser.find_element_by_id("treasure")
#image_value = image_value.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

value = browser.find_element_by_id("input_value")
x = value.text
y = calc(x)

fname = browser.find_element_by_id('answer')
fname.send_keys(y)

fname = browser.find_element_by_id('robotCheckbox')
fname.click()

fname = browser.find_element_by_id('robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", fname)
fname.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()



time.sleep(5)

browser.quit()


        
