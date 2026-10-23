"""
Lista de Revisão 1 - Versão 1 - Problema 5
Gabarito
Linguagem de Programação I - Prof. Orlando Saraiva Júnior
"""

quantidade = int(input("Quantidade de veículos: "))

processados = 0
gratuitos = 0
total_arrecadado = 0

for i in range(quantidade):
    placa = input(f"Placa do veículo {i + 1}: ")
    tipo = input("Tipo (C/M): ").upper()
    minutos = int(input("Tempo de permanência (minutos): "))

    if tipo == "C":
        primeira_hora = 8.00
        hora_adicional = 4.00
    elif tipo == "M":
        primeira_hora = 4.00
        hora_adicional = 2.00
    else:
        print("Tipo inválido!")
        continue

    processados += 1

    if minutos <= 15:
        horas = 0
        valor = 0
        gratuitos += 1
    else:
        horas = minutos // 60
        if minutos % 60 > 0:
            horas += 1
        valor = primeira_hora + (horas - 1) * hora_adicional

    total_arrecadado += valor
    print(f"Placa: {placa} - Horas cobradas: {horas} - Valor: R$ {valor:.2f}")

print(f"Veículos processados: {processados}")
print(f"Veículos gratuitos: {gratuitos}")
print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
