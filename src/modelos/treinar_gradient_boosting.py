# Arquivo reservado para o treinamento do modelo Gradient Boosting.
# Arquivo responsável por treinar o modelo Gradient Boosting.

from sklearn.ensemble import GradientBoostingRegressor  # Nossa classe Gradient Boosting para regressão (GradientBoostingRegressor), utilizada para criar um modelo baseado em árvores sequenciais


def treinar_gradient_boosting(X_treino_final, y_treino):  # Nossa função para treinar o modelo Gradient Boosting (treinar_gradient_boosting), utilizando os dados preparados para treinamento (X_treino_final e y_treino)

    modelo = GradientBoostingRegressor()  # Nosso modelo Gradient Boosting (modelo), crie um conjunto de árvores que aprendem corrigindo os erros anteriores

    modelo.fit(X_treino_final, y_treino)  # Nosso treinamento do modelo (fit), ensine o Gradient Boosting utilizando os dados de treinamento

    return modelo  # Nosso modelo treinado (modelo), retorne o Gradient Boosting pronto para realizar previsões