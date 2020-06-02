from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path="/home/samir/Desktop/GITHUB/python/week8-day2-python-selenium-task-Ssamirr/geckodriver")
driver.get("https://www.facebook.com")
driver.implicitly_wait(5)
sleep(3)


email = driver.find_element_by_id("email")
email.send_keys('asdfgh')

password = driver.find_element_by_id("pass")
password.send_keys('asdfgh')

login = driver.find_element_by_css_selector("#loginbutton")
login.click()