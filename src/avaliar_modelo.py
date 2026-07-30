from sklearn.metrics import mean_absolute_error  # Nossa métrica para calcular o erro médio absoluto das previsões (mean_absolute_error)


def avaliar_modelo(y_teste, previsoes):  # Nossa função para avaliar o modelo (avaliar_modelo), comparando valores reais e previstos (y_teste e previsoes)

    mae = mean_absolute_error(y_teste, previsoes)  # Nosso erro médio absoluto (mae), calcule a diferença média entre valores reais e previstos (mean_absolute_error)

    return mae  # Retorne nosso resultado da avaliação (mae)