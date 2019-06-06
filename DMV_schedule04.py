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
import smtplib
from email.message import EmailMessage

# get password for sending email
#password = input('Enter your password here:')

# run this forever
while(True):

    # when it hits 11:30 perform this
    curr_time = datetime.datetime.now().time()
    #print(curr_time)
    if (curr_time == datetime.time(19,50,00)): #WILL BE CHANGED TO 12AM
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
        while datetime.datetime.now().time() < datetime.time(19, 51, 00): #NOT YET SURE WHEN WE WANT TO STOP CHECKING, IF EVER --> maybe just check early in morning, or hey, run forever
            t = Timer(5, timeout)
            t.start()
            t.join()
            
        if datetime.datetime.now().time() == datetime.time(19, 51, 10): # will be changed to "if the available date changes" --> send that new info
            print("sending the email message")
            msg = EmailMessage()
            msg.set_content(available_dates)
            msg['Subject'] = 'DMV Available Times'
            msg['From'] = 'chloe.loughridge@gmail.com'
            msg['to'] = 'chloe.loughridge@gmail.com' # can I send to multiple people?
            # send the message over gmail
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587) # maybe smtplib.SMTP_SSL() and port 465
            smtpObj.ehlo()
            smtpObj.starttls()
            # REMOVE THIS
            password = 
            smtpObj.login(' chloe.loughridge@gmail.com ', password ) #DEFINITELY NOT POSTING TO GITHUB
            # Will have to set up application-specific password
            smtpObj.sendmail(' chloe.loughridge@gmail.com ', ' chloe.loughridge@gmail.com ',
                             'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob' + available_dates) # maybe could just enter 'msg'
            # alternative message construction
            smtpObj.sendmail(msg)
            
