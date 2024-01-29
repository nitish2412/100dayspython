##################### Extra Hard Starting Project ######################
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import smtplib

my_email = "nitishtestcode@gmail.com"
my_password = "kquzwknimldbwhzc"

now = dt.datetime.now()
day = now.day
month = now.month
data = pd.read_csv("birthdays.csv")
month_list = data.month.to_list()
day_list = data.day.to_list()
name_list = data.name.to_list()
email_list = data.email.to_list()
for i in range(len(month_list)):
    if day == day_list[i] and month == month_list[i]:
        print(month_list[i])
        random_index = random.randint(1,3)
        file_name= f"letter_{random_index}.txt"
        print(file_name)
        file_path = "./letter_templates/"+file_name
        print(file_path)
        with open(file_path) as fp:
            letter_data = fp.readlines()
        letter_data[0] = letter_data[0].replace("[NAME]",name_list[i])
        letter = "".join(letter_data)
        print(letter)
        message = f"Subject:Birthday wishes\n\n{letter}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs= email_list[i], msg=message)
        print(message)





