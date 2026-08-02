# Arquivo responsável por carregar os dados utilizados no projeto.
# Neste arquivo a função de leitura do arquivo CSV é implementada,
# disponibilizando os dados para as próximas etapas do pipeline.


import pandas as pd  # Nossa biblioteca Pandas (pd), utilizada para manipulação e leitura dos dados



def carregar_dados():  # Nossa função (carregar_dados), responsável por carregar o arquivo CSV contendo os dados das vendas

    caminho_arquivo = "data/raw/atendimentos_expandido.csv"  # Nosso caminho do arquivo CSV gerado com a base expandida de dados

    df = pd.read_csv(
        caminho_arquivo
    )  # Nosso DataFrame (df), carregue os dados do arquivo CSV utilizando o Pandas


    print(
        f"\nDados carregados com sucesso! Quantidade de registros: {len(df)}"
    )  # Informa que os dados foram carregados e mostra a quantidade de registros disponíveis


    return df  # Nosso resultado (return), retorne o DataFrame contendo os dados carregados