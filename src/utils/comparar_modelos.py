# Arquivo responsável por comparar os resultados obtidos pelos modelos treinados.


def comparar_modelos(mae_regressao_linear, mae_random_forest_treino, mae_random_forest_teste):  # Nossa função (comparar_modelos), compare os erros médios absolutos (MAE) dos modelos treinados

    print("\n==============================")  # Exiba uma linha para iniciar a tabela de resultados

    print("RESULTADOS DOS MODELOS")  # Exiba o título da comparação dos modelos

    print("==============================")  # Exiba uma linha para finalizar o cabeçalho

    print(f"{'Modelo':<30} {'MAE'}")  # Exiba o cabeçalho da tabela contendo o nome do modelo e seu erro médio absoluto (MAE)

    print("-" * 45)  # Exiba uma linha separando o cabeçalho dos resultados

    print(f"{'Regressão Linear':<30} R$ {mae_regressao_linear:.2f}")  # Exiba o erro médio absoluto (mae_regressao_linear) da Regressão Linear

    print(f"{'Random Forest (Treino)':<30} R$ {mae_random_forest_treino:.2f}")  # Exiba o erro médio absoluto (mae_random_forest_treino) do Random Forest durante o treinamento

    print(f"{'Random Forest (Teste)':<30} R$ {mae_random_forest_teste:.2f}")  # Exiba o erro médio absoluto (mae_random_forest_teste) do Random Forest durante o teste