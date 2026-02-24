import json
import os
import sys
import io
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def get_ai_response(prompt):
    """Wysyła zapytanie do modelu Llama 3.1 przez API Groq."""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
            
                {"role": "system", "content": "Jesteś pomocnym asystentem. Odpowiadaj konkretnie i zgodnie z logiką."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Błąd API: {e}"

def run_benchmark(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        tests = json.load(f)

    report_content = []
    header = f"=== RAPORT Z TESTÓW LLM ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ===\n"
    header += f"Model: llama-3.1-8b-instant\n"
    header += "=" * 60 + "\n\n"
    
    print(header)
    report_content.append(header)

    for test in tests:
        print(f"[{test['category']}] Case #{test['id']}")
        print(f"Pytanie: {test['prompt']}")
        
        print("AI myśli...")
        actual_response = get_ai_response(test['prompt'])
        
        result_text = f"[{test['category']}] Case #{test['id']}\n"
        result_text += f"Pytanie: {test['prompt']}\n"
        result_text += f"ODPOWIEDŹ AI: {actual_response}\n"
        result_text += f"OCZEKIWANO: {test['expected_behavior']}\n"
        result_text += "-" * 40 + "\n"
        
        print(f"Odpowiedź AI: {actual_response}")
        print("-" * 50)
        report_content.append(result_text)


    with open("benchmark_report.txt", "w", encoding="utf-8") as report_file:
        report_file.writelines(report_content)
    
    print(f"\n✅ Testy zakończone! Raport zapisano w pliku: benchmark_report.txt")

if __name__ == "__main__":
    run_benchmark('test_cases.json')