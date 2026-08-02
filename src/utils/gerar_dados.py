# Arquivo responsável por gerar dados sintéticos para testes e treinamento.
# Neste arquivo criamos uma base maior de vendas utilizando regras
# semelhantes aos dados reais para avaliar o desempenho dos modelos.


import random  # Nossa biblioteca para gerar valores aleatórios
import pandas as pd  # Nossa biblioteca para manipulação de dados


def gerar_dados(
    quantidade=2000,
    caminho="data/raw/atendimentos_expandido.csv"
):  # Nossa função para gerar dados sintéticos e salvar em um arquivo CSV


    nomes = [
        "Bruno Lima",
        "Ana Souza",
        "Carlos Mendes",
        "Mariana Silva",
        "João Santos",
        "Pedro Oliveira",
        "Juliana Costa",
        "Marcos Pereira",
        "Fernanda Alves",
        "Lucas Ferreira",
        "Amanda Rodrigues",
        "Diego Martins",
        "Carolina Gomes",
        "Thiago Alves",
        "Renata Costa"
    ]  # Nossa lista de nomes de clientes


    cidades = [
        "Campinas",
        "Valinhos",
        "Vinhedo",
        "Jundiai"
    ]  # Nossa lista de cidades disponíveis


    motos = [
        {
            "moto": "CB 500F",
            "marca": "Honda",
            "categoria": "Naked",
            "ano": 2024,
            "valor": 42500
        },
        {
            "moto": "Ninja 400",
            "marca": "Kawasaki",
            "categoria": "Esportiva",
            "ano": 2023,
            "valor": 35900
        },
        {
            "moto": "MT-03",
            "marca": "Yamaha",
            "categoria": "Naked",
            "ano": 2024,
            "valor": 32490
        },
        {
            "moto": "PCX 160",
            "marca": "Honda",
            "categoria": "Scooter",
            "ano": 2025,
            "valor": 21500
        },
        {
            "moto": "Versys 650",
            "marca": "Kawasaki",
            "categoria": "Trail",
            "ano": 2024,
            "valor": 49900
        },
        {
            "moto": "MT-07",
            "marca": "Yamaha",
            "categoria": "Naked",
            "ano": 2024,
            "valor": 49990
        },
        {
            "moto": "CB 650R",
            "marca": "Honda",
            "categoria": "Naked",
            "ano": 2024,
            "valor": 52990
        }
    ]  # Nossa lista de motos disponíveis


    lojas = {
        "Campinas": "Moto Center Campinas",
        "Valinhos": "Moto Center Valinhos",
        "Vinhedo": "Moto Center Vinhedo",
        "Jundiai": "Moto Center Jundiaí"
    }  # Nossa relação entre cidade e loja


    vendedores = [
        "João Silva",
        "Maria Oliveira",
        "Carlos Santos",
        "Pedro Souza"
    ]  # Nossa lista de vendedores


    pagamentos = [
        "Financiamento",
        "Pix",
        "Cartão"
    ]  # Nossa lista de formas de pagamento


    status_vendas = [
        "Concluída",
        "Agendada",
        "Cancelada"
    ]  # Nossa lista de status das vendas


    registros = []  # Nossa lista que armazenará os registros gerados


    for id_venda in range(1, quantidade + 1):  # Nosso loop responsável por criar cada venda


        nome = random.choice(nomes)  # Nosso nome escolhido aleatoriamente

        cidade = random.choice(cidades)  # Nossa cidade escolhida aleatoriamente

        moto = random.choice(motos)  # Nossa moto escolhida aleatoriamente


        idade = random.randint(18, 75)  # Nossa idade gerada aleatoriamente


        if random.random() < 0.05:  # Nossa condição para gerar algumas idades vazias

            idade = None  # Nossa idade recebe valor nulo


        valor_variacao = random.randint(-3000, 3000)  # Nossa variação de preço

        valor_final = moto["valor"] + valor_variacao  # Nosso valor final da moto


        registro = {

            "id_venda": id_venda,

            "nome_cliente": nome,

            "idade": idade,

            "cidade_cliente": cidade,

            "estado": "SP",

            "moto": moto["moto"],

            "marca": moto["marca"],

            "categoria": moto["categoria"],

            "ano_moto": moto["ano"],

            "valor_moto": f"R$ {valor_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),

            "loja": lojas[cidade],

            "cidade_loja": cidade,

            "vendedor": random.choice(vendedores),

            "status_venda": random.choice(status_vendas),

            "forma_pagamento": random.choice(pagamentos),

            "data_venda": f"{random.randint(1,28):02d}/{random.randint(1,12):02d}/2026",

            "email": nome.lower().replace(" ", ".") + f"{id_venda}@email.com",

            "telefone": f"1199999{id_venda:04d}"

        }  # Nosso registro completo


        registros.append(registro)  # Adiciona o registro na lista final


    df = pd.DataFrame(registros)  # Cria nosso DataFrame


    df.to_csv(
        caminho,
        index=False
    )  # Salva os dados gerados no arquivo CSV


    print(
        f"\nDados sintéticos gerados com sucesso!"
    )  # Exibe mensagem de sucesso


    print(
        f"Quantidade de registros criados: {quantidade}"
    )  # Exibe quantidade criada


    return df  # Retorna o DataFrame gerado