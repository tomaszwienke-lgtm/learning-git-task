from faker import Faker
import random
from operator import attrgetter

class BaseContact:
    """Klasa bazowa dla wizytówki z podstawowymi danymi kontaktowymi."""
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
    
    def __str__(self):
        """Reprezentacja string obiektu: imię, nazwisko i email."""
        return f"{self.imie} {self.nazwisko} - {self.email}"
    
    @property
    def label_length(self):
        """Dynamiczny atrybut zwracający sumę długości imienia i nazwiska z spacją."""
        return len(self.imie) + 1 + len(self.nazwisko)
    
    def contact(self):
        """Wyświetla komunikat o kontakcie prywatnym."""
        return f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}"

class BusinessContact(BaseContact):
    """Klasa rozszerzająca BaseContact o dane służbowe."""
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy
    
    def __str__(self):
        """Reprezentacja string obiektu z danymi biznesowymi."""
        return f"{self.imie} {self.nazwisko} ({self.stanowisko} w {self.firma}) - {self.email}"
    
    def contact(self):
        """Wyświetla komunikat o kontakcie służbowym."""
        return f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}"

def create_contacts(rodzaj, ilosc, lokalizacja='pl_PL'):
    """
    Tworzy listę losowych wizytówek.
    
    Args:
        rodzaj (str): 'base' dla BaseContact, 'business' dla BusinessContact
        ilosc (int): liczba wizytówek do wygenerowania
        lokalizacja (str): lokalizacja dla Faker (domyślnie 'pl_PL')
    
    Returns:
        list: Lista wizytówek
    """
    fake = Faker(lokalizacja)
    wizytowki = []
    
    for _ in range(ilosc):
        # Podstawowe dane wspólne dla obu typów
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        
        # Przygotowanie imienia i nazwiska dla emaila
        imie_email = imie.lower().replace('ą', 'a').replace('ć', 'c').replace('ę', 'e')\
                          .replace('ł', 'l').replace('ń', 'n').replace('ó', 'o')\
                          .replace('ś', 's').replace('ź', 'z').replace('ż', 'z')
        nazwisko_email = nazwisko.lower().replace('ą', 'a').replace('ć', 'c').replace('ę', 'e')\
                               .replace('ł', 'l').replace('ń', 'n').replace('ó', 'o')\
                               .replace('ś', 's').replace('ź', 'z').replace('ż', 'z')
        
        # Losowy format emaila
        formaty_email = [
            f"{imie_email}.{nazwisko_email}",
            f"{imie_email[0]}.{nazwisko_email}",
            f"{imie_email}{nazwisko_email[0]}",
            f"{imie_email}_{nazwisko_email}",
            f"{nazwisko_email}.{imie_email}"
        ]
        
        # Losowa domena
        domeny = ['gmail.com', 'outlook.com', 'yahoo.com', 'protonmail.com', 
                  'firma.pl', 'firma.com', 'firma.eu', 'example.com']
        
        email = f"{random.choice(formaty_email)}@{random.choice(domeny)}"
        
        if rodzaj.lower() == 'base':
            wizytowka = BaseContact(imie, nazwisko, telefon, email)
        elif rodzaj.lower() == 'business':
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            wizytowka = BusinessContact(imie, nazwisko, telefon, email, 
                                        stanowisko, firma, telefon_sluzbowy)
        else:
            raise ValueError("Rodzaj musi być 'base' lub 'business'")
        
        wizytowki.append(wizytowka)
    
    return wizytowki

def wyswietl_liste(tytul, lista_wizytowek):
    """Wyświetla listę wizytówek z podanym tytułem."""
    print(f"\n{tytul}:")
    print("=" * 70)
    for i, wizytowka in enumerate(lista_wizytowek, 1):
        print(f"{i:2}. {wizytowka}")
        print(f"   Długość etykiety: {wizytowka.label_length} znaków")
    print()

def demonstracja_kontaktu(wizytowki):
    """Demonstruje działanie metody contact() dla różnych typów wizytówek."""
    print("\nDEMONSTRACJA METODY contact():")
    print("-" * 70)
    
    for i, wizytowka in enumerate(wizytowki, 1):
        print(f"{i}. {type(wizytowka).__name__}:")
        print(f"   {wizytowka.contact()}")
        print()

