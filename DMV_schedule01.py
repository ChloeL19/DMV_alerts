#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:40:48 2019

@author: chloeloughridge
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# click button to navigate to the schedule page
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www12.honolulu.gov/csdarts/default.aspx')
button = driver.find_element_by_id('btnAcceptTop')
button.click()

# press the go button to find the next available date
driver.find_element_by_id('btnDateJump').click()

date = driver.find_element_by_id('lblDate')
print(date.text)
