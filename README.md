# Sales Dashboard – analiza kanałów sprzedaży

Dashboard interaktywny w Pythonie (Dash, Plotly) do analizy sprzedaży sieci sklepów detalicznych. Zawiera trzy zakładki: Sprzedaż globalna, Produkty, Kanały sprzedaży.

## Wymagane biblioteki
- dash
- plotly
- pandas

## Uruchomienie
1. Sklonuj repozytorium i przełącz się na gałąź `zadanie-kanaly-sprzedazy`.
2. Zainstaluj zależności: `pip install dash plotly pandas`.
3. Uruchom aplikację: `python app.py`.
4. Otwórz w przeglądarce adres `http://127.0.0.1:8050/`.

## Walidacja danych
- Usunięto duplikaty transakcji (934 wiersze).
- Sprawdzono brakujące wartości i zakresy dat.

## Struktura
- `app.py` – główny plik aplikacji
- `modules/` – moduły z funkcjami pomocniczymi
- `tabs/` – layouty poszczególnych zakładek
- `db/` – dane źródłowe (transakcje, klienci, kategorie, kraje)

## Autor
[Tomasz W.]
