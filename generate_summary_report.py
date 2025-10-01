def generate_summary_report(df, accidents_by_state):

    print("\n" + "="*60)
    print("RELATÓRIO RESUMO - ANÁLISE DE ACIDENTES DE TRÂNSITO")
    print("="*60)

    print(f"\n📊 ESTATÍSTICAS GERAIS:")
    print(f"• Total de acidentes analisados: {len(df):,}")
    print(
        f"• Período analisado: {df['Start_Time'].min().strftime('%Y-%m-%d')} a {df['Start_Time'].max().strftime('%Y-%m-%d')}")
    print(f"• Estados com dados: {df['State'].nunique()}")
    print(f"• Cidades com dados: {df['City'].nunique():,}")

    print(f"\n🗺️ DISTRIBUIÇÃO GEOGRÁFICA:")
    top_3_states = accidents_by_state.head(3)
    for i, (state, count) in enumerate(top_3_states.items(), 1):
        print(f"• {i}º lugar: {state} ({count:,} acidentes)")

    print(f"\n⏰ PADRÕES TEMPORAIS:")
    day_with_most = df['Day_of_Week'].value_counts().idxmax()
    hour_with_most = df['Hour'].value_counts().idxmax()
    print(f"• Dia com mais acidentes: {day_with_most}")
    print(f"• Hora com mais acidentes: {hour_with_most}h")

    print(f"\n🚨 SEVERIDADE:")
    severity_dist = df['Severity'].value_counts().sort_index()
    for severity, count in severity_dist.items():
        print(
            f"• Severidade {severity}: {count:,} acidentes ({count/len(df)*100:.1f}%)")
