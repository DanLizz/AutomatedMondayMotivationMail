import smtplib
import datetime as dt
import random

my_email = "franciselizabeth7221@gmail.com"
my_password = "Danlizz@7"

your_mail = "francismaria7221@yahoo.com"
your_password = "btenpbushitdydzz"


with open("quotes.txt", "r") as file:
    contents = [content.rstrip() for content in file]


def send_mondaymail():
    quote = random.choice(contents)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=your_mail,
                            msg=f"Subject:Motivational Monday\n\n{quote}")


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    send_mondaymail()