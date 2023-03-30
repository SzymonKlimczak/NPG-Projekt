import smtplib, ssl
import getpass
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

absolute_path = os.path.dirname(__file__)
relative_path = "Bazy danych/Baza złotych myśli.txt"
full_path = os.path.join(absolute_path, relative_path)

def get_quotes(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        quotes = f.readlines()
    return quotes

port = 465
sender_email = input("Podaj email nadawcy (gmail): ")
password = getpass.getpass("Podaj haslo i nacisniej ENTER: ")
receiver_email = input("Podaj email odbiorcy: ")

# tworzymy wiadomość e-mail
message = MIMEMultipart()
message["Subject"] = "Złota myśl dnia"
message["From"] = sender_email
message["To"] = receiver_email

#wybór złotej myśli
quotes = get_quotes(full_path)
selected_quote = random.choice(quotes)

# dodajemy treść wiadomości
text = MIMEText(selected_quote)
message.attach(text)

# wysyłamy wiadomość
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Wyslano")
