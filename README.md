# Projeto de Análise de Dados

Projeto desenvolvido para aprendizado de manipulação e análise de dados utilizando Python e Pandas.

## Objetivo

O objetivo deste projeto é analisar dados fictícios de atendimentos médicos, aplicando conceitos de:

* Python
* Pandas
* NumPy
* Manipulação de dados
* Limpeza de dados
* Análise exploratória
* Visualização de dados

## Tecnologias utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

## Estrutura do projeto

```text
projeto_analise_dados/
│
├── data/
│   ├── raw/
│   │   ├── atendimentos.csv
│   │   └── atendimentos_sinteticos.csv
│   └── processed/
│       └── atendimentos_limpos.csv
│
├── notebooks/
│
├── src/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── prever_modelo.py
│   │   ├── treinar_regressao_linear.py
│   │   ├── treinar_decision_tree.py
│   │   ├── treinar_random_forest.py
│   │   ├── treinar_gradient_boosting.py
│   │   └── treinar_xgboost.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── comparar_modelos.py
│   │   ├── interpretar_modelo.py
│   │   └── gerar_dados.py
│   │
│   ├── __init__.py
│   ├── carregar_dados.py
│   ├── limpar_dados.py
│   ├── analisar_dados.py
│   ├── visualizar_dados.py
│   ├── preparar_modelo.py
│   └── avaliar_modelo.py
│
├── models/
│   └── melhor_modelo.pkl
│
├── .venv/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Instalação

```
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
.\venv\Scripts\Activate.ps1

# Instalar as dependências
pip install -r requirements.txt
```

## Execução

Com o ambiente virtual ativado:

```
python main.py
```

## Fluxo do Projeto

```text
Arquivo CSV bruto
       |
       v
Carregamento dos dados
       |
       v
Limpeza e tratamento
       |
       v
Padronização dos dados
       |
       v
Análise exploratória (EDA)
       |
       v
Geração de informações
       |
       v
Arquivo CSV tratado
```

### Técnicamente 

```text
CSV (Raw)
   |
   v
carregar_dados()
   |
   v
DataFrame
   |
   v
limpar_dados()
   |
   v
DataFrame Limpo
   |
   v
analisar_dados()
   |
   v
Análise Exploratória (EDA)
   |
   v
