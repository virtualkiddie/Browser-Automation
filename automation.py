#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Driver_Path
s=Service('/home/hoaxer/PycharmProjects/Browser-Automation/chromedriver')

#Browser_Binary_Path
brave_path = "/usr/bin/brave-browser"

#Chrome_Options
option = webdriver.ChromeOptions()
option.binary_location = brave_path

# Create new Instance of Chrome
browser = webdriver.Chrome(service=s,options=option)

#url
browser.get("https://shopatsc.com/account/login")

#Find xpath element function
def xpath(path):
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            By.XPATH, path))).click()
    return path

#username
user = open('username.txt','r').read().split('\n')
browser.find_element_by_xpath("//input[@id='CustomerEmail']").send_keys(user)

time.sleep(1)

#password
passwd = open('password.txt','r').read().split('\n')
browser.find_element_by_xpath("//input[@id='CustomerPassword']").send_keys(passwd)

xpath("//input[@type='submit']")

time.sleep(2)

browser.get('https://shopatsc.com/collections/playstation/products/ps5-marvels-spiderman-miles-morales-ultimate-edition')

#check pincode
browser.find_element_by_xpath("//input[@class='check-delivery-pincode']").send_keys("600070")

#xpath elements
xpath('//*[@id="check-delivery-submit"]')
xpath("//*[@id='product_form_5074936397963']/div[3]/div/button[2]")
xpath('//*[@id="continue_to_shipping_button_custom"]')
xpath('/html/body/div/div/div/header/nav/ol/li[1]/a')
xpath('//*[@id="checkout_button"]')
xpath('/html/body/div/div/div/header/nav/ol/li[1]/a')
xpath('//*[@id="Path_469"]')

time.sleep(2)

browser.get('https://shopatsc.com/cart/39459759554699:1')

#Refresh until find element
while True:
    try:
        browser.find_element_by_xpath('//*[.="Continue to payment"]')
    except NoSuchElementException:
        browser.refresh()
    else:
        button = browser.find_element_by_xpath('//*[.="Continue to payment"]')
        browser.execute_script("arguments[0].click();", button)
        break

#Wait until clickable element
cmplt = WebDriverWait(browser, 9999999999).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="continue_button"]')))
cmplt.click()