# Arquivo principal responsável por executar o fluxo de processamento dos dados.
# Neste arquivo as funções de carregamento, limpeza, análise, visualização
# e preparação para Machine Learning são organizadas para executar o pipeline completo.


from src.carregar_dados import carregar_dados  # Nossa função para carregar os dados (carregar_dados)
from src.limpar_dados import limpar_dados  # Nossa função para limpar os dados (limpar_dados)
from src.analisar_dados import analisar_dados  # Nossa função para analisar os dados (analisar_dados)
from src.visualizar_dados import visualizar_dados  # Nossa função para visualizar os dados (visualizar_dados)
from src.preparar_modelo import preparar_modelo  # Nossa função para preparar os dados para Machine Learning (preparar_modelo)
from src.avaliar_modelo import avaliar_modelo  # Nossa função para avaliar o modelo (avaliar_modelo)
from src.utils.comparar_modelos import comparar_modelos  # Nossa função para comparar os resultados dos modelos (comparar_modelos)

# Treinos
from src.modelos.treinar_regressao_linear import treinar_regressao_linear  # Nossa função para treinar o modelo de Regressão Linear (treinar_regressao_linear)
from src.modelos.treinar_random_forest import treinar_random_forest  # Nossa função para treinar o modelo Random Forest (treinar_random_forest)
from src.modelos.treinar_decision_tree import treinar_decision_tree  # Nossa função para treinar o modelo Decision Tree (treinar_decision_tree)

# Previsões
from src.modelos.prever_modelo import fazer_previsao  # Nossa função para realizar previsões utilizando um modelo treinado (fazer_previsao)


df = carregar_dados()  # Nosso DataFrame (df), carregue os dados do arquivo CSV (carregar_dados)

df = limpar_dados(df)  # Nosso DataFrame (df), limpe os dados utilizando nossa função de limpeza (limpar_dados)

df.to_csv("data/processed/atendimentos_limpos.csv", index=False)  # Nosso DataFrame (df), salve os dados limpos em um novo arquivo CSV (to_csv)

print("\nDados limpos salvos com sucesso!")  # Informa que nossos dados limpos foram salvos com sucesso

analisar_dados(df)  # Nossa análise dos dados (analisar_dados), analise nosso DataFrame já limpo (df)

# visualizar_dados(df)  # Nossa visualização dos dados (visualizar_dados), visualize nosso DataFrame já limpo (df)

X_treino_final, X_teste_final, y_treino, y_teste = preparar_modelo(df)  # Nossos dados preparados (X_treino_final, X_teste_final, y_treino e y_teste), separe os dados para treinamento e teste (preparar_modelo)


# ==============================
# REGRESSÃO LINEAR
# ==============================

modelo_regressao_linear = treinar_regressao_linear(X_treino_final, y_treino)  # Nosso modelo de Regressão Linear (modelo_regressao_linear), treine utilizando os dados de treinamento (X_treino_final e y_treino)

previsoes_regressao_linear = fazer_previsao(modelo_regressao_linear, X_teste_final)  # Nossas previsões da Regressão Linear (previsoes_regressao_linear), utilize o modelo treinado para prever os dados de teste (modelo_regressao_linear e X_teste_final)

mae_regressao_linear = avaliar_modelo(y_teste, previsoes_regressao_linear)  # Nosso erro médio absoluto da Regressão Linear (mae_regressao_linear), compare os valores reais com os previstos (y_teste e previsoes_regressao_linear)


# ==============================
# DECISION TREE
# ==============================

# Será implementada quando estudarmos o algoritmo.
#
# modelo_decision_tree = treinar_decision_tree(X_treino_final, y_treino)  # Nosso modelo Decision Tree (modelo_decision_tree), treine utilizando os dados de treinamento (X_treino_final e y_treino)
#
# previsoes_decision_tree = fazer_previsao(modelo_decision_tree, X_teste_final)  # Nossas previsões da Decision Tree (previsoes_decision_tree), utilize o modelo treinado para prever os dados de teste (modelo_decision_tree e X_teste_final)
#
# mae_decision_tree = avaliar_modelo(y_teste, previsoes_decision_tree)  # Nosso erro médio absoluto da Decision Tree (mae_decision_tree), compare os valores reais com os previstos (y_teste e previsoes_decision_tree)


# ==============================
# RANDOM FOREST
# ==============================

modelo_random_forest = treinar_random_forest(X_treino_final, y_treino)  # Nosso modelo Random Forest (modelo_random_forest), treine utilizando os dados de treinamento (X_treino_final e y_treino)

previsoes_random_forest_treino = fazer_previsao(modelo_random_forest, X_treino_final)  # Nossas previsões do treinamento (previsoes_random_forest_treino), utilize o modelo treinado para prever os dados de treinamento (modelo_random_forest e X_treino_final)

previsoes_random_forest_teste = fazer_previsao(modelo_random_forest, X_teste_final)  # Nossas previsões do teste (previsoes_random_forest_teste), utilize o modelo treinado para prever os dados de teste (modelo_random_forest e X_teste_final)

mae_random_forest_treino = avaliar_modelo(y_treino, previsoes_random_forest_treino)  # Nosso erro médio absoluto do treinamento (mae_random_forest_treino), compare os valores reais com os previstos (y_treino e previsoes_random_forest_treino)

mae_random_forest_teste = avaliar_modelo(y_teste, previsoes_random_forest_teste)  # Nosso erro médio absoluto do teste (mae_random_forest_teste), compare os valores reais com os previstos (y_teste e previsoes_random_forest_teste)


# ==============================
# COMPARAÇÃO DOS MODELOS
# ==============================

comparar_modelos(mae_regressao_linear, mae_random_forest_treino, mae_random_forest_teste)  # Nossa comparação dos modelos (comparar_modelos), compare os erros médios absolutos (MAE) dos modelos treinados