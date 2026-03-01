import re
import matplotlib.pyplot as plt
import numpy as np
import os
import ast

def parse_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    
    matches = re.findall(r"Ocena:\s*(\{.*?\})", content)
    scores_list = []
    
    for m in matches:
        try:
            val = ast.literal_eval(m)
            
            if isinstance(val, dict) and "error" not in val:
                scores_list.append(val)
        except:
            continue
            
    if not scores_list:
        return {'F': 0, 'R': 0, 'S': 0, 'T': 0, 'C': 0}
    
    
    keys = ['F', 'R', 'S', 'T', 'C']
    avg_scores = {k: np.mean([s.get(k, 0) for s in scores_list]) for k in keys}
    return avg_scores

def plot_radar(data_dict):
    categories = ['Fidelity', 'Relevance', 'Safety', 'Tone', 'Context']
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))
    
    for model_name, scores in data_dict.items():
        values = [scores['F'], scores['R'], scores['S'], scores['T'], scores['C']]
        values += values[:1]
        ax.plot(angles, values, linewidth=2, label=model_name)
        ax.fill(angles, values, alpha=0.1)
        
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    
    plt.legend(loc='upper right', bbox_to_anchor=(1.6, 1.1), fontsize='small')
    plt.title("Benchmark LLM: Porównanie modeli i temperatur")
    
    plt.savefig("wykres_radarowy_final.png", bbox_inches='tight')
    print("\nSukces! Wykres zapisany jako 'wykres_radarowy_final.png'")
    plt.show()


results = {}
files = [f for f in os.listdir('.') if f.startswith('report_') and f.endswith('.txt')]

for file in files:
    
    base_name = file.replace("report_", "").replace(".txt", "")
   
    clean_name = str(base_name.split('_2026'))
    
    results[clean_name] = parse_report(file)
    print(f"Przetworzono: {clean_name}")

if results:
    plot_radar(results)
else:
    print("Błąd: Nie znaleziono plików raportów w folderze.")