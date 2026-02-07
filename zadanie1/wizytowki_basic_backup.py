from faker import Faker
import random

class Wizytowka:
    def __init__(self, imie, nazwisko, nazwa_firmy, stanowisko, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.email = email
    
    def __str__(self):
        """Reprezentacja string obiektu: imię, nazwisko i email"""
        return f"{self.imie} {self.nazwisko} - {self.email}"

def generuj_wizytowke(lokalizacja='pl_PL'):
    """
    Tworzy instancję klasy Wizytowka z losowymi danymi za pomocą biblioteki Faker.
    """
    fake = Faker(lokalizacja)
    
    # Losowe dane
    imie = fake.first_name()
    nazwisko = fake.last_name()
    nazwa_firmy = fake.company()
    stanowisko = fake.job()
    
    # Generowanie emaila na podstawie imienia i nazwiska
    imie_email = imie.lower().replace('ą', 'a').replace('ć', 'c').replace('ę', 'e')\
                      .replace('ł', 'l').replace('ń', 'n').replace('ó', 'o')\
                      .replace('ś', 's').replace('ź', 'z').replace('ż', 'z')
    nazwisko_email = nazwisko.lower().replace('ą', 'a').replace('ć', 'c').replace('ę', 'e')\
                           .replace('ł', 'l').replace('ń', 'n').replace('ó', 'o')\
                           .replace('ś', 's').replace('ź', 'z').replace('ż', 'z')
    
    # Losowy wybór domeny
    domeny = ['gmail.com', 'outlook.com', 'yahoo.com', 'protonmail.com', 
              'firma.pl', 'firma.com', 'firma.eu', 'example.com']
    
    # Losowy format emaila dla różnorodności
    formaty_email = [
        f"{imie_email}.{nazwisko_email}",
        f"{imie_email[0]}.{nazwisko_email}",
        f"{imie_email}{nazwisko_email[0]}",
        f"{imie_email}_{nazwisko_email}",
        f"{nazwisko_email}.{imie_email}"
    ]
    
    email = f"{random.choice(formaty_email)}@{random.choice(domeny)}"
    
    return Wizytowka(imie, nazwisko, nazwa_firmy, stanowisko, email)

def generuj_liste_wizytowek(ilosc=10, lokalizacja='pl_PL'):
    """Generuje listę wizytówek."""
    return [generuj_wizytowke(lokalizacja) for _ in range(ilosc)]

def wyswietl_liste(tytul, lista_wizytowek):
    """Wyświetla listę wizytówek z podanym tytułem."""
    print(f"\n{tytul}:")
    print("=" * 60)
    for i, wizytowka in enumerate(lista_wizytowek, 1):
        print(f"{i:2}. {wizytowka}")
    print()

# Główny program
if __name__ == "__main__":
    # Generowanie listy wizytówek
    print("Generowanie losowych wizytówek...")
    lista_wizytowek = generuj_liste_wizytowek(8, 'pl_PL')
    
    # Wyświetlenie oryginalnej listy
    wyswietl_liste("Oryginalna lista wizytówek", lista_wizytowek)
    
    # Sortowanie według imienia
    posortowane_imie = sorted(lista_wizytowek, key=lambda w: w.imie)
    wyswietl_liste("Sortowanie według imienia", posortowane_imie)
    
    # Sortowanie według nazwiska
    posortowane_nazwisko = sorted(lista_wizytowek, key=lambda w: w.nazwisko)
    wyswietl_liste("Sortowanie według nazwiska", posortowane_nazwisko)
    
    # Sortowanie według adresu e-mail
    posortowane_email = sorted(lista_wizytowek, key=lambda w: w.email)
    wyswietl_liste("Sortowanie według adresu e-mail", posortowane_email)
    
    # Alternatywne podejście: sortowanie z użyciem atrybutu operator
    print("\n" + "="*60)
    print("Sortowanie z użyciem funkcji attrgetter:")
    print("="*60)
    
    from operator import attrgetter
    
    # Sortowanie według imienia i nazwiska (pierwsze imię, potem nazwisko)
    posortowane_imie_nazwisko = sorted(lista_wizytowek, key=attrgetter('imie', 'nazwisko'))
    wyswietl_liste("Sortowanie według imienia i nazwiska", posortowane_imie_nazwisko)
    
    # Dodatkowe informacje o każdej wizytówce
    print("\n" + "="*60)
    print("Pełne informacje o wizytówkach z posortowanej listy (według nazwiska):")
    print("="*60)
    
    for i, wizytowka in enumerate(posortowane_nazwisko, 1):
        print(f"\n{i}. {wizytowka}")
        print(f"   Firma: {wizytowka.nazwa_firmy}")
        print(f"   Stanowisko: {wizytowka.stanowisko}")
      