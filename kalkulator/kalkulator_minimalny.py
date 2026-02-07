import logging

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)

# Proste funkcje operacji
def add(a, b):
    """Dodawanie"""
    logging.info(f"Dodaję {a:.2f} i {b:.2f}")
    return a + b

def sub(a, b):
    """Odejmowanie"""
    logging.info(f"Odejmuję {b:.2f} od {a:.2f}")
    return a - b

def mul(a, b):
    """Mnożenie"""
    logging.info(f"Mnożę {a:.2f} przez {b:.2f}")
    return a * b

def div(a, b):
    """Dzielenie z zabezpieczeniem przed dzieleniem przez zero"""
    if b == 0:
        logging.error("Próba dzielenia przez zero!")
        raise ValueError("Nie można dzielić przez zero!")
    logging.info(f"Dzielę {a:.2f} przez {b:.2f}")
    return a / b

# Słownik operacji - zgodnie z sugestią mentora
operations = {
    "1": ("Dodawanie", add),
    "2": ("Odejmowanie", sub),
    "3": ("Mnożenie", mul),
    "4": ("Dzielenie", div)
}

def get_number(prompt):
    """Bezpiecznie pobiera liczbę od użytkownika"""
    while True:
        try:
            wejscie = input(prompt).strip().replace(',', '.')
            return float(wejscie)
        except ValueError:
            print("Błąd! To nie jest prawidłowa liczba. Spróbuj ponownie.")

def main():
    """Główna funkcja kalkulatora"""
    print("KALKULATOR")
    print("-" * 40)
    
    # Wyświetl menu
    print("Podaj działanie, posługując się odpowiednią liczbą:")
    for key, (name, _) in operations.items():
        print(f"{key} {name}")
    
    # Pobierz wybór
    while True:
        wybor = input("> ").strip()
        if wybor in operations:
            break
        print("Nieprawidłowy wybór! Wybierz 1-4.")
    
    # Pobierz liczby
    a = get_number("Podaj składnik 1: ")
    b = get_number("Podaj składnik 2: ")
    
    # Wykonaj obliczenie
    try:
        operation_name, operation_func = operations[wybor]
        wynik = operation_func(a, b)
        print(f"Wynik {operation_name.lower()} to {wynik:.2f}")
    except ValueError as e:
        print(f"Błąd: {e}")

if __name__ == "__main__":
    main()
