import datetime as dt
import pandas as pd
from random import choice
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
PASSWORD = os.envrion.get("PASSWORD")

# 1. Update the birthdays.csv
def check_birthday():
    today_month = dt.datetime.now().month
    today_day = dt.datetime.now().day
    date = (today_month,today_day)

    data = pd.read_csv("birthdays.csv")
    # 2. Check if today matches a birthday in the birthdays.csv
    dic_list3 = [{'name':info['name'],'email':info['email']}   for (index, info) in data.iterrows() if (info.month,info.day) == date]
    return dic_list3

birthdays = check_birthday()
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if birthdays:
    with smtplib.SMTP('smtp.gmail.com') as connections:
        connections.starttls()
        connections.login(user=my_email, password=PASSWORD)

        for person in birthdays:
            letter = choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
            with open(f"letter_templates/{letter}", 'r') as file:
                text = file.read().replace('[NAME]', f'{person["name"]}')
                print(text)
            # 4. Send the letter generated in step 3 to that person's email address.

                connections.sendmail(from_addr=my_email,to_addrs=person['email'],  msg=f"Subject: It's your Birthday!!\n\n{text} ")










