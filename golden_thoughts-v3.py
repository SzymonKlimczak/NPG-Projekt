import smtplib
import time
import random
import tkinter as tk
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_ADDRESS = 'zlotemysliNPG@gmail.com'
MY_PASSWORD = 'theaiualjmhmyfrn'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def inicjalizacjaOkienka():
    root = tk.Tk()
    root.geometry('480x480')
    root.title('Złote myśli')
    return root

def inicjalizacjaEkranu(root):
    ekran = tk.Label(root, bg="lightyellow",text="Wpisz adres e-mail, na który chcesz otrzymywać codzienną złotą myśl", width=55, borderwidth=2)
    ekran.grid(row = 0, column = 0)
    return ekran

def inicjalizacjaPolaNaDane(root, ekran):
    pole_na_dane = tk.Entry(root)
    pole_na_dane.grid(row = 1, column = 0,ipadx = 50, ipady = 5)
    info = tk.Label(root, text="", width=55, borderwidth=2)
    info.grid(row=3, ipadx=15, ipady=1)
    return pole_na_dane

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

def inicjalizacjaPrzycisku(root,ekran,pole_na_dane):
    def send_email():
        TO_ADDRESS = pole_na_dane.get()
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
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.ehlo()
            server.starttls()
            server.login(MY_ADDRESS, MY_PASSWORD)
            server.sendmail(MY_ADDRESS, TO_ADDRESS, msg.as_string())
            server.quit()
            print('Wiadomość wysłana')
        except Exception as e:
            print(f'Błąd podczas wysyłania wiadomości: {str(e)}')
        root.destroy()
    przycisk = tk.Button(root, text = "Wyślij", command=send_email)
    przycisk.grid(row = 2)
    return przycisk

if __name__ == '__main__':
    root = inicjalizacjaOkienka()
    ekran = inicjalizacjaEkranu(root)
    pole_na_dane = inicjalizacjaPolaNaDane(root, ekran)
    przycisk = inicjalizacjaPrzycisku(root, ekran, pole_na_dane)
    root.mainloop()

# oczekiwanie na kolejny dzień
    time.sleep(24 * 60 * 60)  # 24 godziny w sekundach
