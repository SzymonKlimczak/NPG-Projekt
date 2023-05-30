import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Otwórz plik z adresem e-mail odbiorcy
with open("Bazy Danych/email.txt", "r") as mails:
    mail_name = mails.read().strip()

# dane logowania do skrzynki pocztowej
MY_ADDRESS = 
MY_PASSWORD = 

# dane odbiorcy wiadomości
TO_ADDRESS = mail_name

# konfiguracja serwera SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# dodanie plików z bazami danych
QUOTE_FILENAME = 'Bazy danych/Baza_złotych_myśli.txt'
SONG_FILENAME = 'Bazy danych/Piosenki.txt'

# pliki z informacjami o wykorzystanych złotych myślach i piosenkach
USED_QUOTES_FILENAME = 'Bazy danych/quotes-used.txt'
USED_SONGS_FILENAME = 'Bazy danych/songs-used.txt'

# wczytanie informacji o wykorzystanych złotych myślach i piosenkach
with open(USED_QUOTES_FILENAME, 'a+') as f:
    f.seek(0)
    displayed_quotes = f.read().splitlines()
with open(USED_SONGS_FILENAME, 'a+') as f:
    f.seek(0)
    displayed_songs = f.read().splitlines()

# losowanie złotej myśli
def get_quotes(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        quotes = f.readlines()
    while len(displayed_quotes) < len(quotes):
        quote = random.choice(quotes)
        if quote.strip() not in displayed_quotes:
            displayed_quotes.append(quote.strip())
            with open(USED_QUOTES_FILENAME, 'a') as f:
                f.write(quote.strip() + " (użyte)\n")
            return quote
    return None

# losowanie piosenki
def get_songs(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        songs = f.readlines()
    while len(displayed_songs) < len(songs):
        song = random.choice(songs)
        if song.strip() not in displayed_songs:
            displayed_songs.append(song.strip())
            with open(USED_SONGS_FILENAME, 'a') as f:
                f.write(song.strip() + " (użyta)\n")
            return song
    return None

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
    message2 = get_quotes(QUOTE_FILENAME)
    message3 = '\nPropozycja piosenki na dzisiaj to:\n\n'
    message4 = get_songs(SONG_FILENAME)
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
