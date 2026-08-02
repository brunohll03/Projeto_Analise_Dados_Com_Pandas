# Arquivo principal responsável por executar o fluxo de processamento dos dados.
# Neste arquivo as funções de carregamento, limpeza, análise, visualização
# e preparação para Machine Learning são organizadas para executar o pipeline completo.


from src.utils.gerar_dados import gerar_dados  # Nossa função para gerar dados sintéticos (gerar_dados)

from src.carregar_dados import carregar_dados  # Nossa função para carregar os dados (carregar_dados)
from src.limpar_dados import limpar_dados  # Nossa função para limpar os dados (limpar_dados)
from src.preparar_modelo import preparar_modelo  # Nossa função para preparar os dados para Machine Learning (preparar_modelo)
from src.avaliar_modelo import avaliar_modelo, validar_modelo  # Nossas funções para avaliar o modelo (avaliar_modelo) e validar utilizando Cross Validation (validar_modelo)
from src.utils.comparar_modelos import comparar_modelos  # Nossa função para comparar os resultados dos modelos (comparar_modelos)


# Treinos

from src.modelos.treinar_regressao_linear import treinar_regressao_linear  # Nossa função para treinar o modelo de Regressão Linear (treinar_regressao_linear)
from src.modelos.treinar_random_forest import treinar_random_forest  # Nossa função para treinar o modelo Random Forest (treinar_random_forest)
from src.modelos.treinar_decision_tree import treinar_decision_tree  # Nossa função para treinar o modelo Decision Tree (treinar_decision_tree)
from src.modelos.treinar_gradient_boosting import treinar_gradient_boosting  # Nossa função para treinar o modelo Gradient Boosting (treinar_gradient_boosting)
from src.modelos.treinar_xgboost import treinar_xgboost  # Nossa função para treinar o modelo XGBoost (treinar_xgboost)


# Previsões

from src.modelos.prever_modelo import fazer_previsao  # Nossa função para realizar previsões utilizando um modelo treinado (fazer_previsao)



# ==============================
# GERAÇÃO DOS DADOS
# ==============================

gerar_dados(
    quantidade=2000,
    caminho="data/raw/atendimentos_expandido.csv"
)  # Nossa função (gerar_dados), crie uma nova base sintética com 2000 registros para treinamento dos modelos



# ==============================
# CARREGAMENTO E LIMPEZA DOS DADOS
# ==============================

df = carregar_dados()  # Nosso DataFrame (df), carregue os dados do arquivo CSV (carregar_dados)

df = limpar_dados(df)  # Nosso DataFrame (df), limpe os dados utilizando nossa função de limpeza (limpar_dados)

df.to_csv(
    "data/processed/atendimentos_limpos.csv",
    index=False
)  # Nosso DataFrame (df), salve os dados limpos em um novo arquivo CSV

print("\nDados limpos salvos com sucesso!")  # Informa que os dados limpos foram salvos



# ==============================
# PREPARAÇÃO DOS MODELOS
# ==============================

X_treino_final, X_teste_final, y_treino, y_teste = preparar_modelo(df)  # Nossos dados preparados (X_treino_final, X_teste_final, y_treino e y_teste), separe os dados para treinamento e teste



# ==============================
# REGRESSÃO LINEAR
# ==============================

modelo_regressao_linear = treinar_regressao_linear(
    X_treino_final,
    y_treino
)  # Nosso modelo de Regressão Linear, treine utilizando os dados de treinamento


previsoes_regressao_linear = fazer_previsao(
    modelo_regressao_linear,
    X_teste_final
)  # Nossas previsões da Regressão Linear


mae_regressao_linear_teste, rmse_regressao_linear_teste, r2_regressao_linear_teste = avaliar_modelo(
    y_teste,
    previsoes_regressao_linear
)  # Nossos indicadores MAE, RMSE e R² da Regressão Linear


mae_regressao_linear_cv = validar_modelo(
    modelo_regressao_linear,
    X_treino_final,
    y_treino
)  # Nosso MAE médio da validação cruzada



