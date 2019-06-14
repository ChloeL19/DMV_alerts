#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:40:48 2019

@author: chloeloughridge
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from threading import Timer
import smtplib

# get password for sending email
password = input('Enter your password here:')
run = input('yes or no: ') # just say yes, or if you have second thoughts say no

if run=='yes':
    # click button to navigate to the schedule page
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www12.honolulu.gov/csdarts/default.aspx')
        button = driver.find_element_by_id('btnAcceptTop')
        button.click()
        
        last_date = ''
        new_date = ''
        info = ''

        # run this forever
        while(True):
    
            # every 5 secs, press the go button to find the next available date
            def timeout():
                global new_date
                global info
                # press the go button to find the next available date
                driver.find_element_by_id('btnDateJump').click()
                # print that date
                date = driver.find_element_by_id('lblDate').text
                driver.find_element_by_xpath('//*[@title="Click to reserve the appointment."]').click() #not sure this will work
                info = driver.find_element_by_id('lblAppt').text
                print("printing the info")
                print(info)
                new_date = date
                #print(date)
    
            # check every 5 secs, forever
            t = Timer(5, timeout)
            t.start()
            t.join()
            # if the date changes, then send an email
            if new_date != last_date:
                # send the message over gmail
                print("sending the message")
                smtpObj = smtplib.SMTP('smtp.gmail.com', 587) # maybe smtplib.SMTP_SSL() and port 465
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.login('chloe.loughridge@gmail.com ', password ) 
                # Will have to set up application-specific password
                print("about to send the message")
                cleanish = info.replace('\n',', ')
                cleaner = cleanish.replace(': ',' is ')
                clean = cleaner.replace(':', 'hr')
                smtpObj.sendmail('chloe.loughridge@gmail.com ', 'chloe.loughridge@gmail.com ',
                                 'Subject: Next Available DMV Date.\n'+clean) 
                
                
                last_date = new_date
                # return to appointment page before calling timout function again
                
            driver.find_element_by_id('wucHeader1_MakeAppt').click()
                
                
    
                        
