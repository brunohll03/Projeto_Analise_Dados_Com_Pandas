# Arquivo responsável por avaliar os resultados dos modelos treinados.


from sklearn.metrics import mean_absolute_error  # Nossa métrica para calcular o erro médio absoluto das previsões (mean_absolute_error)
from sklearn.metrics import mean_squared_error  # Nossa métrica para calcular o erro quadrático médio das previsões (mean_squared_error)
from sklearn.metrics import r2_score  # Nossa métrica para calcular o coeficiente de determinação do modelo (r2_score)
from sklearn.model_selection import cross_val_score  # Nossa função para realizar validação cruzada (cross_val_score)


def avaliar_modelo(y_teste, previsoes):  # Nossa função para avaliar o modelo (avaliar_modelo), comparando valores reais e previstos (y_teste e previsoes)

    mae = mean_absolute_error(y_teste, previsoes)  # Nosso erro médio absoluto (mae), calculando a diferença média entre valores reais e previstos

    rmse = mean_squared_error(y_teste, previsoes) ** 0.5  # Nosso erro quadrático médio (rmse), calculando a raiz do erro para penalizar diferenças maiores

    r2 = r2_score(y_teste, previsoes)  # Nosso coeficiente de determinação (r2), mostrando quanto o modelo consegue explicar dos dados


    return mae, rmse, r2  # Nosso resultado (return), retornando MAE, RMSE e R² encontrados pelo modelo


def validar_modelo(modelo, X, y):  # Nossa função para validar o modelo (validar_modelo), utilizando validação cruzada com os dados preparados (modelo, X e y)

    resultados = cross_val_score(modelo, X, y, cv=5, scoring="neg_mean_absolute_error")  # Nossos resultados da validação cruzada (resultados), execute cinco treinamentos e avaliações do mesmo modelo utilizando diferentes divisões dos dados

    mae_medio = -resultados.mean()  # Nosso MAE médio (mae_medio), transformando o resultado negativo em positivo e calculando a média das avaliações

    return mae_medio  # Nosso resultado (return), retornando o MAE médio encontrado pela validação cruzada