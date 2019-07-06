import requests #to load the page
import smtplib #to send email
import time
from bs4 import BeautifulSoup
url='https://www.amazon.in/Harry-Potter-ChildrenS-Paperback-Boxed/dp/1408856778/ref=sr_1_3?keywords=harry+potter+complete+collection&qid=1562410535&s=gateway&sr=8-3'
# user agent gives info abput the browser.
header={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
def check():
    page=requests.get(url,headers=header)
    soup=BeautifulSoup(page.content,'html.parser')
    # print(soup.prettify())

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="soldByThirdParty").get_text()
    p=''
    for i in price:
        if(i=='.' or i.isdigit()):
            p+=i
    # print(title)
    price=float(p)
    if(price<1750):
        send_mail()
    else:
        print("Not changed",price)

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('rohithrajesh4@gmail.com','rvlsfcmyvjzqcrwn')

    subject='The price fell down'
    body='Check the link: https://www.amazon.in/Harry-Potter-ChildrenS-Paperback-Boxed/dp/1408856778/ref=sr_1_3?keywords=harry+potter+complete+collection&qid=1562410535&s=gateway&sr=8-3'
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
            'rohithrajesh4@gmail.com',
            'shobhaj1974@gmail.com',
            msg
        )
    print('Email sent')
    server.quit()

while(True):
    check()
    time.sleep(60*60)