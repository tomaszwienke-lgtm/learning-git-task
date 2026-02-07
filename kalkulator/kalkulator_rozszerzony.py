import logging

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.FileHandler('kalkulator_rozszerzony.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Proste funkcje operacji matematycznych
def add(a, b, *args):
    """Dodawanie"""
    result = a + b
    for num in args:
        result += num
    logging.info(f"Dodawanie: {a} + {b}" + "".join(f" + {x}" for x in args) + f" = {result}")
    return result

def sub(a, b, *args):
    """Odejmowanie"""
    result = a - b
    for num in args:
        result -= num
    logging.info(f"Odejmowanie: {a} - {b}" + "".join(f" - {x}" for x in args) + f" = {result}")
    return result

def mul(a, b, *args):
    """Mnożenie"""
    result = a * b
    for num in args:
        result *= num
    logging.info(f"Mnożenie: {a} × {b}" + "".join(f" × {x}" for x in args) + f" = {result}")
    return result

def div(a, b, *args):
    """Dzielenie z zabezpieczeniem przed dzieleniem przez zero"""
    try:
        if b == 0:
            raise ValueError("Nie można dzielić przez zero!")
        result = a / b
        
        for num in args:
            if num == 0:
                raise ValueError("Nie można dzielić przez zero!")
            result /= num
            
        logging.info(f"Dzielenie: {a} / {b}" + "".join(f" / {x}" for x in args) + f" = {result}")
        return result
    except ValueError as e:
        logging.error(f"Błąd dzielenia: {e}")
        raise

# Słownik operacji - KLUCZOWA ZMIANA wg mentora
operations = {
    "1": ("➕ Dodawanie", add),
    "2": ("➖ Odejmowanie", sub),
    "3": ("✖️  Mnożenie", mul),
    "4": ("➗ Dzielenie", div)
}

def pobierz_liczbe(prompt):
    """Bezpiecznie pobiera liczbę od użytkownika"""
    while True:
        try:
            wejscie = input(prompt).strip().replace(',', '.')
            if not wejscie:
                raise ValueError("Puste wejście!")
            liczba = float(wejscie)
            logging.debug(f"Pobrano liczbę: {liczba}")
            return liczba
        except ValueError as e:
            print(f"Błąd! {e} To nie jest prawidłowa liczba. Spróbuj ponownie.")
            logging.warning(f"Nieprawidłowe wejście: '{wejscie}' - {e}")

def get_data():
    """Pobiera dane od użytkownika"""
    print("\n" + "="*50)
    print("ZAawansowany KALKULATOR".center(50))
    print("="*50)
    
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("5. 🚪 Wyjście")
    print("="*50)
    
    # Pobierz wybór operacji
    while True:
        op = input("\nTwój wybór (1-5): ").strip()
        if op == '5':
            return None, None, None, None
        if op in operations:
            break
        print("Nieprawidłowy wybór! Wybierz 1-5.")
        logging.warning(f"Nieprawidłowy wybór: {op}")
    
    # Pobierz liczby
    print(f"\n{operations[op][0]}")
    print("Wprowadź co najmniej 2 liczby:")
    
    liczby = []
    for i in range(1, 3):
        liczba = pobierz_liczbe(f"Liczba {i}: ")
        liczby.append(liczba)
    
    # Opcjonalne dodatkowe liczby
    i = 3
    while True:
        dodaj = input(f"Dodać kolejną liczbę? (t/n): ").strip().lower()
        if dodaj != 't':
            break
        liczba = pobierz_liczbe(f"Liczba {i}: ")
        liczby.append(liczba)
        i += 1
    
    return op, liczby[0], liczby[1], liczby[2:] if len(liczby) > 2 else ()

def main():
    """Główna funkcja zgodna z sugestią mentora"""
    logging.info("Uruchomiono zaawansowany kalkulator")
    
    while True:
        try:
            op, a, b, args = get_data()
            
            if op is None:  # Wyjście
                logging.info("Zamykanie kalkulatora")
                print("\nDziękuję za skorzystanie z kalkulatora!")
                break
            
            # Pobierz funkcję ze słownika i wykonaj
            operation_name, operation_func = operations[op]
            result = operation_func(a, b, *args)
            
            print(f"\n✅ Wynik {operation_name.lower()} to: {result:.4f}")
            logging.info(f"Wyświetlono wynik: {result:.4f}")
            
        except ValueError as e:
            print(f"❌ {e}")
            logging.error(f"Błąd: {e}")
        except Exception as e:
            print(f"❌ Wystąpił nieoczekiwany błąd: {e}")
            logging.error(f"Nieoczekiwany błąd: {e}", exc_info=True)
        
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
