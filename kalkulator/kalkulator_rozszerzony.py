import logging

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.FileHandler('kalkulator_advanced.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def pobierz_liczbe(prompt):
    """Bezpiecznie pobiera liczbę od użytkownika"""
    while True:
        try:
            wejscie = input(prompt).strip().replace(',', '.')
            liczba = float(wejscie)
            logging.debug(f"Pobrano liczbę: {liczba}")
            return liczba
        except ValueError:
            print("Błąd! To nie jest prawidłowa liczba. Spróbuj ponownie.")
            logging.warning(f"Nieprawidłowe wejście użytkownika: '{wejscie}'")

def pobierz_wiele_liczb():
    """Pobiera wiele liczb od użytkownika"""
    liczby = []
    print("\nWprowadzaj liczby (wpisz 'koniec' aby zakończyć):")
    
    i = 1
    while True:
        wejscie = input(f"Liczba {i}: ").strip().lower()
        if wejscie == 'koniec':
            break
        
        try:
            liczba = float(wejscie.replace(',', '.'))
            liczby.append(liczba)
            i += 1
        except ValueError:
            print("Nieprawidłowa liczba! Spróbuj ponownie lub wpisz 'koniec'.")
    
    if len(liczby) < 2:
        print("Potrzeba co najmniej 2 liczby!")
        return None
    
    return liczby

def main():
    """Główna funkcja zaawansowanego kalkulatora"""
    logging.info("Uruchomiono zaawansowany kalkulator")
    
    while True:
        print("\n" + "="*60)
        print("ZAawansowany KALKULATOR".center(60))
        print("="*60)
        print("1. ➕ Dodawanie (dowolna ilość liczb)")
        print("2. ➖ Odejmowanie (2 lub więcej liczb)")
        print("3. ✖️  Mnożenie (dowolna ilość liczb)")
        print("4. ➗ Dzielenie (2 lub więcej liczb)")
        print("5. 🚪 Wyjście")
        print("="*60)
        
        wybor = input("\nTwój wybór (1-5): ").strip()
        
        if wybor == '5':
            logging.info("Zamykanie zaawansowanego kalkulatora")
            print("\nDziękuję za skorzystanie z kalkulatora!")
            break
        
        if wybor not in ['1', '2', '3', '4']:
            print("Nieprawidłowy wybór! Wybierz 1-5.")
            logging.warning(f"Nieprawidłowy wybór: {wybor}")
            continue
        
        # Pobierz liczby w zależności od wyboru
        if wybor in ['1', '3']:  # Dodawanie i mnożenie - wiele liczb
            liczby = pobierz_wiele_liczb()
            if liczby is None:
                continue
        else:  # Odejmowanie i dzielenie - co najmniej 2 liczby
            print("\nWprowadź co najmniej 2 liczby:")
            liczby = []
            for i in range(1, 3):
                liczba = pobierz_liczbe(f"Liczba {i}: ")
                liczby.append(liczba)
            
            # Dodatkowe liczby
            i = 3
            while True:
                dodaj = input(f"Dodać kolejną liczbę? (t/n): ").strip().lower()
                if dodaj != 't':
                    break
                liczba = pobierz_liczbe(f"Liczba {i}: ")
                liczby.append(liczba)
                i += 1
        
        # Wykonaj działanie
        try:
            if wybor == '1':  # Dodawanie
                logging.info(f"Dodawanie: {' + '.join(f'{x:.2f}' for x in liczby)}")
                wynik = sum(liczby)
                dzialanie = "dodawania"
            elif wybor == '2':  # Odejmowanie
                logging.info(f"Odejmowanie: {liczby[0]:.2f} - {' - '.join(f'{x:.2f}' for x in liczby[1:])}")
                wynik = liczby[0]
                for liczba in liczby[1:]:
                    wynik -= liczba
                dzialanie = "odejmowania"
            elif wybor == '3':  # Mnożenie
                logging.info(f"Mnożenie: {' × '.join(f'{x:.2f}' for x in liczby)}")
                wynik = 1
                for liczba in liczby:
                    wynik *= liczba
                dzialanie = "mnożenia"
            elif wybor == '4':  # Dzielenie
                # Sprawdź dzielenie przez zero
                wynik = 0  # Tymczasowa wartość
                for dzielnik in liczby[1:]:
                    if dzielnik == 0:
                        logging.error("Próba dzielenia przez zero!")
                        print("Błąd: Nie można dzielić przez zero!")
                        wynik = None
                        break
                
                if wynik is not None:
                    logging.info(f"Dzielenie: {liczby[0]:.2f} / {' / '.join(f'{x:.2f}' for x in liczby[1:])}")
                    wynik = liczby[0]
                    for dzielnik in liczby[1:]:
                        wynik /= dzielnik
                    dzialanie = "dzielenia"
            
            if wynik is not None:
                print(f"\n✅ Wynik {dzialanie} to: {wynik:.4f}")
                logging.info(f"Wyświetlono wynik: {wynik:.4f}")
        
        except Exception as e:
            logging.error(f"Błąd podczas obliczeń: {e}", exc_info=True)
            print(f"❌ Wystąpił błąd: {e}")
        
        input("\n⏎ Naciśnij Enter, aby kontynuować...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Program przerwany przez użytkownika.")
        logging.info("Program przerwany przez użytkownika")
    except Exception as e:
        logging.critical(f"Krytyczny błąd: {e}", exc_info=True)
        print("💥 Wystąpił krytyczny błąd. Sprawdź plik logów.")
