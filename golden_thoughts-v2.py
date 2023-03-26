import smtplib
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# dane logowania do skrzynki pocztowej
MY_ADDRESS = 'zlotemysliNPG@gmail.com'
MY_PASSWORD = 'theaiualjmhmyfrn'

# dane odbiorcy wiadomości
adres = input("Podaj adres na który chcesz wysłać wiadomość: ")
TO_ADDRESS = adres

# konfiguracja serwera SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# dodanie plików z bazami danych
filename1 = 'Bazy danych\Baza złotych myśli.txt'
filename2 = 'Bazy danych\Piosenki.txt'
quotes = []
displayed_quotes = []
songs = []
displayed_songs = []

# losowanie złotej myśli
def get_quotes(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        quotes = f.readlines()
    while len(displayed_quotes) < len(quotes):
      quote = random.choice(quotes)
      if quote not in displayed_quotes:
          displayed_quotes.append(quote)
          return quote
      elif len(displayed_quotes) >= len(quotes):
          return 0

# losowanie piosenki
def get_songs(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        songs = f.readlines()
    while len(displayed_songs) < len(songs):
      song = random.choice(songs)
      if song not in displayed_songs:
          displayed_songs.append(song)
          return song
      elif len(displayed_songs) >= len(songs):
          return 0

# nieskończona pętla wysyłająca maila raz dziennie
while True:
    try:
        # nawiązanie połączenia z serwerem SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(MY_ADDRESS, MY_PASSWORD)

        # treść wiadomości
        msg = MIMEMultipart()
        msg['From'] = MY_ADDRESS
        msg['To'] = TO_ADDRESS
        msg['Subject'] = 'Dzień dobry'
        message1 = 'Złota myśl na dzisiaj to:\n\n'
        message2 = get_quotes(filename1)
        message3 = '\nPropozycja piosenki na dzisiaj to:\n\n'
        message4 = get_songs(filename2)
        message5 = '\nMiłego dnia 😄'
        msg.attach(MIMEText(message1))
        msg.attach(MIMEText(message2))
        msg.attach(MIMEText(message3))
        msg.attach(MIMEText(message4))
        msg.attach(MIMEText(message5))

        # wysłanie wiadomości
        server.sendmail(MY_ADDRESS, TO_ADDRESS, msg.as_string())
        server.quit()

        print('Wiadomość wysłana')
    except Exception as e:
        print(f'Błąd podczas wysyłania wiadomości: {str(e)}')
    # oczekiwanie na kolejny dzień
    time.sleep(24 * 60 * 60)  # 24 godziny w sekundach