import smtplib
import datetime as dt
import random

my_email = "abc@gmail.com"
password = "pass"
to_email = "xyz@gmail.com"


def send_email(subject, body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        print("sending email...")
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}"
        )


def get_random_quote():
    with open("quotes.txt") as file:
        quotes = file.readlines()
        return random.choice(quotes)


now = dt.datetime.now()

if now.weekday() == 3:
    quote = get_random_quote()
    send_email(subject="Thursday Motivation", body=quote)
