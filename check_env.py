import os
from openai import OpenAI
from dotenv import load_dotenv

def test_setup():
    print("--- Start Smoke Testu Środowiska ---")
    
    # 1. Sprawdzanie bibliotek
    try:
        load_dotenv()
        print("✅ Biblioteka dotenv działa.")
    except ImportError:
        print("❌ Brak biblioteki dotenv.")

    # 2. Sprawdzanie zmiennych środowiskowych
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("✅ Klucz API został wykryty w systemie.")
    else:
        print("⚠️ Klucz API nie został wykryty (to normalne, jeśli jeszcze go nie dodałeś).")

    print("--- Koniec Testu ---")

if __name__ == "__main__":
    test_setup()