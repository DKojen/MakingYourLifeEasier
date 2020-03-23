#! python 3
'''
This simple web scraping code helps to check if your dreamed climbing shoes is worth it's price...
Then send you an email to announce if the price is low enough.
Checking every 24hours
'''

import requests
import smtplib
import time
from bs4 import BeautifulSoup
from lxml import html

url = 'https://www.amazon.com/Sportiva-Miura-Womens-Climbing-White/dp/B071WPG38N/ref=sr_1_8?crid=2NKFMQJIVXAI8&dchild=1&keywords=la%2Bsportiva%2Bclimbing%2Bshoes%2Bwomen&qid=1584951340&sprefix=la%2Bsportiva%2Caps%2C390&sr=8-8&swrs=78F3C944553A946931F39F3F55AABBAF&th=1&psc=1'

#'My user agent' - you can serch it in google and paste below

def check_price():
    
    headers = {'User-Agent': 'My user agent'}
    page = requests.get(url, headers=headers)


    soup = BeautifulSoup(page.content,features='lxml')


    title = soup.select("#productTitle")[0].get_text().strip()
    price = soup.select("#priceblock_ourprice")[0].get_text()
    converted_price = float(price[1:]) #get all the characters after the currency symbol
        
    print(converted_price)
    print(title)

    if(converted_price < 160.0):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    server.login('d.******@hotmail.com', '***********')

    subject = "Miura's price fell down!"
    body = "Check the amazon link: https://www.amazon.com/Sportiva-Miura-Womens-Climbing-White/dp/B071WPG38N/ref=sr_1_8?crid=2NKFMQJIVXAI8&dchild=1&keywords=la%2Bsportiva%2Bclimbing%2Bshoes%2Bwomen&qid=1584951340&sprefix=la%2Bsportiva%2Caps%2C390&sr=8-8&swrs=78F3C944553A946931F39F3F55AABBAF&th=1&psc=1"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'd.******@hotmail.com',
        'd.******@hotmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()

while(True):
    check_price()
    time.sleep(86400) #in seconds 60*60*12

    
    
