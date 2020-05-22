#!/usr/bin/env python
# coding: utf-8

# ## Install this pre-requisites
#
# Requests library will be used to get/send data. <br>
# BeautifulSoup library will be used to parse the webpage
#
# - pip install requests
# - pip install beautifulsoup4
# - pip install smtplib


# Importing Libraries

import requests
from bs4 import BeautifulSoup
import smtplib
import time


# Enter the link of the product you want to track below

url = ''


# Now we will give the information of our current browser
# Search google "My User Agent"
# Copy paste in User-Agent

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def check_price():
    """.com makes the html code with javascript. You can trick them with using 2 soups.
     Load soup1 and then load soup2 with soup1.prettify().
     Then you got soup2 loaded correctly and you can do all the fun stuff. """
    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    """ To find the title of the Amazon product, go to the amazon website and press f12
        Click the top left arrow on inspect bar and then hover over the title and Price to find the id"""

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = price[:-3]

    # get rid of excess blank spaces and print the current title and price
    print(title.strip())
    print(converted_price.strip())

    # Now Enter the price you want keep as threshold
    # When the price drops below the threshold it will send you a mail

    # You can edit the price you want to keep
    if (converted_price < converted_price):
        send.mail()


# In order connect to our mail account to send a notification, we'll need to setup a password for this
# NOTE: This won't work if you have the 2-Step Verification turned on
# You'll need too turn it on inorder for this to work
# Your Allow less secured app should be On
# **** https://myaccount.google.com/lesssecureapps ***

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls  # encrypt the connection
    server.ehlo()

    # login in to the gmail server using our credentials
    # you can use your gmail or the 16 digit password that you generated
    server.login('yourname@gmail.com', 'yourpassword')

    subject = 'The Price for your item just fell down!'
    body = 'Check the Amazon link (your URL)'

    msg = f"Subject:{subject}\n\n{body}"

    # from, to eg. ab123@gmail.com to abc@gmail.com
    server.sendmail('ab123@gmail.com', 'abc@gmail.com', msg)
    server.quit()


print('Go check your email! Now Fool!')


while(True):
    check_price()
    time.sleep(60 * 60)
