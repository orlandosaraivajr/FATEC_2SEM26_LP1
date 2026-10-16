# Variação 3 - Dicionários
#
# O IPTU calculado pelas faixas do exercício 4 agora é ajustado pelo TIPO do
# imóvel e pela FORMA DE PAGAMENTO:
#
#   Tipo:  R - Residencial -> IPTU x 1,0
#          C - Comercial   -> IPTU x 1,5
#          T - Terreno     -> IPTU x 2,0
#
#   Pagamento: 1 - À vista       -> 10% de desconto
#              2 - Parcelado 10x -> sem desconto
#
# Use dicionários para guardar as faixas, os tipos e as formas de pagamento.
# Se o usuário digitar um tipo ou forma de pagamento inválido, informe o erro.
# Ao final, monte um dicionário "resultado" com os dados do cálculo e exiba
# cada chave e valor percorrendo o dicionário.

# Chave: limite superior da faixa. Valor: (alíquota, parcela a deduzir)
faixas = {
    100000.00: (0.0, 0.00),
    250000.00: (0.005, 500.00),
    500000.00: (0.01, 1750.00),
    1000000.00: (0.015, 4250.00),
    float("inf"): (0.02, 9250.00),
}

tipos = {
    "R": ("Residencial", 1.0),
    "C": ("Comercial", 1.5),
    "T": ("Terreno", 2.0),
}

pagamentos = {
    "1": ("À vista", 0.10),
    "2": ("Parcelado 10x", 0.0),
}

valor_venal = float(input("Informe o valor venal do imóvel: R$ "))
tipo = input("Tipo do imóvel (R - Residencial, C - Comercial, T - Terreno): ").upper()
forma = input("Forma de pagamento (1 - À vista, 2 - Parcelado 10x): ")

if tipo not in tipos:
    print("Tipo de imóvel inválido.")
elif forma not in pagamentos:
    print("Forma de pagamento inválida.")
else:
    for limite in faixas:
        if valor_venal <= limite:
            break
    aliquota, parcela = faixas[limite]
    nome_tipo, multiplicador = tipos[tipo]
    nome_pagamento, desconto = pagamentos[forma]

    iptu_base = valor_venal * aliquota - parcela
    iptu_final = iptu_base * multiplicador * (1 - desconto)

    resultado = {
        "Valor venal": "R$ " + str(valor_venal),
        "Tipo": nome_tipo,
        "Alíquota": str(aliquota * 100) + "%",
        "IPTU base": "R$ " + str(round(iptu_base, 2)),
        "Pagamento": nome_pagamento,
        "IPTU a pagar": "R$ " + str(round(iptu_final, 2)),
    }

    for chave, valor in resultado.items():
        print(chave + ": " + valor)
