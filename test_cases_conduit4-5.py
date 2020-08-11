from selenium import webdriver
from time import sleep

test_data = {
    'email' : 'sample@email23.com',
    'password': '12345678',
    'login' : 'auto_test1',
    'article_title' : 'autotest article1',
    'article_sub' : 'autotest  subtitle1',
    'article_text' : 'autotest main article block text',

}

url = 'http://react-redux.realworld.io/'

def login(driver):
    driver.get(url)

    sign_in_btn = driver.find_element_by_css_selector('#main > div > nav > div > ul > li:nth-child(2) > a')
    sign_in_btn.click()

    email_field = driver.find_element_by_css_selector('input[type="email"]')
    email_field.send_keys(test_data['email'])

    password_field = driver.find_element_by_css_selector('input[type="password"]')
    password_field.send_keys(test_data['password'])

    login_btn = driver.find_element_by_css_selector('button[type="submit"]')
    login_btn.click()
    driver.implicitly_wait(5)

def new_post():
    driver = webdriver.Chrome()
    login(driver)
    new_post_btn = driver.find_element_by_xpath('//a[@href="#editor"]')
    new_post_btn.click()

    article_title = driver.find_element_by_css_selector('#main > div > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input')
    article_title.send_keys(test_data['article_title'])

    subtitle_article = driver.find_element_by_css_selector('#main > div > div > div > div > div > form > fieldset > fieldset:nth-child(2) > input')
    subtitle_article.send_keys(test_data['article_sub'])

    main_txt_block = driver.find_element_by_css_selector('#main > div > div > div > div > div > form > fieldset > fieldset:nth-child(3) > textarea')
    main_txt_block.send_keys(test_data['article_text'])

    publish_btn = driver.find_element_by_css_selector('#main > div > div > div > div > div > form > fieldset > button')
    publish_btn.click()

    last_article = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div/h1')

    assert last_article.text == test_data['article_title']

    sleep(1)
    driver.quit()

def delete_post():
    driver = webdriver.Chrome()
    login(driver)
    profile_btn = driver.find_element_by_xpath('//*[@id="main"]/div/nav/div/ul/li[4]/a')
    profile_btn.click()

    articles = driver.find_elements_by_class_name('preview-link')
    articles[0].click()

    dlt_btn = driver.find_element_by_css_selector('#main > div > div > div.banner > div > div > span > button')
    dlt_btn.click()

    msg_assrt = driver.find_element_by_css_selector('[class="article-preview"]')

    assert msg_assrt.text

    driver.quit()

new_post()
delete_post()