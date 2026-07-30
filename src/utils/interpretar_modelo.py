# Arquivo responsável por interpretar informações aprendidas pelos modelos.
# Neste arquivo serão criadas funções para entender quais variáveis influenciam as previsões.


import pandas as pd  # Nossa biblioteca Pandas (pd), utilizada para criar e manipular tabelas e DataFrames


def analisar_coeficientes(modelo, encoder):  # Nossa função para analisar coeficientes (analisar_coeficientes), utilizando o modelo treinado e o encoder utilizado na preparação dos dados (modelo e encoder)

    nomes_categorias = encoder.get_feature_names_out()  # Nossos nomes das categorias transformadas (nomes_categorias), obtenha os nomes criados pelo OneHotEncoder (get_feature_names_out)

    nomes_colunas = ["idade", "ano_moto"] + list(nomes_categorias)  # Nossos nomes das variáveis (nomes_colunas), junte as variáveis numéricas e categóricas utilizadas pelo modelo

    coeficientes = pd.DataFrame({  # Nossa tabela de coeficientes (coeficientes), crie uma tabela mostrando o impacto de cada variável no modelo

        "variavel": nomes_colunas,  # Nossa coluna de variáveis (variavel), informe quais características foram utilizadas pelo modelo

        "coeficiente": modelo.coef_  # Nossa coluna de coeficientes (coeficiente), informe os pesos aprendidos pela Regressão Linear (modelo.coef_)

    })

    return coeficientes  # Retorne nossa tabela com os coeficientes aprendidos pelo modelo (coeficientes)