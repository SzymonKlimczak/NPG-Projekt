import smtplib, ssl
port = 587 
smtp_server = "smtp.gmail.com"
sender_email = "buynever@gmail.com" #potrzeba zmienić uprawnienia
receiver_email = "mkuc@student.agh.edu.pl"
password = input("Hasło:")
message = """\
Subject: Test
Automatyczna wiadomość."""
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo() 
    server.starttls(context=context)
    server.ehlo() 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message) 