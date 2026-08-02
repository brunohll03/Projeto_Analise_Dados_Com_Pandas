
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
