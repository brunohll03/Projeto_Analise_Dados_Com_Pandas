from sklearn.model_selection import train_test_split  # Importa a função responsável por separar os dados de treino e teste
from sklearn.preprocessing import OneHotEncoder       # Importa a função responsável por transformar categorias em números
import numpy as np  # Nossa biblioteca NumPy (np), utilizada para manipular e juntar os dados



def preparar_modelo(df):  # Função responsável por preparar os dados para o Machine Learning

    X = df[["idade", "estado", "marca", "categoria", "ano_moto", "cidade_loja"]]  # Define as variáveis utilizadas para fazer a previsão
    y = df["valor_moto"]  # Define a variável que queremos prever

    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)  # Divide 80% dos dados para treino e 20% para teste

    colunas_categoricas = ["estado", "marca", "categoria", "cidade_loja"]  # Nossas colunas categóricas (colunas_categoricas), que possuem informações em formato de texto

    colunas_numericas = ["idade", "ano_moto"]  # Nossas colunas numéricas (colunas_numericas), que possuem informações em formato de número

    encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)  # Nosso encoder (encoder), transforme as categorias em números (OneHotEncoder) e ignore categorias novas que não apareceram no treinamento (handle_unknown="ignore", sparse_output=False)

    X_treino_categorico = encoder.fit_transform(X_treino[colunas_categoricas])  # Nossos dados categóricos de treinamento (X_treino_categorico), aprendendo e transformando as categorias em números (fit_transform)

    X_teste_categorico = encoder.transform(X_teste[colunas_categoricas])  # Nossos dados categóricos de teste (X_teste_categorico), transformando as categorias utilizando o encoder que já aprendeu no treinamento (transform)

    X_treino_numerico = X_treino[colunas_numericas].values  # Nossos dados numéricos de treinamento (X_treino_numerico), convertendo as colunas numéricas para um array de valores (.values)

    X_teste_numerico = X_teste[colunas_numericas].values  # Nossos dados numéricos de teste (X_teste_numerico), convertendo as colunas numéricas para um array de valores (.values)

    X_treino_final = np.hstack((X_treino_numerico, X_treino_categorico))  # Nossos dados finais de treinamento (X_treino_final), juntando os dados numéricos e categóricos lado a lado (np.hstack)

    X_teste_final = np.hstack((X_teste_numerico, X_teste_categorico))  # Nossos dados finais de teste (X_teste_final), juntando os dados numéricos e categóricos lado a lado (np.hstack)

    return X_treino_final, X_teste_final, y_treino, y_teste  # Nossos resultados finais (return), retornando os dados preparados e nosso encoder que aprendeu as categorias (X_treino_final, X_teste_final, y_treino, y_teste, encoder)