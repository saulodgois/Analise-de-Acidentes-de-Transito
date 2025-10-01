import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

STATE_POPULATION = {
    'AL': 5108468, 'AK': 733406, 'AZ': 7431344, 'AR': 3067732, 'CA': 38965193,
    'CO': 5877610, 'CT': 3617176, 'DE': 1018396, 'FL': 22610726, 'GA': 11029227,
    'HI': 1435138, 'ID': 1964726, 'IL': 12582032, 'IN': 6862199, 'IA': 3207004,
    'KS': 2940865, 'KY': 4526154, 'LA': 4573749, 'ME': 1395722, 'MD': 6164660,
    'MA': 7001399, 'MI': 10037261, 'MN': 5748709, 'MS': 2940057, 'MO': 6196156,
    'MT': 1122069, 'NE': 1988536, 'NV': 3194176, 'NH': 1402054, 'NJ': 9290841,
    'NM': 2114371, 'NY': 19336776, 'NC': 10835491, 'ND': 813503, 'OH': 11785935,
    'OK': 4053824, 'OR': 4233358, 'PA': 12972008, 'RI': 1095610, 'SC': 5373555,
    'SD': 919318, 'TN': 7126489, 'TX': 30503301, 'UT': 3417734, 'VT': 647464,
    'VA': 8715698, 'WA': 7812880, 'WV': 1770071, 'WI': 5910955, 'WY': 584057,
    'DC': 678972
}

def plot_accidents_vs_population(accidents_by_state):

    print("\n=== ANÁLISE B: ACIDENTES VS POPULAÇÃO ===")

    states_data = []
    for state in accidents_by_state.index:
        if state in STATE_POPULATION:
            states_data.append({
                'State': state,
                'Accidents': accidents_by_state[state],
                'Population': STATE_POPULATION[state],
                'Accidents_per_100k': (accidents_by_state[state] / STATE_POPULATION[state]) * 100000
            })
    
    df_states = pd.DataFrame(states_data)

    correlation = df_states['Accidents'].corr(df_states['Population'])
    print(f"Correlação entre acidentes e população: {correlation:.3f}")

    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(df_states['Population']/1000000, df_states['Accidents'], alpha=0.7, s=60, c=df_states['Accidents_per_100k'], cmap='viridis', edgecolors='black', linewidth=0.5)

    z = np.polyfit(df_states['Population'], df_states['Accidents'], 1)
    p = np.poly1d(z)
    plt.plot(df_states['Population']/1000000, p(df_states['Population']), "r--", alpha=0.8)
    
    plt.title('Relação entre População do Estado e Número de Acidentes', fontsize=16, fontweight='bold')
    plt.xlabel('População (milhões)', fontsize=12)
    plt.ylabel('Número de Acidentes', fontsize=12)
    plt.grid(True, alpha=0.3)

    cbar = plt.colorbar(scatter)
    cbar.set_label('Acidentes por 100k habitantes', rotation=270, labelpad=20)

    for i, row in df_states.iterrows():
        if row['Accidents_per_100k'] > 150 or row['Population'] > 30000000:
            plt.annotate(row['State'], (row['Population']/1000000, row['Accidents']),xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    plt.tight_layout()
    plt.show()

    print("\nTop 10 estados com mais acidentes per capita (por 100k habitantes):")
    top_per_capita = df_states.nlargest(10, 'Accidents_per_100k')
    for _, row in top_per_capita.iterrows():
        print(f"{row['State']}: {row['Accidents_per_100k']:.1f} acidentes por 100k hab")