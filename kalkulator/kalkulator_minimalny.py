import logging

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)

print("KALKULATOR")
print("-" * 40)

# Pytanie o działanie
print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")
wybor = input("> ")

# Pobieranie liczb
a = float(input("Podaj składnik 1: "))
b = float(input("Podaj składnik 2: "))

# Logowanie i obliczenia
if wybor == '1':
    logging.info(f"Dodaję {a:.2f} i {b:.2f}")
    wynik = a + b
    print(f"Wynik to {wynik:.2f}")
elif wybor == '2':
    logging.info(f"Odejmuję {b:.2f} od {a:.2f}")
    wynik = a - b
    print(f"Wynik to {wynik:.2f}")
elif wybor == '3':
    logging.info(f"Mnożę {a:.2f} przez {b:.2f}")
    wynik = a * b
    print(f"Wynik to {wynik:.2f}")
elif wybor == '4':
    if b == 0:
        logging.error("Próba dzielenia przez zero!")
        print("Błąd: Nie można dzielić przez zero!")
    else:
        logging.info(f"Dzielę {a:.2f} przez {b:.2f}")
        wynik = a / b
        print(f"Wynik to {wynik:.2f}")
else:
    logging.warning(f"Nieprawidłowy wybór: {wybor}")
    print("Nieprawidłowy wybór działania!")
