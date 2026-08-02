# Arquivo responsável por treinar o modelo XGBoost.

from xgboost import XGBRegressor  # Nossa classe XGBoost para regressão (XGBRegressor), utilizada para criar um modelo baseado em Gradient Boosting otimizado

def treinar_xgboost(X_treino_final, y_treino):  # Nossa função para treinar o modelo XGBoost (treinar_xgboost), utilizando os dados preparados para treinamento (X_treino_final e y_treino)

    modelo = XGBRegressor(  # Nosso modelo XGBoost (modelo), crie um modelo de Gradient Boosting otimizado
        n_estimators=100,  # Nossa quantidade de árvores (n_estimators=100), utilize até 100 árvores para realizar as previsões
        learning_rate=0.1,  # Nossa taxa de aprendizado (learning_rate=0.1), controle o quanto cada árvore corrige os erros da anterior
        max_depth=6,  # Nossa profundidade máxima da árvore (max_depth=6), limite o crescimento de cada árvore para evitar overfitting
        random_state=42  # Nossa semente aleatória (random_state=42), garanta que o treinamento produza sempre os mesmos resultados
    )

    modelo.fit(X_treino_final, y_treino)  # Nosso treinamento do modelo (fit), ensine o XGBoost utilizando os dados de treinamento

    return modelo  # Nosso modelo treinado (modelo), retorne o XGBoost pronto para realizar previsões