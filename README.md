# Narzędzia Pracy Grupowej - Projekt
## Cel projektu ("Złota myśl na każdy dzień")
Projekt polega na stworzeniu programu do wysyłania na wybrany adres mailowy wiadomości ze „złotą myślą” na każdy dzień.

## Twórcy projektu
#### Szymon Klimczak, Maksymilian Kania, Mateusz Kuc, Antoni Krempa

## Funkcjonalności jakie ma posiadać program
#### Podstawowymi funkcjonalnościami są:
* Zawiera bazę co najmniej 100 złotych myśli
* Program po uruchomieniu wysyła jeden mail ze złotą myślą dziennie pod podany adres
* Program pamięta które złote myśli były już użyte i ich nie powtarza
* Możliwość konfiguracji adresu email na który ma zostać wysłana złota myśl
#### Funkcjonalności dodatkowe to:
* Wysyłanie tytułu piosenki (wraz z linkiem) jako propozycji do posłuchania w danym dniu

## Terminy
Czas przewidziany na wykonanie projektu to około 4 tygodnie. W każdym tygodniu planujemy uzupełniać projekt o poszczególne zadania zaplanowane do realizacji.

Planowanym terminem zakończenia projektu są przedostatnie zajęcia laboratoryjne przedmiotu Narzędzia pracy grupowej.

## Problemy jakie możemy napotkać
* Implementacja utworzonej bazy danych do programu
* Wysyłanie maila codziennie o tej samej godzinie
* Połączenie poszczególnych kodów w całość
* Raz wykorzystane "złote myśli" mają się nie powtarzać

## Instrukcja

W repozytorium znajdują się dwa pliki do uruchamiania programu:
* add_emai.py - należy uruchomić go jako pierwszy ponieważ służy do konfiguracji adresu mailowego; po wpisaniu adresu tworzy on w folderze Bazy danych plik email.txt, w którym znajduje się podany kod
* golden_thoughts.py - główny kod, który po uruchomieniu wysyła wiadomość na podany wcześniej adres mailowy

W folderze Bazy danych znajdują się dwa pliki - jeden z bazą złotych myśli, a drugi z bazą piosenek

W folderze kody częściowe najdują się kody, które tworzyliśmy w trakcie trwania projektu, które ostatecznie zostały połączone w całość jako główny kod

Plik NPG4_2_Klimczak_Kania_Kuc_Krempa to dokumentacje naszego projektu
