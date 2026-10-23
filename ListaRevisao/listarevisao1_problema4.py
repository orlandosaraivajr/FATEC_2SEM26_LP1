"""
Lista de Revisão 1 - Versão 1 - Problema 4
Gabarito
Linguagem de Programação I - Prof. Orlando Saraiva Júnior
"""

leitura_anterior = int(input("Leitura anterior (kWh): "))
leitura_atual = int(input("Leitura atual (kWh): "))
bandeira = input("Bandeira (V/A/R): ").upper()

if leitura_atual < leitura_anterior:
    print("Leitura inválida!")
elif bandeira != "V" and bandeira != "A" and bandeira != "R":
    print("Bandeira inválida!")
else:
    consumo = leitura_atual - leitura_anterior

    if consumo <= 100:
        tarifa = 0.60
    elif consumo <= 200:
        tarifa = 0.75
    elif consumo <= 400:
        tarifa = 0.90
    else:
        tarifa = 1.10

    if bandeira == "V":
        percentual = 0
    elif bandeira == "A":
        percentual = 0.05
    else:
        percentual = 0.10

    valor_consumo = consumo * tarifa
    acrescimo = valor_consumo * percentual
    total = valor_consumo + acrescimo + 12.00

    print(f"Consumo: {consumo} kWh")
    print(f"Tarifa: R$ {tarifa:.2f} por kWh")
    print(f"Acréscimo da bandeira: R$ {acrescimo:.2f}")
    print(f"Total da conta: R$ {total:.2f}")
