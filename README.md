# LLM Evaluation & Safety Framework 🚀

## 📌 O projekcie
To autorskie narzędzie typu **QA Benchmarking Tool**, zaprojektowane do automatycznego testowania modeli językowych (LLM). Projekt powstał, aby systematyzować proces sprawdzania jakości odpowiedzi AI, ze szczególnym uwzględnieniem bezpieczeństwa (Safety) i logiki (Reasoning).

Jako tester oprogramowania, przenoszę dobre praktyki z testowania tradycyjnego (Data-Driven Testing) do świata Generative AI.

## 🛠️ Kluczowe Funkcje
- **Data-Driven Testing**: Wszystkie przypadki testowe są odseparowane od kodu i przechowywane w strukturze JSON.
- **Kategoryzacja Testów**: Możliwość filtrowania testów według kategorii:
  - `Logic` (Logika i spójność)
  - `Safety` (Zabezpieczenia i etyka)
  - `Reasoning` (Rozumowanie krok po kroku)
  - `Hallucination` (Weryfikacja faktów)
- **Bezpieczeństwo**: Pełna izolacja kluczy API za pomocą zmiennych środowiskowych (`.env`).

## 🏗️ Architektura Projektu
- **Język**: Python 3.12+
- **Zarządzanie zależnościami**: `pip` (requirements.txt)
- **Format danych**: JSON (test_cases.json)

## 🚀 Jak uruchomić?
1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/piotrwalas1/llm-evaluation-framework.git](https://github.com/piotrwalas1/llm-evaluation-framework.git)
