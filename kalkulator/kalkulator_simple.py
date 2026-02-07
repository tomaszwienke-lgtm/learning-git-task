import logging

# Konfiguracja logowania (minimalna)
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)

# Proste funkcje - TYLKO logika
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero")
    return a / b

# Słownik zgodnie z mentorem
operations = {
    "1": add,
    "2": sub,
    "3": mul,
    "4": div
}

def get_data():
    """Proste pobieranie danych"""
    print("\nWybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    
    while True:
        op = input("Twój wybór (1-4): ").strip()
        if op in operations:
            break
        print("Nieprawidłowy wybór!")
    
    a = float(input("Podaj pierwszą liczbę: ").replace(',', '.'))
    b = float(input("Podaj drugą liczbę: ").replace(',', '.'))
    
    return op, a, b

def main():
    """Zgodnie z mentorem: op, a, b = get_data() + wywołanie"""
    print("=== PROSTY KALKULATOR ===")
    
    op, a, b = get_data()
    
    try:
        result = operations[op](a, b)
        logging.info(f"Operacja {op}: {a} i {b} = {result}")
        print(f"Wynik: {result}")
    except ValueError as e:
        print(f"Błąd: {e}")
        logging.error(f"Błąd: {e}")

if __name__ == "__main__":
    main()
