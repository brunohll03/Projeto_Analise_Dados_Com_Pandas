# Arquivo responsável por treinar o modelo Decision Tree.

from sklearn.tree import DecisionTreeRegressor  # Nossa Árvore de Decisão (DecisionTreeRegressor), utilize perguntas para prever valores


def treinar_decision_tree(X_treino_final, y_treino):  # Nossa função (treinar_decision_tree), treine uma Árvore de Decisão

    modelo = DecisionTreeRegressor(random_state=42)  # Nosso modelo (modelo), utilize uma Árvore de Decisão (DecisionTreeRegressor) e mantenha resultados reproduzíveis (random_state=42)

    modelo.fit(X_treino_final, y_treino)  # Nosso modelo (modelo), aprenda utilizando os dados de treinamento (fit)

    return modelo  # Retorne nosso modelo treinado (modelo)