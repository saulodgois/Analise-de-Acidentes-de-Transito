import matplotlib.pyplot as plt
import seaborn as sns

def analyze_temporal_patterns(df):

    print("\n=== ANÁLISE C: PADRÕES TEMPORAIS ===")

    accidents_by_day = df['Day_of_Week'].value_counts()
    accidents_by_day = accidents_by_day.reindex(['Monday', 'Tuesday', 'Wednesday', 
                                                'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    print("Acidentes por dia da semana:")
    for day, count in accidents_by_day.items():
        print(f"{day}: {count:,} acidentes")

    accidents_by_hour = df['Hour'].value_counts().sort_index()

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    axes[0, 0].bar(range(len(accidents_by_day)), accidents_by_day.values, color='lightcoral', edgecolor='black', alpha=0.8)
    axes[0, 0].set_title('Acidentes por Dia da Semana', fontweight='bold')
    axes[0, 0].set_xlabel('Dia da Semana')
    axes[0, 0].set_ylabel('Número de Acidentes')
    axes[0, 0].set_xticks(range(len(accidents_by_day)))
    axes[0, 0].set_xticklabels([day[:3] for day in accidents_by_day.index], rotation=45)
    axes[0, 0].grid(axis='y', alpha=0.3)

    axes[0, 1].plot(accidents_by_hour.index, accidents_by_hour.values, 
                    marker='o', linewidth=2, markersize=4, color='darkblue')
    axes[0, 1].set_title('Acidentes por Hora do Dia', fontweight='bold')
    axes[0, 1].set_xlabel('Hora')
    axes[0, 1].set_ylabel('Número de Acidentes')
    axes[0, 1].set_xticks(range(0, 24, 2))
    axes[0, 1].grid(True, alpha=0.3)

    peak_hours = accidents_by_hour.nlargest(3)
    for hour in peak_hours.index:
        axes[0, 1].annotate(f'{accidents_by_hour[hour]:,}', 
                           xy=(hour, accidents_by_hour[hour]), 
                           xytext=(5, 10), textcoords='offset points',
                           bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

    pivot_table = df.groupby(['Day_of_Week', 'Hour']).size().unstack(fill_value=0)
    sns.heatmap(pivot_table, ax=axes[1, 0], cmap='YlOrRd', cbar_kws={'label': 'Número de Acidentes'})
    axes[1, 0].set_title('Heatmap: Acidentes por Dia e Hora', fontweight='bold')
    axes[1, 0].set_xlabel('Hora do Dia')
    axes[1, 0].set_ylabel('Dia da Semana')

    severity_by_hour = df.groupby(['Hour', 'Severity']).size().unstack(fill_value=0)
    severity_by_hour.plot(kind='area', stacked=True, ax=axes[1, 1], alpha=0.7)
    axes[1, 1].set_title('Severidade dos Acidentes por Hora', fontweight='bold')
    axes[1, 1].set_xlabel('Hora do Dia')
    axes[1, 1].set_ylabel('Número de Acidentes')
    axes[1, 1].legend(title='Severidade', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.show()

    print(f"\nPicos de acidentes:")
    print(f"Dia com mais acidentes: {accidents_by_day.idxmax()} ({accidents_by_day.max():,} acidentes)")
    print(f"Hora com mais acidentes: {accidents_by_hour.idxmax()}h ({accidents_by_hour.max():,} acidentes)")

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    weekend = ['Saturday', 'Sunday']
    
    weekday_accidents = df[df['Day_of_Week'].isin(weekdays)].shape[0]
    weekend_accidents = df[df['Day_of_Week'].isin(weekend)].shape[0]
    
    print(f"\nComparação dias úteis vs fim de semana:")
    print(f"Acidentes em dias úteis: {weekday_accidents:,} ({weekday_accidents/len(df)*100:.1f}%)")
    print(f"Acidentes no fim de semana: {weekend_accidents:,} ({weekend_accidents/len(df)*100:.1f}%)")