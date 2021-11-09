#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Driver_Path
s=Service('/home/hoaxer/PycharmProjects/Browser-Automation/chromedriver')
#driver_path = "/home/hoaxer/PycharmProjects/automation/chromedriver"


#Browser_Binary_Path
brave_path = "/usr/bin/brave-browser"

#Chrome_Options
option = webdriver.ChromeOptions()
option.binary_location = brave_path

#option.add_argument("--incognito")
#option.add_argument("--headless")

# Create new Instance of Chrome
browser = webdriver.Chrome(service=s,options=option)
#browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

browser.get("https://shopatsc.com/")