CSV (Processed)
```

## Comandos e Métodos do Pandas

| Comando / Método                                    | O que faz                                                                    |
| --------------------------------------------------- | ---------------------------------------------------------------------------- |
| `import pandas as pd`                               | Importa a biblioteca Pandas                                                  |
| `pd.read_csv()`                                     | Lê um arquivo CSV e cria um DataFrame                                        |
| `df`                                                | Exibe o DataFrame                                                            |
| `df.shape`                                          | Mostra a quantidade de linhas e colunas                                      |
| `df.info()`                                         | Mostra informações sobre colunas, tipos de dados e valores não nulos         |
| `df.describe()`                                     | Gera estatísticas descritivas das colunas numéricas                          |
| `df.isnull()`                                       | Identifica valores ausentes                                                  |
| `df.isnull().sum()`                                 | Conta os valores ausentes de cada coluna                                     |
| `df["coluna"]`                                      | Acessa uma coluna específica                                                 |
| `df["coluna"].unique()`                             | Mostra os valores únicos de uma coluna                                       |
| `df["coluna"].value_counts()`                       | Conta a frequência de cada valor                                             |
| `df["coluna"].value_counts().idxmax()`              | Retorna o valor mais frequente                                               |
| `df["coluna"].value_counts().max()`                 | Retorna a maior frequência encontrada                                        |
| `len(df)`                                           | Retorna a quantidade de linhas do DataFrame                                  |
| `df["coluna"].mean()`                               | Calcula a média                                                              |
| `df["coluna"].median()`                             | Calcula a mediana                                                            |
| `df["coluna"].min()`                                | Retorna o menor valor                                                        |
| `df["coluna"].max()`                                | Retorna o maior valor                                                        |
| `df["coluna"].sum()`                                | Soma os valores                                                              |
| `df["coluna"].std()`                                | Calcula o desvio padrão                                                      |
| `df["coluna"].var()`                                | Calcula a variância                                                          |
| `df["coluna"].count()`                              | Conta os valores não nulos                                                   |
| `df["coluna"].nunique()`                            | Conta quantos valores únicos existem                                         |
| `df["coluna"].first()`                              | Retorna o primeiro valor                                                     |
| `df["coluna"].last()`                               | Retorna o último valor                                                       |
| `df["coluna"].prod()`                               | Multiplica todos os valores                                                  |
| `df["coluna"].sem()`                                | Calcula o erro padrão da média                                               |
| `df["coluna"].quantile()`                           | Calcula um quantil                                                           |
| `df["coluna"].agg()`                                | Aplica uma ou várias funções de agregação                                    |
| `df.groupby()`                                      | Agrupa os dados por uma ou mais colunas                                      |
| `df.groupby().size()`                               | Conta a quantidade de registros em cada grupo                                |
| `df.groupby().count()`                              | Conta valores não nulos em cada grupo                                        |
| `df.groupby().mean()`                               | Calcula a média de cada grupo                                                |
| `df.groupby().agg()`                                | Aplica várias funções de agregação em cada grupo                             |
| `df.groupby(["coluna1", "coluna2"])`                | Agrupa os dados usando duas ou mais colunas                                  |
| `.unstack()`                                        | Transforma níveis de um índice em colunas                                    |
| `.unstack(fill_value=0)`                            | Transforma níveis do índice em colunas e substitui valores ausentes por zero |
| `df.sort_values()`                                  | Ordena os registros por uma coluna                                           |
| `df.sort_values(ascending=False)`                   | Ordena os registros em ordem decrescente                                     |
| `df.sort_values(["coluna1", "coluna2"])`            | Ordena usando várias colunas                                                 |
| `df[df["coluna"] > valor]`                          | Filtra registros com base em uma condição                                    |
| `df[df["coluna"] == valor]`                         | Filtra registros que possuem um valor específico                             |
| `&`                                                 | Representa uma condição E                                                    |
| `\|`                                                | Representa uma condição OU                                                   |
| `df.loc[]`                                          | Permite selecionar e filtrar linhas e colunas                                |
| `df.loc[condição]`                                  | Filtra linhas usando uma condição                                            |
| `df.loc[condição, ["coluna1", "coluna2"]]`          | Filtra linhas e seleciona colunas específicas                                |
| `df.loc[condição, "coluna"] = valor`                | Altera valores de uma coluna quando uma condição é atendida                  |
| `df["coluna"].duplicated()`                         | Identifica valores duplicados                                                |
| `df["coluna"].duplicated(keep=False)`               | Identifica todos os registros que possuem valores duplicados                 |
| `df.drop_duplicates()`                              | Remove registros duplicados                                                  |
| `df.drop_duplicates(subset="coluna")`               | Remove duplicados considerando uma coluna específica                         |
| `df.drop_duplicates(subset="coluna", keep="first")` | Remove duplicados mantendo o primeiro registro                               |
| `.str.strip()`                                      | Remove espaços no início e no final de textos                                |
| `.str.lower()`                                      | Converte textos para letras minúsculas                                       |
| `.fillna()`                                         | Preenche valores ausentes                                                    |
| `pd.NA`                                             | Representa um valor ausente                                                  |
| `df["coluna"].quantile(0.25)`                       | Calcula o primeiro quartil                                                   |
| `df["coluna"].quantile(0.50)`                       | Calcula o segundo quartil ou mediana                                         |
| `df["coluna"].quantile(0.75)`                       | Calcula o terceiro quartil                                                   |
| `df.head()`                                         | Exibe as primeiras linhas do DataFrame                                       |
| `df.tail()`                                         | Exibe as últimas linhas do DataFrame                                         |
| `df.sample()`                                       | Exibe registros aleatórios do DataFrame                                      |
| `df.copy()`                                         | Cria uma cópia independente do DataFrame                                     |
| `df.rename()`                                       | Renomeia colunas ou índices                                                  |
| `df.reset_index()`                                  | Reseta o índice do DataFrame                                                 |
| `df.set_index()`                                    | Define uma coluna como índice                                                |
| `df.sort_index()`                                   | Ordena o DataFrame pelo índice                                               |
| `df["coluna"].isin()`                               | Verifica se os valores pertencem a uma lista de valores                      |
| `df["coluna"].between()`                            | Filtra valores dentro de um intervalo                                        |
| `df["coluna"].str.contains()`                       | Verifica se um texto contém determinado padrão                               |
| `df["coluna"].str.replace()`                        | Substitui partes de textos                                                   |
| `df["coluna"].str.upper()`                          | Converte textos para letras maiúsculas                                       |
| `df["coluna"].str.title()`                          | Converte textos para formato de título                                       |
| `df["coluna"].astype()`                             | Converte o tipo de dados de uma coluna                                       |
| `pd.to_numeric()`                                   | Converte valores para formato numérico                                       |
| `pd.to_datetime()`                                  | Converte valores para formato de data e hora                                 |
| `df["data"].dt.year`                                | Extrai o ano de uma coluna de data                                           |
| `df["data"].dt.month`                               | Extrai o mês de uma coluna de data                                           |
| `df["data"].dt.day`                                 | Extrai o dia de uma coluna de data                                           |
| `df["coluna"].apply()`                              | Aplica uma função aos valores de uma coluna                                  |
| `df.apply()`                                        | Aplica uma função a linhas ou colunas do DataFrame                           |
| `df.map()`                                          | Aplica uma função elemento por elemento em uma Series                        |
| `df.replace()`                                      | Substitui valores específicos                                                |
| `df.drop()`                                         | Remove linhas ou colunas                                                     |
| `df.dropna()`                                       | Remove registros que possuem valores ausentes                                |
| `df.fillna()`                                       | Preenche valores ausentes                                                    |
| `pd.concat()`                                       | Concatena DataFrames ou Series                                               |
| `pd.merge()`                                        | Combina DataFrames usando colunas relacionadas                               |
| `df.pivot_table()`                                  | Cria tabelas dinâmicas para análise                                          |
| `pd.crosstab()`                                     | Cria tabelas de frequência cruzando variáveis                                |
| `df.corr()`                                         | Calcula a correlação entre colunas numéricas                                 |
| `df.memory_usage()`                                 | Mostra o uso de memória do DataFrame                                         |
| `df.dtypes`                                         | Mostra o tipo de dados de cada coluna                                        |
| `df.columns`                                        | Mostra os nomes das colunas                                                  |
| `df.index`                                          | Mostra o índice do DataFrame                                                 |


## Funções Python Utilizadas

| Comando | O que faz | Status |
|---|---|---|
| `print()` | Exibe uma informação ou resultado no console | Estudado |
| `len()` | Conta quantos elementos ou registros existem | Estudado |
| `def` | Define uma função personalizada para executar uma tarefa específica | Estudado |
| `lambda` | Cria uma função simples e anônima para executar uma operação | Estudado |

## Limpeza de dados expectativas base:

| Situação encontrada | Exemplo | O que fazer |
|---|---|---|
| Espaços extras | `"  Campinas  "` | Remover espaços das laterais |
| Maiúsculas e minúsculas | `"CAMPINAS"`, `"Campinas"`, `"campinas"` | Padronizar para um único formato |
| Texto duplicado | `"cardiologia"`, `"Cardiologia"` | Padronizar para considerar como o mesmo valor |
| Registro totalmente duplicado | Mesmo paciente e todos os dados repetidos | Remover o registro duplicado |
| Email duplicado | Dois pacientes com o mesmo email | Investigar e decidir qual registro manter |
| Idade ausente | `idade = vazio` | Preencher, remover ou manter como ausente, dependendo da regra |
| Idade inválida | `idade = -5` | Considerar como inválida e corrigir ou transformar em ausente |
| Idade impossível | `idade = 150` | Considerar como inválida e corrigir ou transformar em ausente |
| Status inválido | `"canceladoo"` | Corrigir para `"cancelado"` |
| Status desconhecido | `"???"` | Investigar e corrigir ou marcar como inválido |
| Email inválido | `"joao.gmail.com"` | Identificar como email potencialmente inválido |
| Cidade inconsistente | `"São Paulo"`, `"sao paulo"`, `"Sao Paulo"` | Padronizar os valores |
| Cidade com informação extra | `"Campinas - SP"` | Remover a informação desnecessária, se a regra exigir |
| Especialidade com erro | `"cardiologoa"` | Corrigir para `"cardiologia"` |
| Campo numérico como texto | `"25"` | Converter para número |
| Data como texto | `"24/07/2026"` | Converter para formato de data |
| Data inválida | `"32/15/2026"` | Identificar e corrigir ou considerar inválida |
| Status ausente | `status = vazio` | Investigar e definir como tratar |
| Categoria inesperada | Especialidade `"xyz"` | Verificar se é válida ou corrigir |
| Dados fora da regra | Atendimento com status `"concluido"` sem data de atendimento | Investigar a inconsistência |
| Registros conflitantes | Mesmo email com nomes diferentes | Investigar qual informação é correta |
| Valores ausentes excessivos | Muitas idades vazias | Avaliar a qualidade da coluna antes de preencher |
| Coluna desnecessária | Coluna sem utilidade para a análise | Avaliar a possibilidade de remover |
| Dados após limpeza | Ainda existem duplicados ou valores inválidos | Fazer uma nova validação |



# Projeto de Análise de Dados e Machine Learning - Previsão de Valor de Motos

Projeto desenvolvido para aprendizado de análise de dados, manipulação de informações e aplicação de modelos de Machine Learning utilizando Python.

O projeto simula um cenário de vendas de motocicletas, realizando todo o fluxo de tratamento de dados, análise exploratória e treinamento de modelos de regressão para previsão de valores.

---

# Objetivo

O objetivo deste projeto é desenvolver um pipeline completo de análise de dados e Machine Learning para prever o valor de motocicletas utilizando dados históricos de vendas.

Durante o desenvolvimento foram aplicados conceitos de:

- Python
- Pandas
- NumPy
- Manipulação de dados
- Limpeza de dados
- Tratamento de inconsistências
- Análise exploratória (EDA)
- Visualização de dados
- Preparação de dados para Machine Learning
- Treinamento de modelos de regressão
- Avaliação e comparação de modelos

---

# Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Jupyter Notebook

---

# Estrutura do projeto

```text
projeto_analise_dados/
│
├── data/
│   ├── raw/
│   │   ├── atendimentos.csv
│   │   └── atendimentos_sinteticos.csv
│   │
│   └── processed/
│       └── atendimentos_limpos.csv
│
├── notebooks/
│
├── src/
│   │
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── prever_modelo.py
│   │   ├── treinar_regressao_linear.py
│   │   ├── treinar_decision_tree.py
│   │   ├── treinar_random_forest.py
│   │   ├── treinar_gradient_boosting.py
│   │   └── treinar_xgboost.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── comparar_modelos.py
│   │   ├── interpretar_modelo.py
│   │   └── gerar_dados.py
│   │
│   ├── __init__.py
│   ├── carregar_dados.py
│   ├── limpar_dados.py
│   ├── analisar_dados.py
│   ├── visualizar_dados.py
│   ├── preparar_modelo.py
│   └── avaliar_modelo.py
│
├── models/
│   └── melhor_modelo.pkl
│
├── .venv/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

