# Arquivo responsável por realizar previsões utilizando um modelo treinado.


def fazer_previsao(modelo, X):  # Nossa função (fazer_previsao), utilize um modelo treinado (modelo) para prever os valores dos dados informados (X)

    previsoes = modelo.predict(X)  # Nossas previsões (previsoes), utilize o modelo treinado (modelo) para prever os valores dos dados (X)

    return previsoes  # Retorne nossas previsões (previsoes)