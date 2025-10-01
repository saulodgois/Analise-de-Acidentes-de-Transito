# Analise-de-Acidentes-de-Transito
Projeto feito durante a matéria de Big Data Analysis para identificar padrões nos acidentes de transito e como essas informações podem ser utilizadas para prevenção.

Requisitos
Python 3.x
pandas
matplotlib
seaborn


Principais Funcionalidades
Análise geográfica de acidentes por estado.
Análise de padrões temporais (hora do dia, dia da semana).
Distribuição da severidade dos acidentes.
Comparações entre população e taxa de acidentes.

Uso
Coloque o conjunto de dados de acidentes (US_Accidents_March23.csv) no diretório data.
Execute a análise:
	Bash
	python scripts/traffic_analysis.py


Formato dos Dados
O conjunto de dados deve incluir as seguintes colunas principais:
Start_Time: Carimbo de data/hora do acidente.
State: Abreviação do estado dos EUA.
Severity: Severidade do acidente (1-4).
Colunas adicionais para análise detalhada.

Saída
A análise gera:
Distribuição de acidentes por estado.
Visualização de padrões temporais.
Resumo da distribuição de severidade.
Gráficos de acidentes vs população.

Funções
load_and_prepare_data(): Pré-processamento e carregamento de dados.
analyze_accidents_by_state(): Análise em nível estadual.
analyze_temporal_patterns(): Padrões baseados no tempo.
generate_summary_report(): Relatório de análise abrangente.
plot_accidents_vs_population(): Visualização de acidentes versus população.

Tratamento de Erros
O código inclui tratamento de erros robusto para:
Arquivos ausentes.
Problemas de formato de dados.
Valores inválidos de data/hora.
Problemas de codificação (encoding).

Licença
Licença MIT

Observação
Certifique-se de ter memória suficiente para lidar com o conjunto de dados, pois ele pode ser grande.
Devido ao grande número de dados, é normal que demore alguns minutos para a geração dos gráficos.
