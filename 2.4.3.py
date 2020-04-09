from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button = browser.find_element_by_id('book')
button.click()

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

value = browser.find_element_by_id("input_value")
x = value.text
y = calc(x)

fname = browser.find_element_by_id('answer')
fname.send_keys(y)

button2 = browser.find_element_by_id("solve")
button2.click()
    
