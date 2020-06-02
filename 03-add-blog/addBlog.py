from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path="/home/samir/Desktop/GITHUB/python/week8-day2-python-selenium-task-Ssamirr/geckodriver")
driver.get('http://35.225.243.133/admin/')
driver.implicitly_wait(5)
sleep(3)

username = driver.find_element_by_id('id_username')
username.send_keys('student')

password = driver.find_element_by_id('id_password')
password.send_keys('qatester')

login = driver.find_element_by_css_selector('.submit-row > input:nth-child(2)')
login.click()

add_blog = driver.find_element_by_css_selector('.model-blog > td:nth-child(2)')
add_blog.click()

blog_title = driver.find_element_by_id('id_title')
blog_title.send_keys('selenium')
sleep(0.5)

blog_description = driver.find_element_by_id('id_short_description')
blog_description.send_keys('asdsafasfafasf')
sleep(0.5)

blog_fullName = driver.find_element_by_id('id_blogger_full_name')
blog_fullName.send_keys('Samir Sardarli')
sleep(0.5)

blog_content = driver.find_element_by_id('id_content')
blog_content.send_keys('dafasgafaf')
sleep(2)

blog_save = driver.find_element_by_css_selector('.default')
blog_save.click()
sleep(4)

driver.get('http://35.225.243.133/admin/')

add_blogger = driver.find_element_by_css_selector('.model-blogger > td:nth-child(2)')
add_blogger.click()
sleep(1)

blogger_fullName = driver.find_element_by_id('id_full_name')
blogger_fullName.send_keys('Samir Sardarli')
sleep(1)

blogger_save = driver.find_element_by_css_selector('.default')
blogger_save.click()
sleep(3)

driver.close()
