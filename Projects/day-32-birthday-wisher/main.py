import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "abc@gmail.com"
PASSWORD = "pass"
TO_EMAIL = "xyz@gmail.com"

birthdays = pandas.read_csv("birthdays.csv")
data = birthdays.to_dict('records')


def generate_random_letter(birthday_name):
    rand = random.randint(1, 3)

    with open(f"letter_templates/letter_{rand}.txt") as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_name, 1)

    return content


def send_email(message, subject="Happy Birthday!"):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:{subject}\n\n{message}"
        )


now = dt.datetime.now()
for item in data:
    month, day, name = item["month"], item["day"], item["name"]

    if now.month == month and now.day == day:
        letter = generate_random_letter(name)
        send_email(letter, subject=f"Happy Birthday {name}")
