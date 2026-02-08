warning: in the working copy of 'kalkulator/kalkulator_minimalny.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'kalkulator/kalkulator_rozszerzony.py', LF will be replaced by CRLF the next time Git touches it
[1mdiff --git a/kalkulator/kalkulator_minimalny.py b/kalkulator/kalkulator_minimalny.py[m
[1mindex f7bec7c..0b61e66 100644[m
[1m--- a/kalkulator/kalkulator_minimalny.py[m
[1m+++ b/kalkulator/kalkulator_minimalny.py[m
[36m@@ -7,39 +7,75 @@[m [mlogging.basicConfig([m
     datefmt='%H:%M:%S'[m
 )[m
 [m
[31m-print("KALKULATOR")[m
[31m-print("-" * 40)[m
[31m-[m
[31m-# Pytanie o działanie[m
[31m-print("Podaj działanie, posługując się odpowiednią liczbą:")[m
[31m-print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")[m
[31m-wybor = input("> ")[m
[31m-[m
[31m-# Pobieranie liczb[m
[31m-a = float(input("Podaj składnik 1: "))[m
[31m-b = float(input("Podaj składnik 2: "))[m
[31m-[m
[31m-# Logowanie i obliczenia[m
[31m-if wybor == '1':[m
[32m+[m[32m# Proste funkcje operacji[m
[32m+[m[32mdef add(a, b):[m
[32m+[m[32m    """Dodawanie"""[m
     logging.info(f"Dodaję {a:.2f} i {b:.2f}")[m
[31m-    wynik = a + b[m
[31m-    print(f"Wynik to {wynik:.2f}")[m
[31m-elif wybor == '2':[m
[32m+[m[32m    return a + b[m
[32m+[m
[32m+[m[32mdef sub(a, b):[m
[32m+[m[32m    """Odejmowanie"""[m
     logging.info(f"Odejmuję {b:.2f} od {a:.2f}")[m
[31m-    wynik = a - b[m
[31m-    print(f"Wynik to {wynik:.2f}")[m
[31m-elif wybor == '3':[m
[32m+[m[32m    return a - b[m
[32m+[m
[32m+[m[32mdef mul(a, b):[m
[32m+[m[32m    """Mnożenie"""[m
     logging.info(f"Mnożę {a:.2f} przez {b:.2f}")[m
[31m-    wynik = a * b[m
[31m-    print(f"Wynik to {wynik:.2f}")[m
[31m-elif wybor == '4':[m
[32m+[m[32m    return a * b[m
[32m+[m
[32m+[m[32mdef div(a, b):[m
[32m+[m[32m    """Dzielenie z zabezpieczeniem przed dzieleniem przez zero"""[m
     if b == 0:[m
         logging.error("Próba dzielenia przez zero!")[m
[31m-        print("Błąd: Nie można dzielić przez zero!")[m
[31m-    else:[m
[31m-        logging.info(f"Dzielę {a:.2f} przez {b:.2f}")[m
[31m-        wynik = a / b[m
[31m-        print(f"Wynik to {wynik:.2f}")[m
[31m-else:[m
[31m-    logging.warning(f"Nieprawidłowy wybór: {wybor}")[m
[31m-    print("Nieprawidłowy wybór działania!")[m
[32m+[m[32m        raise ValueError("Nie można dzielić przez zero!")[m
[32m+[m[32m    logging.info(f"Dzielę {a:.2f} przez {b:.2f}")[m
[32m+[m[32m    return a / b[m
[32m+[m
[32m+[m[32m# Słownik operacji - zgodnie z sugestią mentora[m
[32m+[m[32moperations = {[m
[32m+[m[32m    "1": ("Dodawanie", add),[m
[32m+[m[32m    "2": ("Odejmowanie", sub),[m
[32m+[m[32m    "3": ("Mnożenie", mul),[m
[32m+[m[32m    "4": ("Dzielenie", div)[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32mdef get_number(prompt):[m
[32m+[m[32m    """Bezpiecznie pobiera liczbę od użytkownika"""[m
[32m+[m[32m    while True:[m
[32m+[m[32m        try:[m
[32m+[m[32m            wejscie = input(prompt).strip().replace(',', '.')[m
[32m+[m[32m            return float(wejscie)[m
[32m+[m[32m        except ValueError:[m
[32m+[m[32m            print("Błąd! To nie jest prawidłowa liczba. Spróbuj ponownie.")[m
[32m+[m
[32m+[m[32mdef main():[m
[32m+[m[32m    """Główna funkcja kalkulatora"""[m
[32m+[m[32m    print("KALKULATOR")[m
[32m+[m[32m    print("-" * 40)[m
[32m+[m[41m    [m
[32m+[m[32m    # Wyświetl menu[m
[32m+[m[32m    print("Podaj działanie, posługując się odpowiednią liczbą:")[m
[32m+[m[32m    for key, (name, _) in operations.items():[m
[32m+[m[32m        print(f"{key} {name}")[m
[32m+[m[41m    [m
[32m+[m[32m    # Pobierz wybór[m
[32m+[m[32m    while True:[m
[32m+[m[32m        wybor = input("> ").strip()[m
[32m+[m[32m        if wybor in operations:[m
[32m+[m[32m            break[m
[32m+[m[32m        print("Nieprawidłowy wybór! Wybierz 1-4.")[m
[32m+[m[41m    [m
[32m+[m[32m    # Pobierz liczby[m
[32m+[m[32m    a = get_number("Podaj składnik 1: ")[m
[32m+[m[32m    b = get_number("Podaj składnik 2: ")[m
[32m+[m[41m    [m
[32m+[m[32m    # Wykonaj obliczenie[m
[32m+[m[32m    try:[m
[32m+[m[32m        operation_name, operation_func = operations[wybor][m
[32m+[m[32m        wynik = operation_func(a, b)[m
[32m+[m[32m        print(f"Wynik {operation_name.lower()} to {wynik:.2f}")[m
[32m+[m[32m    except ValueError as e:[m
[32m+[m[32m        print(f"Błąd: {e}")[m
[32m+[m
[32m+[m[32mif __name__ == "__main__":[m
[32m+[m[32m    main()[m
[1mdiff --git a/kalkulator/kalkulator_rozszerzony.py b/kalkulator/kalkulator_rozszerzony.py[m
[1mindex 6383bed..f63424f 100644[m
[1m--- a/kalkulator/kalkulator_rozszerzony.py[m
[1m+++ b/kalkulator/kalkulator_rozszerzony.py[m
[36m@@ -6,138 +6,144 @@[m [mlogging.basicConfig([m
     format='%(asctime)s - %(levelname)s - %(message)s',[m
     datefmt='%H:%M:%S',[m
     handlers=[[m
[31m-        logging.FileHandler('kalkulator_advanced.log', encoding='utf-8'),[m
[32m+[m[32m        logging.FileHandler('kalkulator_rozszerzony.log', encoding='utf-8'),[m
         logging.StreamHandler()[m
     ][m
 )[m
 [m
[32m+[m[32m# Proste funkcje operacji matematycznych[m
[32m+[m[32mdef add(a, b, *args):[m
[32m+[m[32m    """Dodawanie"""[m
[32m+[m[32m    result = a + b[m
[32m+[m[32m    for num in args:[m
[32m+[m[32m        result += num[m
[32m+[m[32m    logging.info(f"Dodawanie: {a} + {b}" + "".join(f" + {x}" for x in args) + f" = {result}")[m
[32m+[m[32m    return result[m
[32m+[m
[32m+[m[32mdef sub(a, b, *args):[m
[32m+[m[32m    """Odejmowanie"""[m
[32m+[m[32m    result = a - b[m
[32m+[m[32m    for num in args:[m
[32m+[m[32m        result -= num[m
[32m+[m[32m    logging.info(f"Odejmowanie: {a} - {b}" + "".join(f" - {x}" for x in args) + f" = {result}")[m
[32m+[m[32m    return result[m
[32m+[m
[32m+[m[32mdef mul(a, b, *args):[m
[32m+[m[32m    """Mnożenie"""[m
[32m+[m[32m    result = a * b[m
[32m+[m[32m    for num in args:[m
[32m+[m[32m        result *= num[m
[32m+[m[32m    logging.info(f"Mnożenie: {a} × {b}" + "".join(f" × {x}" for x in args) + f" = {result}")[m
[32m+[m[32m    return result[m
[32m+[m
[32m+[m[32mdef div(a, b, *args):[m
[32m+[m[32m    """Dzielenie z zabezpieczeniem przed dzieleniem przez zero"""[m
[32m+[m[32m    try:[m
[32m+[m[32m        if b == 0:[m
[32m+[m[32m            raise ValueError("Nie można dzielić przez zero!")[m
[32m+[m[32m        result = a / b[m
[32m+[m[41m        [m
[32m+[m[32m        for num in args:[m
[32m+[m[32m            if num == 0:[m
[32m+[m[32m                raise ValueError("Nie można dzielić przez zero!")[m
[32m+[m[32m            result /= num[m
[32m+[m[41m            [m
[32m+[m[32m        logging.info(f"Dzielenie: {a} / {b}" + "".join(f" / {x}" for x in args) + f" = {result}")[m
[32m+[m[32m        return result[m
[32m+[m[32m    except ValueError as e:[m
[32m+[m[32m        logging.error(f"Błąd dzielenia: {e}")[m
[32m+[m[32m        raise[m
[32m+[m
[32m+[m[32m# Słownik operacji - KLUCZOWA ZMIANA wg mentora[m
[32m+[m[32moperations = {[m
[32m+[m[32m    "1": ("➕ Dodawanie", add),[m
[32m+[m[32m    "2": ("➖ Odejmowanie", sub),[m
[32m+[m[32m    "3": ("✖️  Mnożenie", mul),[m
[32m+[m[32m    "4": ("➗ Dzielenie", div)[m
[32m+[m[32m}[m
[32m+[m
 def pobierz_liczbe(prompt):[m
     """Bezpiecznie pobiera liczbę od użytkownika"""[m
     while True:[m
         try:[m
             wejscie = input(prompt).strip().replace(',', '.')[m
[32m+[m[32m            if not wejscie:[m
[32m+[m[32m                raise ValueError("Puste wejście!")[m
             liczba = float(wejscie)[m
             logging.debug(f"Pobrano liczbę: {liczba}")[m
             return liczba[m
[31m-        except ValueError:[m
[31m-            print("Błąd! To nie jest prawidłowa liczba. Spróbuj ponownie.")[m
[31m-            logging.warning(f"Nieprawidłowe wejście użytkownika: '{wejscie}'")[m
[32m+[m[32m        except ValueError as e:[m
[32m+[m[32m            print(f"Błąd! {e} To nie jest prawidłowa liczba. Spróbuj ponownie.")[m
[32m+[m[32m            logging.warning(f"Nieprawidłowe wejście: '{wejscie}' - {e}")[m
 [m
[31m-def pobierz_wiele_liczb():[m
[31m-    """Pobiera wiele liczb od użytkownika"""[m
[31m-    liczby = [][m
[31m-    print("\nWprowadzaj liczby (wpisz 'koniec' aby zakończyć):")[m
[32m+[m[32mdef get_data():[m
[32m+[m[32m    """Pobiera dane od użytkownika"""[m
[32m+[m[32m    print("\n" + "="*50)[m
[32m+[m[32m    print("ZAawansowany KALKULATOR".center(50))[m
[32m+[m[32m    print("="*50)[m
     [m
[31m-    i = 1[m
[32m+[m[32m    for key, (name, _) in operations.items():[m
[32m+[m[32m        print(f"{key}. {name}")[m
[32m+[m[32m    print("5. 🚪 Wyjście")[m
[32m+[m[32m    print("="*50)[m
[32m+[m[41m    [m
[32m+[m[32m    # Pobierz wybór operacji[m
     while True:[m
[31m-        wejscie = input(f"Liczba {i}: ").strip().lower()[m
[31m-        if wejscie == 'koniec':[m
[32m+[m[32m        op = input("\nTwój wybór (1-5): ").strip()[m
[32m+[m[32m        if op == '5':[m
[32m+[m[32m            return None, None, None, None[m
[32m+[m[32m        if op in operations:[m
             break[m
[31m-        [m
[31m-        try:[m
[31m-            liczba = float(wejscie.replace(',', '.'))[m
[31m-            liczby.append(liczba)[m
[31m-            i += 1[m
[31m-        except ValueError:[m
[31m-            print("Nieprawidłowa liczba! Spróbuj ponownie lub wpisz 'koniec'.")[m
[32m+[m[32m        print("Nieprawidłowy wybór! Wybierz 1-5.")[m
[32m+[m[32m        logging.warning(f"Nieprawidłowy wybór: {op}")[m
[32m+[m[41m    [m
[32m+[m[32m    # Pobierz liczby[m
[32m+[m[32m    print(f"\n{operations[op][0]}")[m
[32m+[m[32m    print("Wprowadź co najmniej 2 liczby:")[m
[32m+[m[41m    [m
[32m+[m[32m    liczby = [][m
[32m+[m[32m    for i in range(1, 3):[m
[32m+[m[32m        liczba = pobierz_liczbe(f"Liczba {i}: ")[m
[32m+[m[32m        liczby.append(liczba)[m
     [m
[31m-    if len(liczby) < 2:[m
[31m-        print("Potrzeba co najmniej 2 liczby!")[m
[31m-        return None[m
[32m+[m[32m    # Opcjonalne dodatkowe liczby[m
[32m+[m[32m    i = 3[m
[32m+[m[32m    while True:[m
[32m+[m[32m        dodaj = input(f"Dodać kolejną liczbę? (t/n): ").strip().lower()[m
[32m+[m[32m        if dodaj != 't':[m
[32m+[m[32m            break[m
[32m+[m[32m        liczba = pobierz_liczbe(f"Liczba {i}: ")[m
[32m+[m[32m        liczby.append(liczba)[m
[32m+[m[32m        i += 1[m
     [m
[31m-    return liczby[m
[32m+[m[32m    return op, liczby[0], liczby[1], liczby[2:] if len(liczby) > 2 else ()[m
 [m
 def main():[m
[31m-    """Główna funkcja zaawansowanego kalkulatora"""[m
[32m+[m[32m    """Główna funkcja zgodna z sugestią mentora"""[m
     logging.info("Uruchomiono zaawansowany kalkulator")[m
     [m
     while True:[m
[31m-        print("\n" + "="*60)[m
[31m-        print("ZAawansowany KALKULATOR".center(60))[m
[31m-        print("="*60)[m
[31m-        print("1. ➕ Dodawanie (dowolna ilość liczb)")[m
[31m-        print("2. ➖ Odejmowanie (2 lub więcej liczb)")[m
[31m-        print("3. ✖️  Mnożenie (dowolna ilość liczb)")[m
[31m-        print("4. ➗ Dzielenie (2 lub więcej liczb)")[m
[31m-        print("5. 🚪 Wyjście")[m
[31m-        print("="*60)[m
[31m-        [m
[31m-        wybor = input("\nTwój wybór (1-5): ").strip()[m
[31m-        [m
[31m-        if wybor == '5':[m
[31m-            logging.info("Zamykanie zaawansowanego kalkulatora")[m
[31m-            print("\nDziękuję za skorzystanie z kalkulatora!")[m
[31m-            break[m
[31m-        [m
[31m-        if wybor not in ['1', '2', '3', '4']:[m
[31m-            print("Nieprawidłowy wybór! Wybierz 1-5.")[m
[31m-            logging.warning(f"Nieprawidłowy wybór: {wybor}")[m
[31m-            continue[m
[31m-        [m
[31m-        # Pobierz liczby w zależności od wyboru[m
[31m-        if wybor in ['1', '3']:  # Dodawanie i mnożenie - wiele liczb[m
[31m-            liczby = pobierz_wiele_liczb()[m
[31m-            if liczby is None:[m
[31m-                continue[m
[31m-        else:  # Odejmowanie i dzielenie - co najmniej 2 liczby[m
[31m-            print("\nWprowadź co najmniej 2 liczby:")[m
[31m-            liczby = [][m
[31m-            for i in range(1, 3):[m
[31m-                liczba = pobierz_liczbe(f"Liczba {i}: ")[m
[31m-                liczby.append(liczba)[m
[31m-            [m
[31m-            # Dodatkowe liczby[m
[31m-            i = 3[m
[31m-            while True:[m
[31m-                dodaj = input(f"Dodać kolejną liczbę? (t/n): ").strip().lower()[m
[31m-                if dodaj != 't':[m
[31m-                    break[m
[31m-                liczba = pobierz_liczbe(f"Liczba {i}: ")[m
[31m-                liczby.append(liczba)[m
[31m-                i += 1[m
[31m-        [m
[31m-        # Wykonaj działanie[m
         try:[m
[31m-            if wybor == '1':  # Dodawanie[m
[31m-                logging.info(f"Dodawanie: {' + '.join(f'{x:.2f}' for x in liczby)}")[m
[31m-                wynik = sum(liczby)[m
[31m-                dzialanie = "dodawania"[m
[31m-            elif wybor == '2':  # Odejmowanie[m
[31m-                logging.info(f"Odejmowanie: {liczby[0]:.2f} - {' - '.join(f'{x:.2f}' for x in liczby[1:])}")[m
[31m-                wynik = liczby[0][m
[31m-                for liczba in liczby[1:]:[m
[31m-                    wynik -= liczba[m
[31m-                dzialanie = "odejmowania"[m
[31m-            elif wybor == '3':  # Mnożenie[m
[31m-                logging.info(f"Mnożenie: {' × '.join(f'{x:.2f}' for x in liczby)}")[m
[31m-                wynik = 1[m
[31m-                for liczba in liczby:[m
[31m-                    wynik *= liczba[m
[31m-                dzialanie = "mnożenia"[m
[31m-            elif wybor == '4':  # Dzielenie[m
[31m-                # Sprawdź dzielenie przez zero[m
[31m-                wynik = 0  # Tymczasowa wartość[m
[31m-                for dzielnik in liczby[1:]:[m
[31m-                    if dzielnik == 0:[m
[31m-                        logging.error("Próba dzielenia przez zero!")[m
[31m-                        print("Błąd: Nie można dzielić przez zero!")[m
[31m-                        wynik = None[m
[31m-                        break[m
[31m-                [m
[31m-                if wynik is not None:[m
[31m-                    logging.info(f"Dzielenie: {liczby[0]:.2f} / {' / '.join(f'{x:.2f}' for x in liczby[1:])}")[m
[31m-                    wynik = liczby[0][m
[31m-                    for dzielnik in liczby[1:]:[m
[31m-                        wynik /= dzielnik[m
[31m-                    dzialanie = "dzielenia"[m
[32m+[m[32m            op, a, b, args = get_data()[m
             [m
[31m-            if wynik is not None:[m
[31m-                print(f"\n✅ Wynik {dzialanie} to: {wynik:.4f}")[m
[31m-                logging.info(f"Wyświetlono wynik: {wynik:.4f}")[m
[31m-        [m
[32m+[m[32m            if op is None:  # Wyjście[m
[32m+[m[32m                logging.info("Zamykanie kalkulatora")[m
[32m+[m[32m                print("\nDziękuję za skorzystanie z kalkulatora!")[m
[32m+[m[32m                break[m
[32m+[m[41m            [m
[32m+[m[32m            # Pobierz funkcję ze słownika i wykonaj[m
[32m+[m[32m            operation_name, operation_func = operations[op][m
[32m+[m[32m            result = operation_func(a, b, *args)[m
[32m+[m[41m            [m
[32m+[m[32m            print(f"\n✅ Wynik {operation_name.lower()} to: {result:.4f}")[m
[32m+[m[32m            logging.info(f"Wyświetlono wynik: {result:.4f}")[m
[32m+[m[41m            [m
[32m+[m[32m        except ValueError as e:[m
[32m+[m[32m            print(f"❌ {e}")[m
[32m+[m[32m            logging.error(f"Błąd: {e}")[m
         except Exception as e:[m
[3