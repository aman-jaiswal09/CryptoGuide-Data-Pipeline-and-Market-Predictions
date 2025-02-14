# requests
# pandas
# datetime

# this function get real time crypto currency price every dat at 8 am

import smtplib # sending email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email.encoders

import requests
import schedule
import pandas as pd
from datetime import datetime
import time

def send_mail(subject, body , file_name):

    #setup smtp_server
    smtp_server = 'smtp.google.com'
    smtp_port = 587
    sender_mail = 'jaiswalaman1699@gmail.com'
    email_password = '11311456@Aa'
    receiver_mail = 'jaiswalaman1619@gmail.com'


    # compose the mail

    message = MIMEMultipart()
    message['From'] = sender_mail
    message['To'] = receiver_mail
    message['Subject'] = subject

    # attaching body
    message.attach(MIMEText(body,'plain'))

    # attach csv
    # attach file

    with open(file_name,'rb') as file:
        part = MIMEBase('application','octet-stream')
        part.set_payload(file.read())
        email.encoders.encode_base64(part) # this line encodes the file
        part.add_header('Content-Disposition',f'attachment;filename="{file_name}"')
        message.attach(part)


        #start server
        try:
            with smtplib.SMTP(smtp_server,smtp_port) as server:
                server.starttls()
                server.login(sender_mail , email_password) # login

                # sending mail
                server.sendmail(sender_mail,receiver_mail,message.as_string())
                print("Email Sent Successfully !")

        except Exception as e:
            print(f'Unable to sent mail {e}')


# getting crypto data
def get_crypto_data():
    # API info
    url = 'https://api.coingecko.com/api/v3/coins/markets'

    param = {
        'vs_currency' : 'usd',
        'order' : 'market_cap_desc',
        'per_page': 250,
        'page': 1
    }
    # sending requests
    response = requests.get(url,params=param)

    if response.status_code == 200:
        print("Connection successful! \nGetting Data...")
        # storing the response into data
        data = response.json()

        df = pd.DataFrame(data)

        #print(df.columns)
        #prinst(df.head())  

        df = df[[
            'id','current_price','market_cap','price_change_percentage_24h',
            'high_24h','low_24h','ath','atl'
        ]]

        #creating new columns
        today = datetime.now().strftime('%d-%m-%Y  %S-%M-%H')
        df['timestamp'] = today

        # negative top 10
        #top_negative = df.sort_values(by='price_change_percentage_24h',ascending=True)
        #top_negative_10 = top_negative.head(10)
        top_negative_10 = df.nsmallest(10,'price_change_percentage_24h')
        #top_negative_10.to_csv(f'top_negative_10 of {today}.csv',index=False)

        #positive top 10
        #top_positive = df.sort_values(by='price_change_percentage_24h',ascending=False)
        top_positive_10 = df.nlargest(10,'price_change_percentage_24h')
        #top_positive_10.to_csv(f'top_positive_10 of {today}.csv',index=False)


        file_name = f'crypto_data{today}.csv'
        #saving the data
        df.to_csv(file_name,index=False)
        
        print(f"Data saved Successful as {file_name}")

        # call email function to send the reports
        subject = f"Top 10 Crypto Currency to invest for {today}"
        body = f"""
        Good Morning1\n
        
        Your Crypto report is here :\n
        
        Top 10 Crypto Currency with highiest price increase in last 24 hours!\n
        {top_positive_10}\n\n\n


        Top 10 Crypto Currency with highiest price decrease in last 24 hours!\n
        {top_negative_10}\n\n\n

        Crypto Latest Reports\n

        Regards\n
        Crypto Python Application

        """
        send_mail(subject , body , file_name)

    else:
        print(f"Connection failed Error Code {response.status_code}")

if __name__ == '__main__':

    # call the function

    # scheduling the task at 8 AM
    schedule.every().day.at('17-00').do(get_crypto_data)

    while True:
        schedule.run_pending()