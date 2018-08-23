# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('http://tms-qa.liftit-sandbox.com/services');
driver.save_screenshot('1.png')
driver.find_element_by_name('email').send_keys('adriana.lozano@liftit.co')
driver.find_element_by_name('password').send_keys('lozano0413')
time.sleep(2)
driver.save_screenshot('2.png')
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.save_screenshot('3.png')

driver.find_element_by_xpath("//a[contains(text(),'Integraciones')]").click()
time.sleep(2)
driver.save_screenshot('4.png')
driver.find_element_by_xpath("//a[contains(text(),'Crear servicio con ordenes')]").click()
driver.save_screenshot('5.png')
time.sleep(2)
select = Select(driver.find_element_by_name("filter[hub_id]"))
select.select_by_value('16')
time.sleep(2)
driver.save_screenshot('6.png')

select = Select(driver.find_element_by_name("filter[valid]"))
select.select_by_value('true')
time.sleep(2)
driver.save_screenshot('7.png')
driver.find_element_by_xpath("//button[@id='submit_filter_form']").click()
time.sleep(2)
driver.save_screenshot('8.png')

for i in range(9):
    try:
        driver.find_element_by_xpath(
            "//input[@value='237702']"
        ).click()
        driver.find_element_by_xpath(
            "//input[@value='237713']"
        ).click()
        break
    except NoSuchElementException as e:
        print('retry in 1s.')
        time.sleep(1)

time.sleep(2)
driver.save_screenshot('9.png')

driver.find_element_by_xpath("//button[@id='create']").click()
time.sleep(2)
driver.save_screenshot('10.png')









