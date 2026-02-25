import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def parse_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    categories = ['Fidelity', 'Relevance', 'Safety', 'Tone', 'Context']
    results = {cat: [] for cat in categories}


    for cat in categories:
        pattern = rf"{cat} \(.*?\): (\d)"
        matches = re.findall(pattern, content)
        results[cat] = [int(m) for m in matches]

    # Obliczanie średnich
    averages = {cat: np.mean(scores) for cat, scores in results.items() if scores}
    return averages

def create_radar_chart(data):
    labels = list(data.keys())
    values = list(data.values())
    
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='teal', alpha=0.25)
    ax.plot(angles, values, color='teal', linewidth=2)
    
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=12)
    
    # Dodanie skali 1-5
    for r in [1, 2, 3, 4, 5]:
        ax.annotate(str(r), xy=(0, r), color="grey", size=10)

    plt.title("Profil Jakościowy Modelu (Skala 1-5)", size=16, color='teal', y=1.1)
    plt.savefig('model_profile.png')
    print("✅ Wykres zapisany jako model_profile.png")
    plt.show()

if __name__ == "__main__":
    avg_data = parse_report('benchmark_report.txt')
    if avg_data:
        create_radar_chart(avg_data)
    else:
        print("❌ Nie znaleziono danych w raporcie. Sprawdź format pliku.")