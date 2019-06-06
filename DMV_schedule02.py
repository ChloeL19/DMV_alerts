#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:40:48 2019

@author: chloeloughridge
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from threading import Timer

# run this forever


# when it hits 11:30 perform this

# click button to navigate to the schedule page
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www12.honolulu.gov/csdarts/default.aspx')
button = driver.find_element_by_id('btnAcceptTop')
button.click()

available_dates = []

# every 5 minutes, press the go button to find the next available date
def timeout():
    # press the go button to find the next available date
    driver.find_element_by_id('btnDateJump').click()
    # print that date
    date = driver.find_element_by_id('lblDate').text
    available_dates.append(date)
    print(date)

# check once upon startup
timeout()

# check every 5 min three times following first check
for i in range(3):
    t = Timer(5*60, timeout)
    t.start()
    t.join()
