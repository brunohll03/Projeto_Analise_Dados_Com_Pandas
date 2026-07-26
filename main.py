# Arquivo principal responsável por executar o fluxo de processamento dos dados.
# Neste arquivo as funções de carregamento, limpeza e análise são organizadas
# para executar o pipeline completo do projeto.


from src.carregar_dados import carregar_dados        # Importa a função responsável por carregar os dados
from src.limpar_dados import limpar_dados            # Importa a função responsável pela limpeza dos dados
from src.analisar_dados import analisar_dados        # Importa a função responsável pela análise dos dados
from src.visualizar_dados import visualizar_dados  # Importa a função responsável pelos gráficos

df = carregar_dados()                                # Carrega os dados do arquivo CSV para um DataFrame

print("Dados antes da limpeza:")                     # Exibe o título dos dados antes da limpeza
print(df.head(5))                                    # Exibe as primeiras 5 linhas do DataFrame


df = limpar_dados(df)                                # Executa o processo de limpeza dos dados


print("\nDados depois da limpeza (5 primeiros):")                  # Exibe o título dos dados depois da limpeza


df.to_csv("data/processed/atendimentos_limpos.csv", index=False)  # Salva os dados limpos em um novo arquivo CSV
print("\nDados limpos salvos com sucesso!")          # Informa que o arquivo foi salvo com sucesso

analisar_dados(df)                                   # Executa a análise exploratória dos dados

visualizar_dados(df)                                 # Executa a visualização dos dados com gráficos