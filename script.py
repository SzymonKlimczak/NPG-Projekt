import smtplib, ssl
import getpass

port = 465
sender_email = input("Podaj email nadawcy (gmail): ")
password = getpass.getpass("Podaj haslo i nacisniej ENTER: ")
receiver_email = input("Podaj email odbiorcy: ")

message = """\
Subject: Test

Testujemy pythona"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Wyslano")
