# Arquivo responsável por treinar o modelo Random Forest.

from sklearn.ensemble import RandomForestRegressor  # Nossa classe Random Forest para regressão (RandomForestRegressor), utilizada para criar um conjunto de árvores de decisão


def treinar_random_forest(X_treino_final, y_treino):  # Nossa função para treinar o modelo Random Forest (treinar_random_forest), utilizando os dados preparados para treinamento (X_treino_final e y_treino)

    modelo = RandomForestRegressor(
        n_estimators=100,
        max_depth=5,
        min_samples_split=10
    )  # Nosso modelo Random Forest (modelo), configurado com quantidade de árvores, profundidade máxima e quantidade mínima de amostras para divisão


    modelo.fit(X_treino_final, y_treino)  # Nosso treinamento do modelo (fit), ensine a floresta utilizando os dados de treinamento


    return modelo  # Nosso modelo treinado (modelo), retorne a floresta pronta para realizar previsões