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
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── __init__.py
│   ├── carregar_dados.py
│   ├── limpar_dados.py
│   └── analisar_dados.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
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

| Comando / Método | O que faz | Status |
|---|---|---|
| `import pandas as pd` | Importa a biblioteca Pandas | Estudado |
| `pd.read_csv()` | Lê um arquivo CSV e cria uma tabela DataFrame | Estudado |
| `df` | Exibe a tabela DataFrame | Estudado |
| `df.shape` | Mostra a quantidade de linhas e colunas da tabela DataFrame | Estudado |
| `df.info()` | Mostra informações da tabela DataFrame, como colunas, tipos de dados e valores não nulos | Estudado |
| `df.describe()` | Gera um resumo estatístico das colunas numéricas da tabela DataFrame | Estudado |
| `df.isnull()` | Verifica na tabela DataFrame quais valores estão ausentes | Estudado |
| `df.isnull().sum()` | Verifica na tabela DataFrame e conta quantos valores ausentes existem em cada coluna | Estudado |
| `df["coluna"]` | Acessa na tabela DataFrame uma coluna específica | Estudado |
| `df["coluna"].unique()` | Acessa uma coluna da tabela DataFrame e mostra quais valores únicos existem nela | Estudado |
| `df["coluna"].value_counts()` | Acessa uma coluna da tabela DataFrame e conta quantas vezes cada valor aparece | Estudado |
| `df["coluna"].value_counts().idxmax()` | Acessa uma coluna, conta a frequência dos valores e retorna o valor que aparece mais vezes | Estudado |
| `df["coluna"].value_counts().max()` | Acessa uma coluna, conta a frequência dos valores e retorna a maior quantidade encontrada | Estudado |
| `len(df)` | Conta quantos registros existem na tabela DataFrame | Estudado |
| `df["coluna"].mean()` | Acessa uma coluna da tabela DataFrame e calcula a média dos valores | Estudado |
| `df["coluna"].median()` | Acessa uma coluna da tabela DataFrame e calcula a mediana dos valores | Estudado |
| `df["coluna"].min()` | Acessa uma coluna da tabela DataFrame e retorna o menor valor encontrado | Estudado |
| `df["coluna"].max()` | Acessa uma coluna da tabela DataFrame e retorna o maior valor encontrado | Estudado |
| `df["coluna"].sum()` | Acessa uma coluna da tabela DataFrame e soma todos os valores | Estudado |
| `df["coluna"].std()` | Acessa uma coluna da tabela DataFrame e calcula o desvio padrão dos valores | Estudado |
| `df["coluna"].var()` | Acessa uma coluna da tabela DataFrame e calcula a variância dos valores | Estudado |
| `df["coluna"].count()` | Acessa uma coluna da tabela DataFrame e conta quantos valores não são nulos | Estudado |
| `df["coluna"].nunique()` | Acessa uma coluna da tabela DataFrame e conta quantos valores diferentes existem | Estudado |
| `df["coluna"].first()` | Acessa uma coluna da tabela DataFrame e retorna o primeiro valor encontrado | Estudado |
| `df["coluna"].last()` | Acessa uma coluna da tabela DataFrame e retorna o último valor encontrado | Estudado |
| `df["coluna"].prod()` | Acessa uma coluna da tabela DataFrame e multiplica todos os valores | Estudado |
| `df["coluna"].sem()` | Acessa uma coluna da tabela DataFrame e calcula o erro padrão da média | Estudado |
| `df["coluna"].quantile()` | Acessa uma coluna da tabela DataFrame e calcula um quantil dos valores | Estudado |
| `df["coluna"].agg()` | Acessa uma coluna da tabela DataFrame e aplica uma ou várias funções de agregação | Estudado |
| `df.groupby()` | Agrupa os registros da tabela DataFrame com base em uma ou mais colunas | Estudado |
| `df.groupby().size()` | Agrupa os registros da tabela DataFrame e conta quantos registros existem em cada grupo | Estudado |
| `df.groupby().count()` | Agrupa os registros da tabela DataFrame e conta os valores não nulos de cada grupo | Estudado |
| `df.groupby().mean()` | Agrupa os registros da tabela DataFrame e calcula a média de cada grupo | Estudado |
| `df.groupby().agg()` | Agrupa os registros da tabela DataFrame e aplica várias funções de agregação em cada grupo | Estudado |
| `df.groupby(["coluna1", "coluna2"])` | Agrupa os registros da tabela DataFrame considerando duas ou mais colunas | Estudado |
| `.unstack()` | Transforma níveis do índice do resultado em colunas | Estudado |
| `.unstack(fill_value=0)` | Transforma níveis do índice em colunas e preenche valores ausentes com zero | Estudado |
| `df.sort_values()` | Ordena os registros da tabela DataFrame com base nos valores de uma coluna | Estudado |
| `df.sort_values(ascending=False)` | Ordena os registros da tabela DataFrame do maior valor para o menor | Estudado |
| `df.sort_values(["coluna1", "coluna2"])` | Ordena os registros da tabela DataFrame usando duas ou mais colunas | Estudado |
| `df[df["coluna"] > valor]` | Acessa a tabela DataFrame e filtra os registros que possuem na coluna um valor maior que o informado | Estudado |
| `df[df["coluna"] == valor]` | Acessa a tabela DataFrame e filtra os registros que possuem na coluna o valor informado | Estudado |
| `&` | Combina duas condições e exige que ambas sejam verdadeiras | Estudado |
| `\|` | Combina duas condições e permite que pelo menos uma seja verdadeira | Estudado |
| `~` | Nega uma condição e seleciona os valores que não atendem ao filtro informado | Estudado |
| `df.loc[]` | Acessa a tabela DataFrame e localiza registros e colunas específicos | Estudado |
| `df.loc[condição]` | Acessa a tabela DataFrame e localiza os registros que atendem a uma condição | Estudado |
| `df.loc[condição, ["coluna1", "coluna2"]]` | Acessa a tabela DataFrame, localiza os registros que atendem à condição e seleciona as colunas informadas | Estudado |
| `df.loc[condição, "coluna"] = valor` | Acessa a tabela DataFrame, localiza os registros que atendem à condição e altera o valor da coluna informada | Estudado |
| `df["coluna"].duplicated()` | Acessa uma coluna da tabela DataFrame e identifica quais valores estão duplicados | Estudado |
| `df["coluna"].duplicated(keep=False)` | Acessa uma coluna da tabela DataFrame e identifica todos os registros que possuem valores duplicados | Estudado |
| `df.drop_duplicates()` | Remove da tabela DataFrame os registros duplicados | Estudado |
| `df.drop_duplicates(subset="coluna")` | Remove da tabela DataFrame os registros duplicados considerando uma coluna específica | Estudado |
| `df.drop_duplicates(subset="coluna", keep="first")` | Remove da tabela DataFrame os registros duplicados e mantém o primeiro registro encontrado | Estudado |
| `.str.strip()` | Acessa os valores de texto e remove os espaços no início e no final | Estudado |
| `.str.lower()` | Acessa os valores de texto e converte todos os caracteres para letras minúsculas | Estudado |
| `.fillna()` | Localiza valores ausentes e preenche esses valores com a informação definida | Estudado |
| `pd.NA` | Representa um valor ausente nos dados | Estudado |
| `df["coluna"].quantile(0.25)` | Acessa uma coluna da tabela DataFrame e calcula o valor que representa 25% dos dados | Estudado |
| `df["coluna"].quantile(0.50)` | Acessa uma coluna da tabela DataFrame e calcula o valor que representa 50% dos dados, equivalente à mediana | Estudado |
| `df["coluna"].quantile(0.75)` | Acessa uma coluna da tabela DataFrame e calcula o valor que representa 75% dos dados | Estudado |
| `df["coluna"].isin(["valor1", "valor2"])` | Acessa uma coluna da tabela DataFrame e verifica quais registros possuem valores que estão na lista informada | Estudado |
| `df.loc[df["coluna"].isin(["valor1", "valor2"])]` | Acessa a tabela DataFrame, localiza na coluna os registros que possuem valores presentes na lista informada | Estudado |
| `~df["coluna"].isin(["valor1", "valor2"])` | Acessa uma coluna da tabela DataFrame e identifica os registros que não possuem valores presentes na lista informada | Estudado |
| `df["coluna"].between(valor1, valor2)` | Acessa uma coluna da tabela DataFrame e verifica quais valores estão dentro do intervalo informado | Estudado |
| `df.loc[df["coluna"].between(valor1, valor2)]` | Acessa a tabela DataFrame e localiza os registros que possuem valores dentro do intervalo informado | Estudado |
| `df["nova_coluna"] = valor` | Acessa a tabela DataFrame, cria uma nova coluna e define um valor para os registros | Estudado |
| `df.loc[condição, "nova_coluna"] = valor` | Acessa a tabela DataFrame, localiza os registros que atendem à condição e define um valor na nova coluna | Estudado |
| `df["faixa_etaria"].value_counts()` | Acessa a coluna faixa_etaria e conta quantos usuários existem em cada categoria de idade | Estudado |
| `df.groupby(["coluna1", "coluna2"]).size()` | Agrupa a tabela DataFrame por duas colunas e conta quantos registros existem em cada combinação | Estudado |
| `df.groupby(["coluna1", "coluna2"]).size().unstack(fill_value=0)` | Agrupa a tabela DataFrame por duas colunas, conta os registros e transforma uma das categorias em colunas preenchendo valores ausentes com zero | Estudado |
| `df.groupby("coluna").size().sort_values(ascending=False)` | Agrupa a tabela DataFrame por uma coluna, conta os registros de cada grupo e ordena do maior grupo para o menor | Estudado |
| `df["coluna"].apply()` | Acessa uma coluna da tabela DataFrame e aplica uma função aos valores dessa coluna | Estudado |
| `df["coluna"].apply(lambda valor: expressao)` | Acessa uma coluna da tabela DataFrame e aplica uma função simples a cada valor da coluna | Estudado |
| `df.apply(funcao, axis=1)` | Acessa a tabela DataFrame e aplica uma função percorrendo cada linha da tabela | Estudado |
| `lambda valor: expressao` | Cria uma função simples que recebe um valor e retorna o resultado de uma expressão | Estudado |
| `def nome_funcao()` | Define uma função personalizada que pode ser utilizada para executar uma tarefa específica | Estudado |
| `axis=1` | Define que a operação deve percorrer a tabela DataFrame linha por linha | Estudado |
| `axis=0` | Define que a operação deve percorrer a tabela DataFrame coluna por coluna | Estudado |
| `df["coluna"].str.contains()` | Acessa uma coluna de texto e verifica quais valores contêm o texto ou padrão informado | Estudado |
| `df["coluna"].str.contains("texto", case=False)` | Acessa uma coluna de texto e verifica quais valores contêm o texto informado ignorando letras maiúsculas e minúsculas | Estudado |
| `df["coluna"].str.contains("texto", na=False)` | Acessa uma coluna de texto e verifica quais valores contêm o texto informado considerando valores ausentes como não encontrados | Estudado |
| `df["coluna"].str.contains("texto", case=False, na=False)` | Acessa uma coluna de texto e verifica quais valores contêm o texto informado ignorando maiúsculas, minúsculas e valores ausentes | Estudado |
| `df[~df["coluna"].str.contains("texto")]` | Acessa a tabela DataFrame, filtra uma coluna de texto e localiza os registros que não contêm o texto informado | Estudado |
| `df.head()` | Exibe as primeiras linhas da tabela DataFrame | Próximo |
| `df.tail()` | Exibe as últimas linhas da tabela DataFrame | Próximo |
| `df.sample()` | Exibe registros aleatórios da tabela DataFrame | Próximo |
| `df.copy()` | Cria uma cópia independente da tabela DataFrame | Próximo |
| `df.rename()` | Renomeia colunas ou índices da tabela DataFrame | Próximo |
| `df.reset_index()` | Reseta o índice da tabela DataFrame e cria um novo índice sequencial | Próximo |
| `df.set_index()` | Define uma coluna da tabela DataFrame como índice | Próximo |
| `df.sort_index()` | Ordena os registros da tabela DataFrame com base no índice | Próximo |
| `df["coluna"].str.replace()` | Acessa uma coluna de texto e substitui partes dos valores por outro texto | Próximo |
| `df["coluna"].str.upper()` | Acessa uma coluna de texto e converte todos os caracteres para letras maiúsculas | Próximo |
| `df["coluna"].str.title()` | Acessa uma coluna de texto e converte os textos para o formato de título | Próximo |
| `df["coluna"].astype()` | Acessa uma coluna da tabela DataFrame e converte seus valores para o tipo de dado informado | Próximo |
| `pd.to_numeric()` | Converte os valores informados para o formato numérico | Próximo |
| `pd.to_datetime()` | Converte os valores informados para o formato de data e hora | Próximo |
| `df["data"].dt.year` | Acessa a coluna de data e extrai o ano de cada registro | Próximo |
| `df["data"].dt.month` | Acessa a coluna de data e extrai o mês de cada registro | Próximo |
| `df["data"].dt.day` | Acessa a coluna de data e extrai o dia de cada registro | Próximo |
| `df["coluna"].map()` | Acessa uma Series e aplica uma função individualmente a cada valor | Próximo |
| `df.replace()` | Acessa a tabela DataFrame e substitui valores específicos por outros valores | Próximo |
| `df.drop()` | Acessa a tabela DataFrame e remove linhas ou colunas especificadas | Próximo |
| `df.dropna()` | Acessa a tabela DataFrame e remove registros que possuem valores ausentes | Próximo |
| `pd.concat()` | Combina duas ou mais tabelas DataFrame ou Series em uma única estrutura | Próximo |
| `pd.merge()` | Combina tabelas DataFrame usando uma ou mais colunas relacionadas | Próximo |
| `df.pivot_table()` | Cria uma tabela dinâmica para resumir e analisar os dados | Próximo |
| `pd.crosstab()` | Cria uma tabela cruzada para analisar a frequência entre duas ou mais variáveis | Próximo |
| `df.corr()` | Calcula a correlação entre as colunas numéricas da tabela DataFrame | Próximo |
| `df.memory_usage()` | Mostra quanto de memória cada coluna da tabela DataFrame está utilizando | Próximo |
| `df.dtypes` | Mostra o tipo de dado armazenado em cada coluna da tabela DataFrame | Próximo |
| `df.columns` | Mostra os nomes das colunas existentes na tabela DataFrame | Próximo |
| `df.index` | Mostra os índices dos registros da tabela DataFrame | Próximo |

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