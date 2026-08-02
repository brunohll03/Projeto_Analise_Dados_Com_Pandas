# Arquivo responsável por comparar os resultados obtidos pelos modelos treinados.


def comparar_modelos(
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

):  # Nossa função (comparar_modelos), compare os modelos utilizando MAE, RMSE, R² e Cross Validation


    print("\n==============================")  # Exiba uma linha para iniciar a tabela de resultados

    print("RESULTADOS DOS MODELOS")  # Exiba o título da comparação dos modelos

    print("==============================")  # Exiba uma linha para finalizar o cabeçalho


    print(
        f"{'Modelo':<30} {'MAE Teste':<15} {'RMSE Teste':<15} {'R² Teste':<12} {'MAE CV'}"
    )  # Exiba o cabeçalho da tabela contendo modelo, MAE, RMSE, R² e validação cruzada


    print("-" * 90)  # Exiba uma linha separando o cabeçalho dos resultados


    print(
        f"{'Regressão Linear':<30} R$ {mae_regressao_linear_teste:<10.2f} R$ {rmse_regressao_linear_teste:<10.2f} {r2_regressao_linear_teste:<10.2f} R$ {mae_regressao_linear_cv:.2f}"
    )  # Exiba os resultados da Regressão Linear utilizando MAE, RMSE, R² e Cross Validation


    print(
        f"{'Random Forest':<30} R$ {mae_random_forest_teste:<10.2f} R$ {rmse_random_forest_teste:<10.2f} {r2_random_forest_teste:<10.2f} R$ {mae_random_forest_cv:.2f}"
    )  # Exiba os resultados do Random Forest utilizando MAE, RMSE, R² e Cross Validation


    print(
        f"{'Decision Tree':<30} R$ {mae_decision_tree_teste:<10.2f} R$ {rmse_decision_tree_teste:<10.2f} {r2_decision_tree_teste:<10.2f} R$ {mae_decision_tree_cv:.2f}"
    )  # Exiba os resultados da Decision Tree utilizando MAE, RMSE, R² e Cross Validation


    print(
        f"{'Gradient Boosting':<30} R$ {mae_gradient_boosting_teste:<10.2f} R$ {rmse_gradient_boosting_teste:<10.2f} {r2_gradient_boosting_teste:<10.2f} R$ {mae_gradient_boosting_cv:.2f}"
    )  # Exiba os resultados do Gradient Boosting utilizando MAE, RMSE, R² e Cross Validation


    print(
        f"{'XGBoost':<30} R$ {mae_xgboost_teste:<10.2f} R$ {rmse_xgboost_teste:<10.2f} {r2_xgboost_teste:<10.2f} R$ {mae_xgboost_cv:.2f}"
    )  # Exiba os resultados do XGBoost utilizando MAE, RMSE, R² e Cross Validation