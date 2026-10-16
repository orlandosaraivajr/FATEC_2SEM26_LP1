# Variação 1 - Tuplas
#
# A prefeitura definiu as faixas do IPTU abaixo, que NÃO podem ser alteradas
# durante a execução do programa. Armazene-as em uma tupla de tuplas no formato
# (limite_superior, aliquota, parcela_a_deduzir).
#
#   Faixa 1: até R$ 100.000,00          -> isento
#   Faixa 2: até R$ 250.000,00          -> 0,5%  (deduzir R$ 500,00)
#   Faixa 3: até R$ 500.000,00          -> 1,0%  (deduzir R$ 1.750,00)
#   Faixa 4: até R$ 1.000.000,00        -> 1,5%  (deduzir R$ 4.250,00)
#   Faixa 5: acima de R$ 1.000.000,00   -> 2,0%  (deduzir R$ 9.250,00)
#
# O programa deve:
#   a) exibir a tabela de faixas percorrendo a tupla;
#   b) ler o valor venal de um imóvel;
#   c) informar em qual faixa o imóvel se encaixa, a alíquota e o IPTU a pagar
#      (IPTU = valor_venal * aliquota - parcela).

FAIXAS = (
    (100000.00, 0.0, 0.00),
    (250000.00, 0.005, 500.00),
    (500000.00, 0.01, 1750.00),
    (1000000.00, 0.015, 4250.00),
    (float("inf"), 0.02, 9250.00),
)

print("Tabela de faixas do IPTU")
for numero, (limite, aliquota, parcela) in enumerate(FAIXAS, start=1):
    print("Faixa " + str(numero) + ": até R$ " + str(limite) +
          " | alíquota " + str(aliquota * 100) + "% | dedução R$ " + str(parcela))

valor_venal = float(input("Informe o valor venal do imóvel: R$ "))

for numero, (limite, aliquota, parcela) in enumerate(FAIXAS, start=1):
    if valor_venal <= limite:
        break

iptu = (valor_venal * aliquota) - parcela

print("Faixa: " + str(numero))
if aliquota == 0:
    print("Imóvel isento. Não há IPTU a pagar.")
else:
    print("Alíquota aplicada: " + str(aliquota * 100) + "%")
    print("IPTU a pagar: R$ " + str(round(iptu, 2)))
