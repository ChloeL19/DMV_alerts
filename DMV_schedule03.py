#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:40:48 2019

@author: chloeloughridge
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from threading import Timer
import datetime

# run this forever
while(True):

    # when it hits 11:30 perform this
    curr_time = datetime.datetime.now().time()
    if (curr_time == datetime.time(11,48,00)): #WILL BE CHANGED TO 12AM
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

        # check every 5 min until time hits 11:50
        #for i in range(3):
        while datetime.datetime.now().time() < datetime.time(11, 50, 00): #NOT YET SURE WHEN WE WANT TO STOP CHECKING, IF EVER --> maybe just check early in morning, or hey, run forever
            t = Timer(5, timeout)
            t.start()
            t.join()
