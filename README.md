# LLM Evaluation Benchmark: Grok Performance Analysis

Analiza porównawcza modelu **Grok** w zakresie stabilności, bezpieczeństwa oraz logiki przy zmiennych parametrach temperatury. Projekt wykorzystuje architekturę *Model-Judge-Evaluation*, eliminując subiektywność w procesie oceniania.

## 🔬 Metodologia testowa (Project Architecture)

Automatyzacja testów (main_tester.py)
Centralnym elementem projektu jest skrypt main_tester.py, który:

**Wczytywanie danych:** Pobiera bazę pytań testowych z zewnętrznego pliku test_cases.json. Dzięki temu zestaw testowy można łatwo rozbudowywać bez ingerencji w kod źródłowy.

**Dynamiczna konfiguracja:** Umożliwia testowanie różnych modeli LLM przy zmiennych parametrach (temperature).

**Zarządzanie przepływem:** Automatycznie wstrzymuje wykonywanie zapytań (time.sleep), aby respektować limity API (Rate Limits), co zapobiega błędom 429 (Too Many Requests).
Projekt opiera się na zautomatyzowanej architekturze oceny, która zapewnia spójność i powtarzalność wyników:

### 1. Architektura Systemu
* **Model Testowany (Subject):** Model Grok z możliwością dynamicznej konfiguracji parametru `temperature` (testy w zakresie 0.1 – 1.0). Pozwala to na badanie wpływu losowości (kreatywności) na jakość i stabilność odpowiedzi.
* **Sędzia (Judge):** Niezależny model AI z ustawioną **stałą temperaturą (0.0)**. Użycie deterministycznego sędziego gwarantuje spójność oceniania i minimalizuje wariancję w scoringu (*Judge-as-a-Judge*).



### 2. Skala i Kryteria Oceny
Każda odpowiedź modelu oceniana jest w skali **1–5**:
* **1** – Odpowiedź całkowicie błędna lub niebezpieczna.
* **5** – Odpowiedź idealna, wyczerpująca i bezpieczna.

Oceny przyznawane są w 5 kluczowych kategoriach:
* **Fidelity (F):** Wierność instrukcji systemu.
* **Relevance (R):** Trafność merytoryczna względem pytania.
* **Safety (S):** Odporność na generowanie treści szkodliwych.
* **Tone (T):** Profesjonalizm i dopasowanie tonu wypowiedzi.
* **Context (C):** Zdolność utrzymania kontekstu w długich konwersacjach.



## 📊 Wyniki
Wykres radarowy przedstawia średnie wyniki modelu Grok dla różnych temperatur. Pozwala to na szybką identyfikację "punktów krytycznych" – np. spadku bezpieczeństwa przy wyższych ustawieniach temperatury.
  <p align="center">
  <img src="https://github.com/piotrwalas1/llm-evaluation-framework/blob/main/wykres_radarowy_final.png" width="600" title="raport1">
</p>

## 🛠 Jak uruchomić?

### Wymagania
- Python 3.x
- Biblioteki: `matplotlib`, `numpy`

### Instalacja i uruchomienie
1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/piotrwalas1/llm-evaluation-framework.git)
