# 🚀 LLM Evaluation Framework

Narzędzie do automatycznego audytu i benchmarkingu modeli językowych (LLM). Projekt pozwala na systematyczne testowanie modeli pod kątem logiki, bezpieczeństwa (Safety), halucynacji oraz stronniczości (Bias), wykorzystując architekturę **LLM-as-a-Judge**.

## 🧠 O projekcie

Framework został zaprojektowany, aby rozwiązać problem subiektywnej oceny odpowiedzi modeli AI. Zamiast ręcznego sprawdzania każdego przypadku, system wykorzystuje potężniejszy model (sędziowski), który dokonuje rygorystycznego audytu odpowiedzi mniejszego modelu na podstawie zdefiniowanych kryteriów QA.



## 🛠️ Architektura i Technologie

- **Język:** Python 3.x
- **Silnik AI:** Groq API
- **Modele:**
  - **Testowany:** `llama-3.1-8b-instant` (szybki, lekki model)
  - **Audytor (Sędzia):** `llama-3.3-70b-versatile` (zaawansowany model do rygorystycznej oceny)
- **Integracja zewnętrzna:** Projekt zaprojektowany z myślą o współpracy z automatyzacją w **Make.com** (analiza wymagań i raportowanie błędów w Jirze).

## 📊 Kluczowe Funkcjonalności

1. **Automatyczny Audyt:** Sędzia AI wystawia werdykt (PASS/FAIL), klasyfikuje błąd (np. Halucynacja, Overthinking) oraz podaje merytoryczne uzasadnienie.
2. **Testy Bezpieczeństwa (Red Teaming):** Sprawdzanie odporności na próby wyłudzenia danych (PII) oraz generowanie złośliwego oprogramowania.
3. **Wykrywanie Halucynacji:** Weryfikacja faktów historycznych, geograficznych i matematycznych.
4. **Analiza Overthinking:** Wykrywanie sytuacji, w których model generuje zbędny, nielogiczny wywód zamiast prostej odpowiedzi.

## 📈 Przykładowe Wyniki Audytu

Ostatni raport wykazał skuteczność modelu na poziomie **41.67%**. Najważniejsze wnioski:
- **Krytyczna luka bezpieczeństwa:** Model uległ manipulacji i wygenerował skrypt do ekstrakcji haseł (Case #2).
- **Problemy z logiką:** Silna tendencja do nadinterpretacji prostych zagadek (Case #1).
- **Halucynacje:** Błędy w podawaniu stolic europejskich na określoną literę (Case #12).

## 🚀 Jak uruchomić?

1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/piotrwalas1/llm-evaluation-framework.git](https://github.com/piotrwalas1/llm-evaluation-framework.git)
