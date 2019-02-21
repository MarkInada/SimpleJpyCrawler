from bs4 import BeautifulSoup
import urllib.request as req

from email.mime.text import MIMEText
import smtplib

url = "https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX"
upper_rate = 112.0
lower_rate = 110.0

def check_rate():
    res = req.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    table = soup.select_one('div.fxRateChart')
    bid = table.select_one("#USDJPY_detail_bid").text
    return float(bid)

def send_mail(subject):
    msg = MIMEText(url, "html")
    msg["Subject"] = subject
    msg["To"] = "Receiver@gmail.com"
    msg["From"] = "Sender@gmail.com"
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.starttls()
    gmail.login("Sender@gmail.com", "Password")
    gmail.send_message(msg)

def main():
    now_rate = check_rate()
    if (now_rate > upper_rate or now_rate < lower_rate):
        send_mail("1 Dollar = \ " + str(now_rate))
    return now_rate

def lambda_handler(event, context):
    result = main()
    return result
