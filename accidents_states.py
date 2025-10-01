import matplotlib.pyplot as plt

def analyze_accidents_by_state(df):

    print("\n=== ANÁLISE A: ACIDENTES POR ESTADO ===")

    accidents_by_state = df['State'].value_counts().sort_index()

    mean_accidents = accidents_by_state.mean()
    median_accidents = accidents_by_state.median()
    
    print(f"Média de acidentes por estado: {mean_accidents:.2f}")
    print(f"Mediana de acidentes por estado: {median_accidents:.2f}")
    print(f"Desvio padrão: {accidents_by_state.std():.2f}")

    print("\nTop 10 estados com mais acidentes:")
    top_10 = accidents_by_state.head(10)
    for state, count in top_10.items():
        print(f"{state}: {count:,} acidentes")

    plt.figure(figsize=(15, 8))
    accidents_by_state.head(15).plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Top 15 Estados com Mais Acidentes de Trânsito', fontsize=16, fontweight='bold')
    plt.xlabel('Estado', fontsize=12)
    plt.ylabel('Número de Acidentes', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)

    plt.axhline(y=mean_accidents, color='red', linestyle='--', alpha=0.7, 
                label=f'Média: {mean_accidents:.0f}')
    plt.axhline(y=median_accidents, color='orange', linestyle='--', alpha=0.7, 
                label=f'Mediana: {median_accidents:.0f}')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    return accidents_by_state