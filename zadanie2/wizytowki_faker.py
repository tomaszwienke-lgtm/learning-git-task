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
    
    def contact(self):
        """Wyświetla informacje kontaktowe"""
        print(f"Kontaktuję się z {self.imie} {self.nazwisko}, {self.stanowisko}, email: {self.email}")
    
    @property
    def dlugosc_imienia_i_nazwiska(self):
        """Dynamiczny atrybut zwracający sumę długości imienia i nazwiska z spacją"""
        return len(self.imie) + 1 + len(self.nazwisko)
    
    @property
    def pelne_imie_i_nazwisko(self):
        """Dynamiczny atrybut zwracający pełne imię i nazwisko"""
        return f"{self.imie} {self.nazwisko}"

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

def demonstracja_wlasciwosci(wizytowka):
    """Demonstruje działanie dynamicznych właściwości"""
    print(f"\nDemonstracja właściwości dla: {wizytowka}")
    print(f"  Pełne imię i nazwisko: {wizytowka.pelne_imie_i_nazwisko}")
    print(f"  Długość imienia i nazwiska (ze spacją): {wizytowka.dlugosc_imienia_i_nazwiska}")
    print(f"  Czy mieści się w 25 znakach? {'TAK' if wizytowka.dlugosc_imienia_i_nazwiska <= 25 else 'NIE'}")
    print(f"  Czy mieści się w 20 znakach? {'TAK' if wizytowka.dlugosc_imienia_i_nazwiska <= 20 else 'NIE'}")
    print(f"  Czy mieści się w 15 znakach? {'TAK' if wizytowka.dlugosc_imienia_i_nazwiska <= 15 else 'NIE'}")

class KsiazkaAdresowa:
    def __init__(self):
        self.wizytowki = []
    
    def dodaj_wizytowke(self, wizytowka):
        """Dodaje wizytówkę do książki adresowej"""
        self.wizytowki.append(wizytowka)
        print(f"Dodano wizytówkę: {wizytowka}")
    
    def pokaz_wszystkie(self):
        """Wyświetla wszystkie wizytówki"""
        if not self.wizytowki:
            print("Książka adresowa jest pusta.")
            return
        
        print("\nWszystkie wizytówki w książce adresowej:")
        print("=" * 80)
        for i, wizytowka in enumerate(self.wizytowki, 1):
            print(f"{i:2}. {wizytowka}")
    
    def znajdz_przez_imie(self, imie):
        """Znajduje wizytówki po imieniu"""
        znalezione = [w for w in self.wizytowki if w.imie.lower() == imie.lower()]
        return znalezione
    
    def znajdz_przez_nazwisko(self, nazwisko):
        """Znajduje wizytówki po nazwisku"""
        znalezione = [w for w in self.wizytowki if w.nazwisko.lower() == nazwisko.lower()]
        return znalezione
    
    def znajdz_przez_stanowisko(self, stanowisko):
        """Znajduje wizytówki po stanowisku"""
        znalezione = [w for w in self.wizytowki if stanowisko.lower() in w.stanowisko.lower()]
        return znalezione
    
    def usun_wizytowke(self, indeks):
        """Usuwa wizytówkę o podanym indeksie"""
        if 0 <= indeks < len(self.wizytowki):
            usunieta = self.wizytowki.pop(indeks)
            print(f"Usunięto wizytówkę: {usunieta}")
            return usunieta
        else:
            print(f"Nieprawidłowy indeks: {indeks}")
            return None
    
    def sortuj_wedlug_dlugosci_nazwiska(self):
        """Sortuje wizytówki według długości imienia i nazwiska"""
        return sorted(self.wizytowki, key=lambda w: w.dlugosc_imienia_i_nazwiska)
    
    def pokaz_kontakty_z_krotkimi_nazwiskami(self, max_dlugosc=20):
        """Pokazuje kontakty, których imię i nazwisko mieszczą się w limicie znaków"""
        print(f"\nKontakty z imieniem i nazwiskiem mieszczącym się w {max_dlugosc} znakach:")
        print("=" * 80)
        znalezione = [w for w in self.wizytowki if w.dlugosc_imienia_i_nazwiska <= max_dlugosc]
        
        if not znalezione:
            print(f"Brak kontaktów z imieniem i nazwiskiem krótszym niż {max_dlugosc} znaków.")
        else:
            for i, wizytowka in enumerate(znalezione, 1):
                print(f"{i:2}. {wizytowka.pelne_imie_i_nazwisko} ({wizytowka.dlugosc_imienia_i_nazwiska} znaków)")
        return znalezione

