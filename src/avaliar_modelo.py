import pandas as pd  # Nossa biblioteca Pandas (pd), utilizada para trabalhar com tabelas e DataFrames
from sklearn.metrics import mean_absolute_error  # Nossa métrica para calcular o erro médio absoluto das previsões (mean_absolute_error)
from sklearn.model_selection import cross_val_score  # Nossa função para realizar validação cruzada (cross_val_score)


def avaliar_modelo(y_teste, previsoes):  # Nossa função para avaliar o modelo (avaliar_modelo), comparando os valores reais com os valores previstos (y_teste e previsoes)

    mae = mean_absolute_error(y_teste, previsoes)  # Nosso erro médio absoluto (mae), calculando a diferença média entre os valores reais e previstos (mean_absolute_error)

    return mae  # Nosso resultado (return), retornando o erro médio absoluto (mae)


def comparar_previsoes(y_teste, previsoes):  # Nossa função para comparar as previsões (comparar_previsoes), utilizando os valores reais e previstos (y_teste e previsoes)

    comparacao = pd.DataFrame({
        "valor_real": y_teste.values,
        "valor_previsto": previsoes
    })

    comparacao["diferenca"] = comparacao["valor_real"] - comparacao["valor_previsto"]

    return comparacao


def analisar_coeficientes(modelo, encoder):  # Nossa função para analisar os coeficientes (analisar_coeficientes), utilizando nosso modelo treinado e nosso encoder (modelo e encoder)

    nomes_categorias = encoder.get_feature_names_out()

    nomes_colunas = ["idade", "ano_moto"] + list(nomes_categorias)

    coeficientes = pd.DataFrame({
        "variavel": nomes_colunas,
        "coeficiente": modelo.coef_
    })

    return coeficientes


def validar_modelo(modelo, X, y):  # Nossa função para validar o modelo (validar_modelo), utilizando validação cruzada com todos os dados preparados (modelo, X e y)

    scores = cross_val_score(  # Nossos resultados da validação cruzada (scores), avalie o modelo utilizando cinco divisões diferentes dos dados (cross_val_score)
        modelo,
        X,
        y,
        cv=5,
        scoring="neg_mean_absolute_error"
    )

    mae = -scores.mean()  # Nosso erro médio absoluto (mae), converta o resultado negativo para positivo e calcule a média dos cinco testes (-scores.mean)

    return mae  # Nosso resultado (return), retornando o MAE médio encontrado pela validação cruzada (mae)