#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:58:49 2019

@author: chloeloughridge
"""

import smtplib
from email.message import EmailMessage

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
password 
smtpObj.login(' chloe.loughridge@gmail.com ', password ) #DEFINITELY NOT POSTING TO GITHUB
# Will have to set up application-specific password
smtpObj.sendmail(' chloe.loughridge@gmail.com ', ' chloe.loughridge@gmail.com ',
                 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob' + available_dates) # maybe could just enter 'msg'
# alternative message construction
smtpObj.sendmail(msg)
