"""
Program do sprawdzania palindromów.
Palindrom to słowo, które czytane od przodu i od tyłu brzmi tak samo.
"""

def czy_palindrom(tekst):
    """
    Sprawdza, czy podany tekst jest palindromem.
    """
    # Usuwamy białe znaki i zamieniamy na małe litery
    tekst_przygotowany = tekst.replace(" ", "").lower()
    
    # Sprawdzamy czy tekst od przodu jest taki sam jak od tyłu
    return tekst_przygotowany == tekst_przygotowany[::-1]


def main():
    """Główna funkcja programu."""
    print("=" * 50)
    print("SPRAWDZANIE PALINDROMÓW")
    print("=" * 50)
    
    # Testy
    testowe_slowa = ["kajak", "potop", "anna", "python", "A to idiota"]
    
    for slowo in testowe_slowa:
        if czy_palindrom(slowo):
            print(f"✓ '{slowo}' JEST palindromem")
        else:
            print(f"✗ '{slowo}' NIE JEST palindromem")
    
    # Tryb interaktywny
    print("\n" + "=" * 50)
    print("TRYB INTERAKTYWNY (wpisz 'q' aby wyjść)")
    print("=" * 50)
    
    while True:
        tekst = input("\nWprowadź tekst do sprawdzenia: ")
        
        if tekst.lower() == 'q':
            print("Do zobaczenia!")
            break
        
        if czy_palindrom(tekst):
            print(f"✓ '{tekst}' JEST palindromem!")
        else:
            print(f"✗ '{tekst}' NIE JEST palindromem.")


if __name__ == "__main__":
    main()

