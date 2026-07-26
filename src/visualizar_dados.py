import seaborn as sns  # Importa o Seaborn
import matplotlib.pyplot as plt  # Importa o Matplotlib


def visualizar_dados(df):  # Função responsável pela visualização dos dados

    dados = df["cidade_loja"].value_counts().head(10).reset_index()  # Conta as vendas e seleciona as 10 cidades com mais vendas

    sns.barplot(data=dados, x="cidade_loja", y="count")  # Cria o gráfico de barras

    plt.title("Quantidade de vendas por cidade")  # Define o título do gráfico
    plt.xlabel("Cidade")  # Define o nome do eixo X
    plt.ylabel("Quantidade de vendas")  # Define o nome do eixo Y
    plt.xticks(rotation=45)  # Inclina os nomes das cidades
    plt.show()  # Exibe o gráfico