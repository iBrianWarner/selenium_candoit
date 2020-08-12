from selenium import webdriver
import random
import time
from selenium.webdriver.common.keys import Keys

DATA = {
    'username': 'Max13132im',
    'email': 'lhrnww+2@gmail.com',
    'password': 'lhrnww13'
}

def test_sign_up():
    driver = webdriver.Chrome()
    driver.get("https://react-redux.realworld.io/#/register?_k=1fkhn5")
    driver.find_element_by_css_selector('[type="text"]').send_keys('test'+str(random.randint(0, 6666666)))
    driver.find_element_by_css_selector('[type="email"]').send_keys(str(random.randint(0, 6666666)) + '@gmail.com')
    driver.find_element_by_css_selector('[type="password"]').send_keys(str(random.randint(12345678, 87654321)))
    driver.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(2)
    assert driver.find_element_by_css_selector('[href="#settings"]')
    driver.quit()
test_sign_up()

def test_sign_in(driver):
    driver.get("https://react-redux.realworld.io/#/login?_k=tclgpm")
    driver.find_element_by_css_selector('[type="email"]').send_keys(DATA['email'])
    driver.find_element_by_css_selector('[type="password"]').send_keys(DATA['password'])
    driver.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(3)
    assert driver.find_element_by_css_selector('[href="#settings"]')

def test_edit_settings():
    driver = webdriver.Chrome()
    test_sign_in(driver)
    driver.find_element_by_css_selector('[href="#settings"]').click()
    driver.find_element_by_css_selector('[placeholder="Username"]').clear()
    driver.find_element_by_css_selector('[placeholder="Username"]').send_keys('new_test_user_2222')
    driver.find_element_by_css_selector('[placeholder*="Short bio"]').clear()
    driver.find_element_by_css_selector('[placeholder*="Short bio"]').send_keys('123123123')
    # driver.find_element_by_css_selector('[placeholder="Email"]').clear()
    # driver.find_element_by_css_selector('[placeholder="Email"]').send_keys('1231234ggfgf@gmail.com')
    driver.find_element_by_css_selector('.btn.btn-lg.btn-primary.pull-xs-right').click()
    time.sleep(2)
    assert driver.find_element_by_css_selector('[href="#@new_test_user_2222"]')
test_edit_settings()


