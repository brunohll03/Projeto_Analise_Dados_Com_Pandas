from sklearn.linear_model import LinearRegression  # Nosso algoritmo de Regressão Linear (LinearRegression), utilizado para criar previsões com base em relações lineares
from sklearn.ensemble import RandomForestRegressor  # Nosso algoritmo Random Forest para regressão (RandomForestRegressor), utilizado para criar previsões utilizando várias árvores de decisão


def treinar_modelo(X_treino_final, y_treino):  # Nossa função para treinar o modelo (treinar_modelo), utilizando os dados preparados para treinamento (X_treino_final e y_treino)

    modelo = LinearRegression()  # Nosso modelo (modelo), utilizando a Regressão Linear para realizar as previsões (LinearRegression)

    modelo.fit(X_treino_final, y_treino)  # Nosso modelo (modelo), aprenda os padrões existentes nos dados de treinamento (fit)

    return modelo  # Nosso resultado (return), retornando o modelo treinado (modelo)


def treinar_random_forest(X_treino_final, y_treino):  # Nossa função para treinar o Random Forest (treinar_random_forest), utilizando os dados preparados para treinamento (X_treino_final e y_treino)

    modelo = RandomForestRegressor(n_estimators=100, random_state=42)  # Nosso modelo (modelo), utilize 100 árvores de decisão para criar o Random Forest e mantenha os mesmos resultados em cada execução (n_estimators=100, random_state=42)

    modelo.fit(X_treino_final, y_treino)  # Nosso modelo (modelo), aprenda os padrões existentes nos dados de treinamento (fit)

    return modelo  # Nosso resultado (return), retornando o Random Forest treinado (modelo)


def fazer_previsao(modelo, X_teste_final):  # Nossa função para fazer previsões (fazer_previsao), utilizando nosso modelo treinado e os dados de teste (modelo e X_teste_final)

    previsoes = modelo.predict(X_teste_final)  # Nossas previsões (previsoes), utilize nosso modelo treinado para prever os valores dos dados de teste (predict)

    return previsoes  # Nosso resultado (return), retornando os valores previstos pelo modelo (previsoes)
