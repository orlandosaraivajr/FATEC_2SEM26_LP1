# Variação 2 - Listas
#
# Um fiscal da prefeitura precisa calcular o IPTU de vários imóveis de uma rua.
# Faça um programa que leia o valor venal de vários imóveis até que seja
# digitado 0 (zero). Use as mesmas faixas do exercício 4.
#
# Guarde os valores venais em uma lista e os IPTUs calculados em outra lista.
# Ao final, exiba:
#   a) o IPTU de cada imóvel (Imóvel 1, Imóvel 2, ...);
#   b) o total arrecadado;
#   c) o maior e o menor IPTU;
#   d) a média de IPTU por imóvel;
#   e) a quantidade de imóveis isentos.

# Cada faixa: [limite_superior, aliquota, parcela_a_deduzir]
faixas = [
    [100000.00, 0.0, 0.00],
    [250000.00, 0.005, 500.00],
    [500000.00, 0.01, 1750.00],
    [1000000.00, 0.015, 4250.00],
    [float("inf"), 0.02, 9250.00],
]

valores = []
iptus = []

valor_venal = float(input("Informe o valor venal do imóvel (0 para sair): R$ "))
while valor_venal != 0:
    for limite, aliquota, parcela in faixas:
        if valor_venal <= limite:
            break
    valores.append(valor_venal)
    iptus.append(round(valor_venal * aliquota - parcela, 2))
    valor_venal = float(input("Informe o valor venal do imóvel (0 para sair): R$ "))

if len(iptus) == 0:
    print("Nenhum imóvel informado.")
else:
    for i in range(len(valores)):
        print("Imóvel " + str(i + 1) + ": valor venal R$ " + str(valores[i]) +
              " | IPTU R$ " + str(iptus[i]))

    print("Total arrecadado: R$ " + str(round(sum(iptus), 2)))
    print("Maior IPTU: R$ " + str(max(iptus)))
    print("Menor IPTU: R$ " + str(min(iptus)))
    print("Média de IPTU: R$ " + str(round(sum(iptus) / len(iptus), 2)))
    print("Imóveis isentos: " + str(iptus.count(0.0)))
