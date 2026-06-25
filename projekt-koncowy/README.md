# 🎯 Projekt końcowy: Predykcja niewypłacalności kart kredytowych

## 📌 Cel biznesowy
Zbudowanie modelu klasyfikacyjnego, który na podstawie danych demograficznych i historii płatności klienta przewidzi ryzyko niespłacenia karty kredytowej w kolejnym miesiącu. Model ma wspomagać decyzje Działu Ryzyka Kredytowego.

## 🧠 Podejście (nowoczesny Data Science)
- Automatyczna analiza eksploracyjna (Data Profiling)
- Inżynieria cech oparta na wiedzy domenowej (historia opóźnień, dynamika zadłużenia)
- **LightGBM** + inteligentne strojenie **Optuną**
- Minimalizacja biznesowej funkcji kosztu (False Negative kosztuje 10× więcej niż False Positive)
- Pełna interpretowalność z **SHAP** (Waterfall, Summary Plot)
- Interaktywne wizualizacje gotowe na prezentację dla zarządu

## 📊 Kluczowe wyniki (zbiór testowy: 9000 klientów)
| Metryka | Wartość |
|:---|:---|
| Recall dla klasy "default" | **43%** |
| Precision dla klasy "default" | 58% |
| F1-score dla klasy "default" | 0.49 |
| Biznesowy koszt całkowity | 12 008 jednostek |

> **Wniosek:** Model skutecznie identyfikuje ryzykownych klientów, a każda decyzja może być transparentnie wyjaśniona.

## 🛠 Stack technologiczny
`Python` · `LightGBM` · `Optuna` · `SHAP` · `Scikit-learn` · `Pandas` · `Plotly` · `ydata-profiling`

## 📁 Pliki w folderze
- `PROJEKT_KONCOWY_Wdrozenie.ipynb` – pełny pipeline: EDA → modelowanie → ewaluacja → interpretacja
- `README.md` – opis projektu

---

**Autor:** Tomasz Wienke  
**Data:** Czerwiec 2026  
**Kurs:** Analityk danych
