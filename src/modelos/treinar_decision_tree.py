# Arquivo responsável por treinar o modelo Decision Tree.

from sklearn.tree import DecisionTreeRegressor  # Nossa classe Decision Tree para regressão (DecisionTreeRegressor), utilizada para criar um modelo baseado em árvores de decisão


def treinar_decision_tree(X_treino_final, y_treino):  # Nossa função para treinar o modelo Decision Tree (treinar_decision_tree), utilizando os dados preparados para treinamento (X_treino_final e y_treino)

    modelo = DecisionTreeRegressor()  # Nosso modelo Decision Tree (modelo), crie uma árvore de decisão para prever valores numéricos

    modelo.fit(X_treino_final, y_treino)  # Nosso treinamento do modelo (fit), ensine a árvore de decisão utilizando os dados de treinamento

    return modelo  # Nosso modelo treinado (modelo), retorne a árvore de decisão pronta para realizar previsões