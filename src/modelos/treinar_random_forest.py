# Arquivo responsável por treinar o modelo Random Forest.


from sklearn.ensemble import RandomForestRegressor  # Nossa Floresta Aleatória (RandomForestRegressor), utilize várias árvores de decisão para prever valores


def treinar_random_forest(X_treino_final, y_treino):  # Nossa função (treinar_random_forest), treine um modelo Random Forest

    modelo = RandomForestRegressor(random_state=42)  # Nosso modelo (modelo), utilize uma Floresta Aleatória (RandomForestRegressor) mantendo resultados reproduzíveis (random_state=42)

    modelo.fit(X_treino_final, y_treino)  # Nosso modelo (modelo), aprenda utilizando os dados de treinamento (X_treino_final e y_treino)

    return modelo  # Retorne nosso modelo treinado (modelo)