# ==============================
# RANDOM FOREST
# ==============================

modelo_random_forest = treinar_random_forest(
    X_treino_final,
    y_treino
)  # Nosso modelo Random Forest


previsoes_random_forest_teste = fazer_previsao(
    modelo_random_forest,
    X_teste_final
)  # Nossas previsões do Random Forest


mae_random_forest_teste, rmse_random_forest_teste, r2_random_forest_teste = avaliar_modelo(
    y_teste,
    previsoes_random_forest_teste
)  # Nossos indicadores MAE, RMSE e R² do Random Forest


mae_random_forest_cv = validar_modelo(
    modelo_random_forest,
    X_treino_final,
    y_treino
)  # Nosso MAE médio da validação cruzada



# ==============================
# DECISION TREE
# ==============================

modelo_decision_tree = treinar_decision_tree(
    X_treino_final,
    y_treino
)  # Nosso modelo Decision Tree


previsoes_decision_tree_teste = fazer_previsao(
    modelo_decision_tree,
    X_teste_final
)  # Nossas previsões da Decision Tree


mae_decision_tree_teste, rmse_decision_tree_teste, r2_decision_tree_teste = avaliar_modelo(
    y_teste,
    previsoes_decision_tree_teste
)  # Nossos indicadores MAE, RMSE e R² da Decision Tree


mae_decision_tree_cv = validar_modelo(
    modelo_decision_tree,
    X_treino_final,
    y_treino
)  # Nosso MAE médio da validação cruzada



# ==============================
# GRADIENT BOOSTING
# ==============================

modelo_gradient_boosting = treinar_gradient_boosting(
    X_treino_final,
    y_treino
)  # Nosso modelo Gradient Boosting


previsoes_gradient_boosting_teste = fazer_previsao(
    modelo_gradient_boosting,
    X_teste_final
)  # Nossas previsões do Gradient Boosting


mae_gradient_boosting_teste, rmse_gradient_boosting_teste, r2_gradient_boosting_teste = avaliar_modelo(
    y_teste,
    previsoes_gradient_boosting_teste
)  # Nossos indicadores MAE, RMSE e R² do Gradient Boosting


mae_gradient_boosting_cv = validar_modelo(
    modelo_gradient_boosting,
    X_treino_final,
    y_treino
)  # Nosso MAE médio da validação cruzada



# ==============================
# XGBOOST
# ==============================

modelo_xgboost = treinar_xgboost(
    X_treino_final,
    y_treino
)  # Nosso modelo XGBoost


previsoes_xgboost_teste = fazer_previsao(
    modelo_xgboost,
    X_teste_final
)  # Nossas previsões do XGBoost


mae_xgboost_teste, rmse_xgboost_teste, r2_xgboost_teste = avaliar_modelo(
    y_teste,
    previsoes_xgboost_teste
)  # Nossos indicadores MAE, RMSE e R² do XGBoost


mae_xgboost_cv = validar_modelo(
    modelo_xgboost,
    X_treino_final,
    y_treino
)  # Nosso MAE médio da validação cruzada



# ==============================
# COMPARAÇÃO DOS MODELOS
# ==============================

comparar_modelos(
    mae_regressao_linear_teste,
    rmse_regressao_linear_teste,
    r2_regressao_linear_teste,
    mae_regressao_linear_cv,

    mae_random_forest_teste,
    rmse_random_forest_teste,
    r2_random_forest_teste,
    mae_random_forest_cv,

    mae_decision_tree_teste,
    rmse_decision_tree_teste,
    r2_decision_tree_teste,
    mae_decision_tree_cv,

    mae_gradient_boosting_teste,
    rmse_gradient_boosting_teste,
    r2_gradient_boosting_teste,
    mae_gradient_boosting_cv,

    mae_xgboost_teste,
    rmse_xgboost_teste,
    r2_xgboost_teste,
    mae_xgboost_cv

)  # Nossa comparação dos modelos utilizando MAE, RMSE, R² e Cross Validation