class KsiazkaAdresowa:
    """Klasa do zarządzania książką adresową."""
    def __init__(self):
        self.wizytowki = []
    
    def dodaj_wizytowke(self, wizytowka):
        """Dodaje wizytówkę do książki adresowej."""
        self.wizytowki.append(wizytowka)
        print(f"Dodano wizytówkę: {wizytowka}")
    
    def dodaj_wiele_wizytowek(self, lista_wizytowek):
        """Dodaje wiele wizytówek na raz."""
        self.wizytowki.extend(lista_wizytowek)
        print(f"Dodano {len(lista_wizytowek)} wizytówek.")
    
    def pokaz_wszystkie(self):
        """Wyświetla wszystkie wizytówki."""
        if not self.wizytowki:
            print("Książka adresowa jest pusta.")
            return
        
        print("\nWszystkie wizytówki w książce adresowej:")
        print("=" * 70)
        for i, wizytowka in enumerate(self.wizytowki, 1):
            print(f"{i:2}. {wizytowka}")
    
    def znajdz_przez_imie(self, imie):
        """Znajduje wizytówki po imieniu."""
        return [w for w in self.wizytowki if w.imie.lower() == imie.lower()]
    
    def znajdz_przez_nazwisko(self, nazwisko):
        """Znajduje wizytówki po nazwisku."""
        return [w for w in self.wizytowki if w.nazwisko.lower() == nazwisko.lower()]
    
    def pokaz_kontakty_z_krotkimi_nazwiskami(self, max_dlugosc=20):
        """Pokazuje kontakty, których imię i nazwisko mieszczą się w limicie znaków."""
        znalezione = [w for w in self.wizytowki if w.label_length <= max_dlugosc]
        
        if not znalezione:
            print(f"Brak kontaktów z imieniem i nazwiskiem krótszym niż {max_dlugosc} znaków.")
        else:
            print(f"\nKontakty z imieniem i nazwiskiem mieszczącym się w {max_dlugosc} znakach:")
            print("-" * 50)
            for i, wizytowka in enumerate(znalezione, 1):
                print(f"{i:2}. {wizytowka.imie} {wizytowka.nazwisko} ({wizytowka.label_length} znaków)")
        
        return znalezione

def sortuj_wizytowki(lista_wizytowek, kryterium):
    """
    Sortuje listę wizytówek według podanego kryterium.
    
    Args:
        lista_wizytowek: Lista wizytówek do sortowania
        kryterium: 'imie', 'nazwisko' lub 'email'
    
    Returns:
        Posortowana lista
    """
    if kryterium == 'imie':
        return sorted(lista_wizytowek, key=lambda w: w.imie)
    elif kryterium == 'nazwisko':
        return sorted(lista_wizytowek, key=lambda w: w.nazwisko)
    elif kryterium == 'email':
        return sorted(lista_wizytowek, key=lambda w: w.email)
    elif kryterium == 'label_length':
        return sorted(lista_wizytowek, key=lambda w: w.label_length)
    else:
        raise ValueError("Nieprawidłowe kryterium sortowania")

def generuj_etykiety_adresowe(lista_wizytowek):
    """Generuje etykiety adresowe dla listy wizytówek."""
    print("\nETYKIETY ADRESOWE (format dla kopert):")
    print("=" * 60)
    
    for i, wizytowka in enumerate(lista_wizytowek, 1):
        print(f"\nEtykieta {i}:")
        print("-" * 40)
        print(f"Do: {wizytowka.imie} {wizytowka.nazwisko}")
        print(f"Długość pola 'Do': {wizytowka.label_length} znaków")
        
        if isinstance(wizytowka, BusinessContact):
            print(f"Firma: {wizytowka.firma}")
            print(f"Stanowisko: {wizytowka.stanowisko}")
        
        print(f"Email: {wizytowka.email}")

