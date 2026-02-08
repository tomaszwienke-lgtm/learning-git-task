"""
Business Cards Manager - Główny program
Wybierz, które zadanie chcesz uruchomić.
"""

import sys
import os

def display_menu():
    print("=" * 50)
    print("BUSINESS CARDS MANAGER")
    print("=" * 50)
    print("\nWybierz zadanie do uruchomienia:")
    print("1. Zadanie 1 - Podstawowa klasa wizytówki")
    print("2. Zadanie 2 - Rozszerzona klasa z Faker")
    print("3. Zadanie 3 - Dziedziczenie klas")
    print("4. Wyjście")
    print()

def main():
    while True:
        display_menu()
        choice = input("Twój wybór (1-4): ").strip()
        
        if choice == "1":
            print("\nUruchamiam Zadanie 1...")
            from zadanie1 import wizytowki_basic
            if hasattr(wizytowki_basic, 'main'):
                wizytowki_basic.main()
            else:
                print("Uruchom plik bezpośrednio: python zadanie1/wizytowki_basic.py")
            
        elif choice == "2":
            print("\nUruchamiam Zadanie 2...")
            from zadanie2 import wizytowki_faker
            if hasattr(wizytowki_faker, 'main'):
                wizytowki_faker.main()
            else:
                print("Uruchom plik bezpośrednio: python zadanie2/wizytowki_faker.py")
            
        elif choice == "3":
            print("\nUruchamiam Zadanie 3...")
            from zadanie3 import wizytowki_dziedziczenie
            if hasattr(wizytowki_dziedziczenie, 'main'):
                wizytowki_dziedziczenie.main()
            else:
                print("Uruchom plik bezpośrednio: python zadanie3/wizytowki_dziedziczenie.py")
            
        elif choice == "4":
            print("\nDziękuję za skorzystanie z programu!")
            sys.exit(0)
            
        else:
            print("\nNieprawidłowy wybór.")
        
        input("\nNaciśnij Enter, aby kontynuować...")

if __name__ == "__main__":
    main()
