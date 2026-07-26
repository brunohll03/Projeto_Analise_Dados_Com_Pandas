# Módulo responsável pela limpeza e preparação dos dados.
# Neste arquivo são implementadas funções para tratar dados ausentes,
# remover duplicidades, corrigir inconsistências e preparar os dados
# para as etapas de análise.


import pandas as pd                                      # Importa a biblioteca Pandas para manipulação dos dados


def limpar_dados(df):                                    # Função responsável pela limpeza e preparação dos dados

    df["nome_cliente"] = df["nome_cliente"].str.strip().str.title()# Remove espaços extras e converte para formato título

    #

    df["idade"] = pd.to_numeric(df["idade"], errors="coerce")  # Converte valores inválidos para NaN

    df.loc[(df["idade"] < 0) | (df["idade"] > 100), "idade"] = pd.NA  # Valores fora do intervalo válido viram NA

    mediana = df["idade"].median()  # Calcula a mediana das idades válidas

    df["idade"] = df["idade"].fillna(mediana).astype("int64")  # Preenche NA com a mediana e converte para int64

    #

    df["cidade_cliente"] = df["cidade_cliente"].str.strip().str.title()  # Remove espaços extras e converte para formato título

    #

    df["estado"] = df["estado"].str.strip().str.upper()  # Remove espaços extras e converte para formato título
    #

    df["moto"] = df["moto"].str.strip().str.upper()  # Remove espaços extras e converte para formato título

    #

    df["marca"] = df["marca"].str.strip().str.upper()  # Remove espaços extras e converte para letras maiúsculas

    #

    df["categoria"] = df["categoria"].str.strip().str.title()  # Remove espaços extras e converte para formato título

    #

    df["ano_moto"] = df["ano_moto"].astype("int64")  # Converte o ano para número inteiro
    #

    df["valor_moto"] = (df["valor_moto"]
        .astype(str)                      # Converte os valores para texto
        .str.strip()                      # Remove espaços extras
        .str.replace(r"[^\d,.]", "", regex=True)  # Remove letras e caracteres inválidos
        .str.replace(".", "", regex=False)        # Remove o separador de milhar
        .str.replace(",", ".", regex=False)       # Converte a vírgula decimal para ponto
        .astype(float)                    # Converte para float
    )

    #

    df["loja"] = df["loja"].str.strip().str.title()  # Remove espaços extras e converte para formato título

    #

    df["cidade_loja"] = df["cidade_loja"].str.strip().str.title()  # Remove espaços extras e converte para formato título

    #

    df["vendedor"] = df["vendedor"].str.strip().str.title()  # Remove espaços extras e converte para formato título

    #

    df["status_venda"] = (
        df["status_venda"]
        .str.strip()                                      # Remove espaços extras
        .str.replace("á", "a").str.replace("ã", "a")     # Remove acentos
        .str.replace("é", "e").str.replace("í", "i")     # Remove acentos
        .str.replace("ó", "o").str.replace("ú", "u")     # Remove acentos
        .str.upper()                                      # Converte para maiúsculo
        .str.replace("AGENDADO", "AGENDADA")             # Converte masculino para feminino
        .str.replace("CONCLUIDO", "CONCLUIDA")           # Converte masculino para feminino
        .str.replace("CANCELADO", "CANCELADA")           # Converte masculino para feminino
    )

    status_validos = ["AGENDADA", "CONCLUIDA", "CANCELADA"]  # Define os status válidos

    df.loc[~df["status_venda"].isin(status_validos), "status_venda"] = pd.NA  # Valores inválidos viram NA

    #

    df["forma_pagamento"] = df["forma_pagamento"].str.strip().str.title()  # Remove espaços extras e converte para formato título

    #

    df["data_venda"] = pd.to_datetime(df["data_venda"].astype("string").str.strip(), dayfirst=True, errors="coerce")  # Remove espaços e converte para data

    #

    df["email"] = df["email"].str.strip().str.lower()  # Remove espaços e converte para minúsculo

    df.loc[~df["email"].str.contains("@", na=False), "email"] = pd.NA  # E-mails sem @ viram NA

    #

    df["telefone"] = df["telefone"].astype("string").str.replace(r"\D", "", regex=True)  # Converte para texto e mantém apenas números

    df.loc[~df["telefone"].str.len().isin([10, 11]), "telefone"] = pd.NA  # Telefones diferentes de 10 ou 11 dígitos viram NA

    #

    df = df.drop_duplicates(subset="id_venda", keep="first")  # Remove IDs de venda duplicados e mantém a primeira ocorrência

    return df                                             # Retorna o DataFrame após a limpeza