# Instalação

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente virtual:

```bash
.\venv\Scripts\Activate.ps1
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

---

# Execução

Com o ambiente virtual ativado:

```bash
python main.py
```

---

# Fluxo do projeto

```text
Geração dos dados
        |
        v
Arquivo CSV bruto
        |
        v
Carregamento dos dados
        |
        v
Limpeza e tratamento
        |
        v
Padronização dos dados
        |
        v
Análise exploratória (EDA)
        |
        v
Preparação para Machine Learning
        |
        v
Treinamento dos modelos
        |
        v
Avaliação dos resultados
        |
        v
Comparação dos modelos
        |
        v
Escolha do melhor modelo
```

---

# Fluxo técnico

```text
gerar_dados()

       |
       v

CSV Raw

       |
       v

carregar_dados()

       |
       v

DataFrame

       |
       v

limpar_dados()

       |
       v

DataFrame Limpo

       |
       v

analisar_dados()

       |
       v

Análise Exploratória (EDA)

       |
       v

preparar_modelo()

       |
       v

Treinamento dos modelos

       |
       v

avaliar_modelo()

       |
       v

comparar_modelos()
```

---


# Machine Learning - Regressão

O projeto utiliza aprendizado supervisionado para prever valores numéricos de motocicletas.

Objetivo:

```
Prever:
valor_moto
```

Os modelos recebem dados históricos de vendas e aprendem padrões entre características como:

- Marca
- Modelo
- Categoria
- Ano da moto
- Idade do cliente
- Cidade
- Loja
- Forma de pagamento

---

# Modelos utilizados

Foram aplicados diferentes algoritmos de regressão para comparação de desempenho:

| Modelo | Descrição |
|---|---|
| Regressão Linear | Modelo inicial para identificar relações lineares |
| Decision Tree | Modelo baseado em regras de decisão |
| Random Forest | Conjunto de árvores para melhorar estabilidade |
| Gradient Boosting | Modelo sequencial que corrige erros anteriores |
| XGBoost | Algoritmo otimizado baseado em boosting |

---

# Avaliação dos modelos

Os modelos são comparados utilizando métricas de regressão:

| Métrica | Objetivo |
|---|---|
| MAE | Mede o erro médio das previsões |
| RMSE | Penaliza erros maiores |
| R² | Mede o quanto o modelo explica os dados |
| Cross Validation | Avalia estabilidade e generalização |

---

# Fluxo de Machine Learning

```text
Dados tratados

      |
      v

preparar_modelo()

      |
      v

Separação treino/teste

      |
      v

Treinamento dos modelos

      |
      v

Previsões

      |
      v

Avaliação e comparação

      |
      v

Escolha do melhor modelo
```

---

# Geração de dados sintéticos

O projeto possui uma rotina para criação de dados fictícios para testes de volume e treinamento.

Arquivo:

```
src/utils/gerar_dados.py
```

Objetivos:

- Criar novos registros;
- Simular cenários reais;
- Testar impacto da quantidade de dados nos modelos.

---
