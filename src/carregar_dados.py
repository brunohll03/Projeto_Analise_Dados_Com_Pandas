# Módulo responsável pelo carregamento dos dados.
# Neste arquivo é implementada a função responsável por ler
# o arquivo CSV e disponibilizar os dados para o projeto.


import pandas as pd                                      # Importa a biblioteca Pandas para manipulação dos dados


def carregar_dados():                                    # Função responsável por carregar os dados do arquivo CSV
    caminho = "data/raw/atendimentos.csv"                # Define o caminho do arquivo CSV com os dados brutos
    df = pd.read_csv(caminho)                            # Lê o arquivo CSV e armazena os dados em um DataFrame
    
    return df                                             # Retorna o DataFrame com os dados carregados