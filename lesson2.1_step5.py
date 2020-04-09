from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

#image = browser.find_element_by_id("treasure")
#image_value = image_value.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

image_value = browser.find_element_by_id("treasure")
x = image_value.get_attribute("valuex")
y = calc(x)

fname = browser.find_element_by_id('answer')
fname.send_keys(y)

fname = browser.find_element_by_id('robotCheckbox')
fname.click()

fname = browser.find_element_by_id('robotsRule')
fname.click()

submit = browser.find_element_by_xpath("//html/body/div/form/div/div/button")
submit.click()



time.sleep(5)

browser.quit()


        
