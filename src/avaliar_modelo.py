import pandas as pd  # Nossa biblioteca Pandas (pd), utilizada para trabalhar com tabelas e DataFrames
from sklearn.metrics import mean_absolute_error  # Nossa métrica para calcular o erro médio absoluto das previsões (mean_absolute_error)


def avaliar_modelo(y_teste, previsoes):  # Nossa função para avaliar o modelo (avaliar_modelo), comparando os valores reais com os valores previstos (y_teste e previsoes)

    mae = mean_absolute_error(y_teste, previsoes)  # Nosso erro médio absoluto (mae), calculando a diferença média entre os valores reais e os valores previstos (mean_absolute_error)

    return mae  # Nosso resultado (return), retornando o valor do erro médio absoluto calculado (mae)


def comparar_previsoes(y_teste, previsoes):  # Nossa função para comparar as previsões (comparar_previsoes), utilizando os valores reais e previstos (y_teste e previsoes)

    comparacao = pd.DataFrame({  # Nossa tabela de comparação (comparacao), criando um DataFrame para visualizar os valores reais e previstos (pd.DataFrame)
        "valor_real": y_teste.values,  # Nossa coluna de valores reais (valor_real), utilizando os valores que realmente aconteceram (y_teste.values)
        "valor_previsto": previsoes  # Nossa coluna de valores previstos (valor_previsto), utilizando os valores que nosso modelo previu (previsoes)
    })

    comparacao["diferenca"] = comparacao["valor_real"] - comparacao["valor_previsto"]  # Nossa diferença (diferenca), calculando a diferença entre o valor real e o valor previsto (valor_real - valor_previsto)

    return comparacao  # Nosso resultado (return), retornando a tabela com os valores reais, previstos e suas diferenças (comparacao)


def analisar_coeficientes(modelo, encoder):  # Nossa função para analisar os coeficientes (analisar_coeficientes), utilizando nosso modelo treinado e nosso encoder (modelo e encoder)

    nomes_categorias = encoder.get_feature_names_out()  # Nossos nomes das categorias transformadas (nomes_categorias), recuperando os nomes criados pelo encoder (get_feature_names_out)

    nomes_colunas = ["idade", "ano_moto"] + list(nomes_categorias)  # Nossos nomes de todas as colunas (nomes_colunas), juntando as colunas numéricas com as categorias transformadas (idade, ano_moto e nomes_categorias)

    coeficientes = pd.DataFrame({  # Nossa tabela de coeficientes (coeficientes), criando um DataFrame para relacionar cada coluna ao seu coeficiente (pd.DataFrame)
        "variavel": nomes_colunas,  # Nossa coluna de variáveis (variavel), mostrando o nome de cada característica utilizada pelo modelo (nomes_colunas)
        "coeficiente": modelo.coef_  # Nossa coluna de coeficientes (coeficiente), mostrando o peso que o modelo aprendeu para cada característica (modelo.coef_)
    })

    return coeficientes  # Nosso resultado (return), retornando a tabela com as variáveis e seus coeficientes (coeficientes)