def main():
    """Główna funkcja programu."""
    # Inicjalizacja
    fake = Faker('pl_PL')

    # Tworzenie książki adresowej
    ksiazka = KsiazkaAdresowa()

    # Dodawanie przykładowych wizytówek
    print("Tworzenie książki adresowej...")

    # Generowanie 5 wizytówek
    for _ in range(5):
        wizytowka = generuj_wizytowke('pl_PL')
        ksiazka.dodaj_wizytowke(wizytowka)

    print("\n" + "="*80)
    print("DEMONSTRACJA METODY contact():")
    print("="*80)

    # Demonstracja metody contact()
    print("\nPrzykładowe kontakty:")
    for i, wizytowka in enumerate(ksiazka.wizytowki[:3], 1):
        print(f"\n{i}. ", end="")
        wizytowka.contact()

    print("\n" + "="*80)
    print("DEMONSTRACJA DYNAMICZNEGO ATRYBUTU dlugosc_imienia_i_nazwiska:")
    print("="*80)

    # Demonstracja dynamicznego atrybutu
    for i, wizytowka in enumerate(ksiazka.wizytowki, 1):
        demonstracja_wlasciwosci(wizytowka)

    print("\n" + "="*80)
    print("ZASTOSOWANIA PRAKTYCZNE - ADRESOWANIE KOPERT:")
    print("="*80)

    # Praktyczne zastosowanie - adresowanie kopert
    print("\n1. Kontakty, które zmieszczą się na standardowej kopercie (max 25 znaków):")
    kontakty_25_znakow = ksiazka.pokaz_kontakty_z_krotkimi_nazwiskami(25)

    print("\n2. Kontakty, które zmieszczą się na małej kopercie (max 20 znaków):")
    kontakty_20_znakow = ksiazka.pokaz_kontakty_z_krotkimi_nazwiskami(20)

    print("\n3. Kontakty, które zmieszczą się na wąskiej etykiecie (max 15 znaków):")
    kontakty_15_znakow = ksiazka.pokaz_kontakty_z_krotkimi_nazwiskami(15)

    print("\n" + "="*80)
    print("SORTOWANIE WEDŁUG DŁUGOŚCI IMIENIA I NAZWISKA:")
    print("="*80)

    # Sortowanie według długości imienia i nazwiska
    posortowane = ksiazka.sortuj_wedlug_dlugosci_nazwiska()
    print("\nWizytówki posortowane według długości imienia i nazwiska:")
    for i, wizytowka in enumerate(posortowane, 1):
        print(f"{i:2}. {wizytowka.pelne_imie_i_nazwisko} ({wizytowka.dlugosc_imienia_i_nazwiska} znaków)")

    print("\n" + "="*80)
    print("DODATKOWE FUNKCJONALNOŚCI KSIAŻKI ADRESOWEJ:")
    print("="*80)

    # Demonstracja wyszukiwania
    print("\nWyszukiwanie kontaktów:")

    # Szukanie przez imię (pierwsze imię z listy)
    if ksiazka.wizytowki:
        pierwsze_imie = ksiazka.wizytowki[0].imie
        znalezione = ksiazka.znajdz_przez_imie(pierwsze_imie)
        print(f"\nKontakty o imieniu '{pierwsze_imie}':")
        for wizytowka in znalezione:
            print(f"  - {wizytowka}")

    # Szukanie przez stanowisko (zawierające słowo "manager")
    znalezione_manager = ksiazka.znajdz_przez_stanowisko("manager")
    if znalezione_manager:
        print(f"\nKontakty na stanowiskach menedżerskich:")
        for wizytowka in znalezione_manager:
            print(f"  - {wizytowka}, {wizytowka.stanowisko}")
    else:
        print("\nBrak kontaktów na stanowiskach menedżerskich.")

    # Przykład użycia - tworzenie etykiet adresowych
    print("\n" + "="*80)
    print("GENEROWANIE ETYKIET ADRESOWYCH:")
    print("="*80)

    print("\nEtykiety adresowe (format dla kopert):")
    print("-" * 40)
    for i, wizytowka in enumerate(ksiazka.wizytowki, 1):
        print(f"\nEtykieta {i}:")
        print("-" * 30)
        print(f"Do: {wizytowka.pelne_imie_i_nazwisko}")
        print(f"Długość pola 'Do': {wizytowka.dlugosc_imienia_i_nazwiska} znaków")
        print(f"Firma: {wizytowka.nazwa_firmy}")
        print(f"Stanowisko: {wizytowka.stanowisko}")

    # Dodanie specjalnej wizytówki z bardzo długim imieniem i nazwiskiem
    print("\n" + "="*80)
    print("TEST Z DŁUGIM IMIENIEM I NAZWISKIEM:")
    print("="*80)

    dluga_wizytowka = Wizytowka(
        "Katarzyna-Joanna-Maria",
        "Nowakowska-Wiśniewska-Kowalska",
        "MegaCorp International",
        "Senior Vice President of Global Operations",
        "k.j.m.nowakowska-wisniewska-kowalska@megacorp.com"
    )

    ksiazka.dodaj_wizytowke(dluga_wizytowka)
    demonstracja_wlasciwosci(dluga_wizytowka)
    print("\n", end="")
    dluga_wizytowka.contact()

if __name__ == "__main__":
    main()
