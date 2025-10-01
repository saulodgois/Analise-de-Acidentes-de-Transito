import os
from loan_data import load_and_prepare_data
from accidents_states import analyze_accidents_by_state
from plot_accidents_population import plot_accidents_vs_population
from temporal_patterns import analyze_temporal_patterns
from generate_summary_report import generate_summary_report


def main():
    filename = "US_Accidents_March23.csv"

    print("📂 Working dir:", os.getcwd())
    try:
        print("📂 Arquivos na pasta data:", os.listdir("data")[:20])
    except FileNotFoundError:
        print("⚠️ Pasta 'data' não encontrada")

    try:
        df = load_and_prepare_data(filename)

        accidents_by_state = analyze_accidents_by_state(df)
        plot_accidents_vs_population(accidents_by_state)
        analyze_temporal_patterns(df)
        generate_summary_report(df, accidents_by_state)

        print("\n✅ Análise concluída com sucesso!")

    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{filename}' não encontrado.")
        print("Por favor, certifique-se de que o arquivo está no diretório correto e ajuste o nome na variável 'filename'.")
    except Exception as e:
        print(f"❌ Erro durante a análise: {str(e)}")


if __name__ == "__main__":
    main()
