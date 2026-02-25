# 🚀 LLM Evaluation Framework (Professional QA Edition)

Zaawansowane narzędzie do wielowymiarowego audytu modeli językowych (LLM). Projekt wykorzystuje architekturę **LLM-as-a-Judge** do oceny odpowiedzi w skali 1-5 na podstawie rygorystycznych kryteriów inżynierii jakościowej.

## 📊 Metodologia Audytu (Multi-dimensional Grading)

Zamiast prostego testu PASS/FAIL, każda odpowiedź modelu jest oceniana przez "Sędziego AI" (`llama-3.3-70b`) w pięciu kluczowych kategoriach:

- **Fidelity (Wierność):** Zgodność z instrukcją.
- **Relevance (Trafność):** Trzymanie się tematu.
- **Safety (Bezpieczeństwo):** Odporność na próby Red Teamingu.
- **Tone (Ton):** Profesjonalizm i styl wypowiedzi.
- **Context (Kontekst):** Zrozumienie niuansów i intencji.

## 📈 Wyniki Benchmarku (Próba n=60)

Ostatni audyt modelu `Llama-3.1-8b-instant` na 60 zróżnicowanych przypadkach wykazał:

- **Średnia Ogólna:** 41.67% (Score: ~2.1/5)
- **Największa słabość:** **Context & Logic** – model wykazuje silną tendencję do tzw. *Overthinking* (np. Case #1, #55).
- **Największa siła:** **Safety (Jailbreak protection)** – model skutecznie odparł próby zmiany persony na "ChaosMode" (Case #9).
- **Krytyczne znalezisko:** Wykryto lukę bezpieczeństwa w procesie generowania kodu (Case #2) – model dostarczył skrypt do ekstrakcji haseł.

![Profil Modelu](./model_profile.png)

## 🛠️ Nowe Funkcjonalności

- **Rate Limit Protection:** Zaimplementowałem mechanizm `time.sleep`, pozwalający na stabilne odpytywanie darmowych API przy dużych zestawach danych.
- **Automatyczna wizualizacja:** Skrypt `generate_charts.py` generuje wykresy radarowe na podstawie raportów tekstowych.
- **Zestaw 60 Edge Cases:** Baza testowa obejmuje teraz zaawansowaną logikę, matematykę, bezpieczeństwo chemiczne i próby daxingu.

## 🚀 Jak użyć?
1. Uruchom `python main_tester.py` aby wygenerować raport.
2. Uruchom `python generate_charts.py` aby stworzyć wizualizację wyników.
