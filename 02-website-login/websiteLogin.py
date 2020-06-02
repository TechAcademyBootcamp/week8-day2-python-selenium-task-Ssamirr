from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path="/home/samir/Desktop/GITHUB/python/week8-day2-python-selenium-task-Ssamirr/geckodriver")
driver.implicitly_wait(5)
driver.get("http://35.225.243.133/admin/login/")
sleep(2)

username = driver.find_element_by_id('id_username')
username.send_keys('student')

password = driver.find_element_by_id('id_password')
password.send_keys('qatester')

login = driver.find_element_by_css_selector('.submit-row > input:nth-child(2)')
login.click()

sleep(5)
driver.close()