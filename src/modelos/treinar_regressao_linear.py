# Arquivo responsável por treinar o modelo de Regressão Linear.


from sklearn.linear_model import LinearRegression  # Nossa Regressão Linear (LinearRegression), utilize um modelo baseado em uma equação matemática para prever valores


def treinar_regressao_linear(X_treino_final, y_treino):  # Nossa função (treinar_regressao_linear), treine um modelo de Regressão Linear

    modelo = LinearRegression()  # Nosso modelo (modelo), utilize a Regressão Linear (LinearRegression) para aprender os padrões dos dados

    modelo.fit(X_treino_final, y_treino)  # Nosso modelo (modelo), aprenda utilizando os dados de treinamento (X_treino_final e y_treino)

    return modelo  # Retorne nosso modelo treinado (modelo)