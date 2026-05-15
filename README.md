# 📧 Wykrywanie spamu – NLP w praktyce

Projekt zaliczeniowy z modułu **Natural Language Processing (NLP)**.

## 🎯 Cel
Zbudowanie modelu klasyfikującego wiadomości SMS jako **spam** lub **nie-spam (ham)**.  
Porównanie podejścia klasycznego (TF‑IDF + Random Forest) z nowoczesnymi technikami (Sentence Transformers).

## 📊 Wyniki

| Metoda | F1-score (spam) | Accuracy |
|--------|-----------------|----------|
| TF‑IDF + selekcja cech + Random Forest (kurs) | 0.89 | 0.971 |
| Pipeline TF‑IDF + LogisticRegression | 0.945 | 0.948 |
| **Sentence Transformers + LogisticRegression** | **0.93** | **0.980** |

## 🛠️ Technologie
- Python 3, scikit-learn, NLTK, spaCy
- Sentence Transformers (all-MiniLM-L6-v2)
- Git, GitHub

## 📁 Plik
- `Zadanie_Random_Forest.ipynb` – kompletny notebook z kodem i wnioskami.

## 🔍 Wnioski
Nowoczesne embeddingi kontekstowe dają wyższą jakość przy znacznie mniejszym nakładzie pracy.  
Pipeline'y i Transformery to standard w Data Science 2026.

---
*Autor:Tomasz Wienke 

