# Módulo responsável pela análise exploratória dos dados.
# Neste arquivo são implementadas funções para analisar,
# resumir e extrair informações relevantes dos dados.


def analisar_dados(df):                                # Função responsável pela análise dos dados

    print(df.head(5))                                  # Exibe as primeiras 5 linhas do DataFrame

    #

    print("\n\nInformações gerais sobre o DataFrame:") # Exibe o título
    print(df.shape)                                    # Quantas linhas e colunas existem na nossa base?

    #

    print("\n\nResumo estatístico das colunas numéricas da nossa base:")  # Exibe o título
    print(df.describe())                               # Exibe o resumo estatístico

    #

    print("\n\nValores ausentes em cada coluna da nossa base:")          # Exibe o título
    print(df.isnull().sum())                            # Exibe a quantidade de valores ausentes

    return df