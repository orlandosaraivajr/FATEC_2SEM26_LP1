valor_venal = float(input("Informe o valor venal do imóvel: R$ "))

# Chave: limite superior da faixa. Valor: (alíquota, parcela a deduzir)
faixas = {
    100000.00: (0.0, 0.00),
    250000.00: (0.005, 500.00),
    500000.00: (0.01, 1750.00),
    1000000.00: (0.015, 4250.00),
    float("inf"): (0.02, 9250.00),
}

# Escolhe o menor limite que seja >= valor venal.
# Limites menores que o valor recebem a chave (True, ...) e ficam no fim da ordenação.
limite = min(faixas, key=lambda lim: (lim < valor_venal, lim))
aliquota, parcela = faixas[limite]

iptu = (valor_venal * aliquota) - parcela
print("Alíquota aplicada: " + str(aliquota * 100) + "%")
print("IPTU a pagar: R$ " + str(round(iptu, 2)))
