import tkinter as tk
from tkinter import messagebox


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

def inicjalizacjaPrzycisku(root,ekran):
    przycisk = tk.Button(root, text = "Wyślij")
    przycisk.grid(row = 2)

    return przycisk



if __name__ == '__main__':
    root = inicjalizacjaOkienka()

    ekran = inicjalizacjaEkranu(root)

    pole_na_dane = inicjalizacjaPolaNaDane(root, ekran)

    przycisk = inicjalizacjaPrzycisku(root,ekran)



    root.mainloop()
