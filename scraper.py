import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Test-Exclusive-748/dp/B07DJLVJ5M/ref=sr_1_1?crid=1DDCZ4YCPPUE9&keywords=one+pluse7t&qid=1574061459&sprefix=one+plus%2Caps%2C328&sr=8-1'

headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:8].replace(',', ''))
    print(title.strip())
    print(converted_price)
    if converted_price < 38000:
        send_main()
    else:
        print('else executed')


def send_main():
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('yogeshparwani.yp99@gmail.com', 'jsyjniinhtoibxut')

    subject = 'Hey the price fell down'
    body = f'Check the amazon link {URL}'
    message = f'Subject: {subject}\n\n {body}'

    server.sendmail(
        'yogeshparwani.yp99@gmail.com',
        'yogeshparwani99.yp@gmail.com',
        message
    )

    print('Email Sent!')


while True:
    check_price()
    time.sleep(60)
