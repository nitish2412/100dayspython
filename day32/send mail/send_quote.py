import datetime as dt
import random
import smtplib

my_email = "nitishtestcode@gmail.com"
my_password = "kquzwknimldbwhzc"
now = dt.datetime.now()
weekday = now.weekday()
with open("quotes.txt") as fp:
    quotes = fp.readlines()
quote = random.choice(quotes)

# message = "Subject:Sunday quote\n\n"+quote
message = f"Subject:Sunday Motivation\n\n{quote}"
if weekday == 6:
    print(weekday)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="nitishtestcode@outlook.com", msg=message)


