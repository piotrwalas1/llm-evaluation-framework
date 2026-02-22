import json

def run_benchmark(file_path, filter_category=None):
    with open(file_path, 'r', encoding='utf-8') as f:
        tests = json.load(f)

    print(f"🚀 Uruchamiam AI Benchmark")
    print("=" * 30)

    for test in tests:
        # Filtracja kategorii
        if filter_category and test['category'] != filter_category:
            continue
            
        print(f"[{test['category']}] Case #{test['id']}")
        print(f"Pytanie: {test['prompt']}")
        print(f"Oczekujemy: {test['expected_behavior']}")
        print("-" * 20)

if __name__ == "__main__":
    # Możesz wpisać np. 'Safety', żeby zobaczyć tylko testy bezpieczeństwa
    run_benchmark('test_cases.json', filter_category=None)