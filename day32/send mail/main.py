
'''
import smtplib

my_email = "nitishtestcode@gmail.com"
# my_email = "nitishcs007@gmail.com"
my_password = "kquzwknimldbwhzc "

#connection = smtplib.SMTP("smtp.gmail.com")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    # connection.sendmail(from_addr=my_email, to_addrs="nitishtestcode@outlook.com", msg="Hello")
    # add subject
    connection.sendmail(
        from_addr=my_email,
        to_addrs="nitishtestcode@outlook.com",
        msg="Subject:Connection\n\nThis is the body message."
    )

# if we use "with" keyword to open connection then no need to close this.
#connection.close()
'''

import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(now)
print(year)
print(month)
print(day_of_week)

date_of_birth = dt.datetime(year=1990, month=12, day=24)
print(date_of_birth)

with open("quotes.txt") as fp:
    quotes = fp.readlines()
    # print(quotes)
quote = random.choice(quotes)
print(quote)