def main():
    """Główna funkcja programu."""
    print("PROGRAM DO OBSŁUGI WIZYTÓWEK")
    print("=" * 70)
    
    # Inicjalizacja książki adresowej
    ksiazka = KsiazkaAdresowa()
    
    # Tworzenie przykładowych wizytówek
    print("\nTworzenie przykładowych wizytówek...")
    
    # Generowanie 3 wizytówek podstawowych
    wizytowki_base = create_contacts('base', 3)
    ksiazka.dodaj_wiele_wizytowek(wizytowki_base)
    
    # Generowanie 3 wizytówek biznesowych
    wizytowki_business = create_contacts('business', 3)
    ksiazka.dodaj_wiele_wizytowek(wizytowki_business)
    
    # Wyświetlanie wszystkich wizytówek
    ksiazka.pokaz_wszystkie()
    
    # Demonstracja metody contact()
    demonstracja_kontaktu(ksiazka.wizytowki)
    
    # Sortowanie i wyświetlanie
    print("\nSORTOWANIE WIZYTÓWEK:")
    print("=" * 70)
    
    # Sortowanie według imienia
    posortowane_imie = sortuj_wizytowki(ksiazka.wizytowki, 'imie')
    wyswietl_liste("Sortowanie według imienia", posortowane_imie)
    
    # Sortowanie według nazwiska
    posortowane_nazwisko = sortuj_wizytowki(ksiazka.wizytowki, 'nazwisko')
    wyswietl_liste("Sortowanie według nazwiska", posortowane_nazwisko)
    
    # Sortowanie według email
    posortowane_email = sortuj_wizytowki(ksiazka.wizytowki, 'email')
    wyswietl_liste("Sortowanie według adresu e-mail", posortowane_email)
    
    # Sortowanie według długości etykiety
    posortowane_label = sortuj_wizytowki(ksiazka.wizytowki, 'label_length')
    wyswietl_liste("Sortowanie według długości etykiety", posortowane_label)
    
    # Alternatywne sortowanie z użyciem attrgetter
    print("\nSORTOWANIE Z UŻYCIEM ATTRGETTER:")
    print("-" * 70)
    posortowane_imie_nazwisko = sorted(ksiazka.wizytowki, key=attrgetter('imie', 'nazwisko'))
    wyswietl_liste("Sortowanie według imienia i nazwiska", posortowane_imie_nazwisko)
    
    # Wyświetlanie wizytówek z krótkimi nazwiskami
    print("\nPRAKTYCZNE ZASTOSOWANIE - ADRESOWANIE KOPERT:")
    print("=" * 70)
    
    ksiazka.pokaz_kontakty_z_krotkimi_nazwiskami(25)
    ksiazka.pokaz_kontakty_z_krotkimi_nazwiskami(20)
    ksiazka.pokaz_kontakty_z_krotkimi_nazwiskami(15)
    
    # Generowanie etykiet adresowych
    generuj_etykiety_adresowe(ksiazka.wizytowki[:3])
    
    # Dodanie specjalnej wizytówki z bardzo długim imieniem i nazwiskiem
    print("\n" + "=" * 70)
    print("TEST Z DŁUGIM IMIENIEM I NAZWISKIEM:")
    print("=" * 70)
    
    dluga_wizytowka = BusinessContact(
        "Katarzyna-Joanna-Maria", 
        "Nowakowska-Wiśniewska-Kowalska", 
        "+48 123 456 789",
        "k.j.m.nowakowska-wisniewska-kowalska@megacorp.com",
        "Senior Vice President of Global Operations",
        "MegaCorp International",
        "+48 987 654 321"
    )
    
    ksiazka.dodaj_wizytowke(dluga_wizytowka)
    print(f"\n{type(dluga_wizytowka).__name__}:")
    print(f"  {dluga_wizytowka}")
    print(f"  Długość etykiety: {dluga_wizytowka.label_length} znaków")
    print(f"  Kontakt: {dluga_wizytowka.contact()}")
    
    # Statystyki
    print("\n" + "=" * 70)
    print("STATYSTYKI:")
    print("=" * 70)
    
    liczba_base = sum(1 for w in ksiazka.wizytowki if isinstance(w, BaseContact) and not isinstance(w, BusinessContact))
    liczba_business = sum(1 for w in ksiazka.wizytowki if isinstance(w, BusinessContact))
    
    print(f"Liczba wizytówek podstawowych: {liczba_base}")
    print(f"Liczba wizytówek biznesowych: {liczba_business}")
    print(f"Łączna liczba wizytówek: {len(ksiazka.wizytowki)}")
    
    if ksiazka.wizytowki:
        srednia_label = sum(w.label_length for w in ksiazka.wizytowki) / len(ksiazka.wizytowki)
        print(f"Średnia długość etykiety: {srednia_label:.1f} znaków")
    
        # Najkrótsza i najdłuższa etykieta
        najkrotsza = min(ksiazka.wizytowki, key=lambda w: w.label_length)
        najdluzsza = max(ksiazka.wizytowki, key=lambda w: w.label_length)
        print(f"Najkrótsza etykieta: {najkrotsza.imie} {najkrotsza.nazwisko} ({najkrotsza.label_length} znaków)")
        print(f"Najdłuższa etykieta: {najdluzsza.imie} {najdluzsza.nazwisko} ({najdluzsza.label_length} znaków)")

if __name__ == "__main__":
    main()
