# Arquivo principal responsável por executar o fluxo de processamento dos dados.
# Neste arquivo as funções de carregamento, limpeza, análise, visualização
# e preparação para Machine Learning são organizadas para executar o pipeline completo.


from src.carregar_dados import carregar_dados  # Nossa função para carregar os dados (carregar_dados)
from src.limpar_dados import limpar_dados  # Nossa função para limpar os dados (limpar_dados)
from src.analisar_dados import analisar_dados  # Nossa função para analisar os dados (analisar_dados)
from src.visualizar_dados import visualizar_dados  # Nossa função para visualizar os dados (visualizar_dados)
from src.preparar_modelo import preparar_modelo  # Nossa função para preparar os dados para Machine Learning (preparar_modelo)
from src.treinar_modelo import treinar_modelo, treinar_random_forest, fazer_previsao  # Nossas funções para treinar os modelos e fazer previsões (treinar_modelo, treinar_random_forest, fazer_previsao)
from src.avaliar_modelo import avaliar_modelo, comparar_previsoes, analisar_coeficientes  # Nossas funções para avaliar o modelo, comparar previsões e analisar coeficientes (avaliar_modelo, comparar_previsoes, analisar_coeficientes)


df = carregar_dados()  # Nosso DataFrame (df), carregue os dados do arquivo CSV (carregar_dados)

df = limpar_dados(df)  # Nosso DataFrame (df), limpe os dados utilizando nossa função de limpeza (limpar_dados)

df.to_csv("data/processed/atendimentos_limpos.csv", index=False)  # Nosso DataFrame (df), salve os dados limpos em um novo arquivo CSV (to_csv)

print("\nDados limpos salvos com sucesso!")  # Informa que nossos dados limpos foram salvos com sucesso

analisar_dados(df)  # Nossa análise dos dados (analisar_dados), analise nosso DataFrame já limpo (df)

# visualizar_dados(df)  # Nossa visualização dos dados (visualizar_dados), visualize nosso DataFrame já limpo (df)

X_treino_final, X_teste_final, y_treino, y_teste, encoder = preparar_modelo(df)  # Nossos dados preparados (X e y) e nosso encoder (encoder), separe os dados e aprenda as categorias para o Machine Learning (preparar_modelo)

modelo = treinar_modelo(X_treino_final, y_treino)  # Nosso modelo (modelo), treine utilizando os dados que treinamos (X_treino_final e y_treino)

print("\nModelo de Regressão Linear treinado com sucesso!")  # Informa que nosso modelo de Regressão Linear foi treinado com sucesso

previsoes = fazer_previsao(modelo, X_teste_final)  # Nossas previsões (previsoes), utilize nosso modelo treinado para prever os valores dos dados de teste (modelo e X_teste_final)

print("\nValores previstos pela Regressão Linear:")  # Exibe o título dos valores previstos pela Regressão Linear
print(previsoes)  # Nossas previsões (previsoes), mostre os valores que nosso modelo de Regressão Linear previu

mae = avaliar_modelo(y_teste, previsoes)  # Nosso erro médio absoluto da Regressão Linear (mae), compare os valores reais com os valores previstos (y_teste e previsoes)

print("\nErro médio absoluto da Regressão Linear (MAE):")  # Exibe o título do erro médio absoluto da Regressão Linear (MAE)
print(f"R$ {mae:.2f}")  # Nosso erro médio absoluto (mae), exibe o valor médio que o modelo errou em reais com duas casas decimais

comparacao = comparar_previsoes(y_teste, previsoes)  # Nossa comparação (comparacao), compare os valores reais com os valores previstos pela Regressão Linear (y_teste e previsoes)

print("\nComparação entre valores reais e previstos pela Regressão Linear:")  # Exibe o título da comparação entre os valores reais e previstos pela Regressão Linear
print(comparacao)  # Nossa comparação (comparacao), exibe os valores reais, previstos e suas diferenças

coeficientes = analisar_coeficientes(modelo, encoder)  # Nossos coeficientes (coeficientes), analise os pesos que nosso modelo de Regressão Linear aprendeu para cada característica (modelo e encoder)

print("\nCoeficientes aprendidos pela Regressão Linear:")  # Exibe o título dos coeficientes aprendidos pela Regressão Linear
print(coeficientes)  # Nossos coeficientes (coeficientes), exibe o peso aprendido pela Regressão Linear para cada característica


modelo_random_forest = treinar_random_forest(X_treino_final, y_treino)  # Nosso modelo Random Forest (modelo_random_forest), treine utilizando os dados que treinamos (X_treino_final e y_treino)

print("\nModelo Random Forest treinado com sucesso!")  # Informa que nosso modelo Random Forest foi treinado com sucesso

previsoes_treino_random_forest = fazer_previsao(modelo_random_forest, X_treino_final)  # Nossas previsões dos dados de treinamento (previsoes_treino_random_forest), utilize nosso Random Forest treinado para prever os valores dos próprios dados de treinamento (modelo_random_forest e X_treino_final)

mae_treino_random_forest = avaliar_modelo(y_treino, previsoes_treino_random_forest)  # Nosso erro médio absoluto dos dados de treinamento (mae_treino_random_forest), compare os valores reais de treinamento com os valores previstos pelo Random Forest (y_treino e previsoes_treino_random_forest)

print("\nErro médio absoluto do Random Forest nos dados de treinamento (MAE):")  # Exibe o título do erro médio absoluto do Random Forest nos dados de treinamento (MAE)

print(f"R$ {mae_treino_random_forest:.2f}")  # Nosso erro médio absoluto dos dados de treinamento (mae_treino_random_forest), exibe o valor médio que o modelo errou nos dados utilizados durante o treinamento em reais com duas casas decimais


previsoes_random_forest = fazer_previsao(modelo_random_forest, X_teste_final)  # Nossas previsões dos dados de teste (previsoes_random_forest), utilize nosso modelo Random Forest treinado para prever os valores dos dados que ele nunca viu durante o treinamento (modelo_random_forest e X_teste_final)

mae_random_forest = avaliar_modelo(y_teste, previsoes_random_forest)  # Nosso erro médio absoluto do Random Forest nos dados de teste (mae_random_forest), compare os valores reais de teste com os valores previstos pelo Random Forest (y_teste e previsoes_random_forest)

print("\nErro médio absoluto do Random Forest nos dados de teste (MAE):")  # Exibe o título do erro médio absoluto do Random Forest nos dados de teste (MAE)

print(f"R$ {mae_random_forest:.2f}")  # Nosso erro médio absoluto dos dados de teste (mae_random_forest), exibe o valor médio que o modelo errou nos dados que nunca viu durante o treinamento em reais com duas casas decimais