import logging

# Konfiguracja logowania DO PLIKU (jak w zadaniu)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    filename='kalkulator.log',
    filemode='a'
)

# Funkcje matematyczne - BARDZO PROSTE
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): 
    if b == 0:
        raise ValueError("Dzielenie przez zero")
    return a / b

# Słownik - KLUCZOWA ZMIANA mentora
operations = {
    "1": ("Dodawanie", add),
    "2": ("Odejmowanie", sub),
    "3": ("Mnożenie", mul),
    "4": ("Dzielenie", div)
}

def get_number(prompt):
    """Bezpieczne pobieranie liczby"""
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("To nie jest liczba!")

def get_data():
    """Pobiera tylko to co potrzebne"""
    print("\n" + "="*30)
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    
    while True:
        op = input("\nWybierz (1-4): ")
        if op in operations:
            break
        print("Błąd!")
    
    a = get_number("Pierwsza liczba: ")
    b = get_number("Druga liczba: ")
    
    return op, a, b

def main():
    """GŁÓWNA funkcja zgodnie z mentorem"""
    logging.info("Start kalkulatora")
    
    while True:
        try:
            op, a, b = get_data()
            name, func = operations[op]
            
            result = func(a, b)
            
            print(f"\n{name}: {a} i {b} = {result}")
            logging.info(f"{name}: {a} i {b} = {result}")
            
        except ValueError as e:
            print(f"\nBłąd: {e}")
            logging.error(f"Błąd: {e}")
        
        again = input("\nJeszcze raz? (t/n): ").lower()
        if again != 't':
            break
    
    logging.info("Koniec kalkulatora")
    print("Dziękuję!")

if __name__ == "__main__":
    main()
