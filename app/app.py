import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sqlite3

def store_db(product_asin, product_name, product_price, product_ratings, product_ratings_num, product_link):
    conn = sqlite3.connect('amazon_search.db')
    curr = conn.cursor()

    # create table
    
    curr.execute('''CREATE TABLE IF NOT EXISTS search_result (ASIN text, name text, price real, ratings text, ratings_num text, details_link text)''')
    # insert data into a table
    curr.executemany("INSERT INTO search_result (ASIN, name, price, ratings, ratings_num, details_link) VALUES (?,?,?,?,?,?)", 
                    list(zip(product_asin, product_name, product_price, product_ratings, product_ratings_num, product_link)))
        
    conn.commit()
    conn.close()


options = webdriver.ChromeOptions()
options.add_argument('--headless')

keyword = 'raspberry pi 4'
next_page = ''

def scrape_amazon(keyword, max_pages):

    page_number = 1
    driver = webdriver.Chrome()
    web = 'https://www.amazon.fr/'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # create a driver object using driver_path as a parameter
    driver.get(web)

    driver.implicitly_wait(5)
    keyword = keyword
    search_box = driver.find_element_by_id('twotabsearchtextbox')
    search_box.send_keys(keyword)
    search_button = driver.find_element_by_id('nav-search-submit-button')
    search_button.click()
    
    driver.implicitly_wait(5)

    while page_number <= max_pages:
        scrape_page(driver)
        driver.get(next_page)
        driver.implicitly_wait(5)
        page_number += 1
    driver.quit()

def scrape_page(driver):
    
    product_name = []
    product_asin = []
    product_price = []
    product_ratings = []
    product_ratings_num = []
    product_link = []
    
    items = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
    for item in items:
        name = item.find_element(By.XPATH,'.//span [@class="a-size-base-plus a-color-base a-text-normal"]')
        product_name.append(name.text)

        data_asin = item.get_attribute("data-asin")
        product_asin.append(data_asin)
        # find prices
        whole_price = item.find_elements(By.XPATH,'.//span[@class="a-price-whole"]')
        #fraction_price = item.find_elements(By.XPATH,'.//span[@class="a-price-fraction"]')
        #if whole_price != [] and fraction_price != []:
        #    price = '.'.join([whole_price[0].text, fraction_price[0].text])
        if whole_price != []:
            price = '.'.join([whole_price[0].text])
        else:
            price = 0
        product_price.append(price)

        # find a ratings box
        ratings_box = item.find_elements_by_xpath('.//div[@class="a-row a-size-small"]/span')
        if ratings_box != []:
            ratings = ratings_box[0].get_attribute('aria-label')
            ratings_num = ratings_box[1].get_attribute('aria-label')
        else:
            ratings, ratings_num = 0, 0
        product_ratings.append(ratings)
        product_ratings_num.append(str(ratings_num))

        link = item.find_element_by_xpath('.//a[@class="a-link-normal a-text-normal"]').get_attribute("href")
        product_link.append(link)
    # store data from lists to database
    global next_page
    next_page = driver.find_element(By.XPATH,'//li[@class ="a-selected"]/following-sibling::li/a').get_attribute("href")
    
    store_db(product_asin, product_name, product_price, product_ratings, product_ratings_num, product_link)

scrape_amazon(keyword,2)
