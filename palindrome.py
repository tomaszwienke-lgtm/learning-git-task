"""
Zadanie: Palindromy
Funkcja sprawdzająca czy tekst jest palindromem.
Palindrom to słowo czytane tak samo od przodu i od tyłu.
Autor: Tomasz Wienke
"""

def is_palindrome(text):
    """
    Sprawdza, czy podany tekst jest palindromem.
    
    Algorytm zgodny z sugestią mentora:
    1. Zbiera tylko litery i cyfry (ignoruje znaki specjalne)
    2. Porównuje z odwróconą wersją
    
    Args:
        text (str): Tekst do sprawdzenia
        
    Returns:
        bool: True jeśli tekst jest palindromem
    """
    znaki = []
    for znak in text:
        if znak.isalnum():
            znaki.append(znak.lower())
    
    return znaki == znaki[::-1]


# Testy wymagane w zadaniu
if __name__ == "__main__":
    print("Testowanie funkcji is_palindrome:")
    print("=" * 40)
    
    # Test 1: Przykłady z zadania
    print("\n1. Przykłady z treści zadania:")
    print(f"   'kajak' -> {is_palindrome('kajak')}")      # True
    print(f"   'potop' -> {is_palindrome('potop')}")      # True
    
    # Test 2: Dodatkowe przykłady
    print("\n2. Dodatkowe testy:")
    print(f"   'anna' -> {is_palindrome('anna')}")        # True
    print(f"   'python' -> {is_palindrome('python')}")    # False
    
    # Test 3: Ze znakami specjalnymi (ignorowane zgodnie z algorytmem mentora)
    print("\n3. Testy ze znakami specjalnymi:")
    print(f"   'A to idiota!' -> {is_palindrome('A to idiota!')}")  # True
    print(f"   'Kajak!' -> {is_palindrome('Kajak!')}")              # True
    
    # Test 4: Interaktywny tryb
    print("\n" + "=" * 40)
    print("4. Tryb interaktywny (wpisz 'q' aby wyjść):")
    
    while True:
        user_input = input("\nWpisz tekst do sprawdzenia: ")
        if user_input.lower() == 'q':
            print("Koniec programu.")
            break
        
        result = is_palindrome(user_input)
        if result:
            print(f"✅ '{user_input}' JEST palindromem")
        else:
            print(f"❌ '{user_input}' NIE JEST palindromem")
