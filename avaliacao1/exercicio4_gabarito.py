valor_venal = float(input("Informe o valor venal do imóvel: R$ "))

if valor_venal <= 100000.00:
    print("Imóvel isento. Não há IPTU a pagar.")
else:
    if valor_venal <= 250000.00:
        aliquota = 0.005
        parcela = 500.00
    elif valor_venal <= 500000.00:
        aliquota = 0.01
        parcela = 1750.00
    elif valor_venal <= 1000000.00:
        aliquota = 0.015
        parcela = 4250.00
    else:
        aliquota = 0.02
        parcela = 9250.00

    iptu = (valor_venal * aliquota) - parcela
    print("Alíquota aplicada: " + str(aliquota * 100) + "%")
    print("IPTU a pagar: R$ " + str(round(iptu, 2)))
