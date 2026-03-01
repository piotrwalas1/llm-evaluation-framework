# LLM Evaluation Benchmark: Grok Performance Analysis

Analiza porównawcza modelu **Grok** w zakresie stabilności, bezpieczeństwa oraz logiki przy zmiennych parametrach temperatury. Projekt wykorzystuje architekturę *Model-Judge-Evaluation*, eliminując subiektywność w procesie oceniania.

## 🔬 Metodologia testowa (Project Architecture)

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

## 🛠 Jak uruchomić?

### Wymagania
- Python 3.x
- Biblioteki: `matplotlib`, `numpy`

### Instalacja i uruchomienie
1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/twoja-nazwa/llm-benchmark.git](https://github.com/twoja-nazwa/llm-benchmark.git)
