def fazer_previsao(modelo, X_teste_final):  # Nossa função (fazer_previsao), receba nosso modelo treinado (modelo) e os dados que queremos prever (X_teste_final)

    previsoes = modelo.predict(X_teste_final)  # Nossas previsões (previsoes), utilize nosso modelo treinado (modelo) para prever os valores utilizando os dados de teste (X_teste_final)

    return previsoes  # Retorne nossas previsões realizadas pelo modelo (previsoes)