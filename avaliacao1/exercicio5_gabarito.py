quantidade = int(input("Quantidade de funcionários: "))

total_folha = 0
processados = 0

for i in range(quantidade):
    nome = input("Nome do funcionário: ")
    codigo = int(input("Código do cargo: "))
    horas_extras = float(input("Horas extras no mês: "))

    if codigo == 1:
        cargo = "Auxiliar Administrativo"
        salario_base = 2200.00
        beneficios = 350.00
        imposto_percentual = 0.075
    elif codigo == 2:
        cargo = "Técnico de TI"
        salario_base = 3520.00
        beneficios = 450.00
        imposto_percentual = 0.09
    elif codigo == 3:
        cargo = "Analista"
        salario_base = 4400.00
        beneficios = 500.00
        imposto_percentual = 0.11
    elif codigo == 4:
        cargo = "Coordenador"
        salario_base = 6600.00
        beneficios = 800.00
        imposto_percentual = 0.14
    elif codigo == 5:
        cargo = "Gerente"
        salario_base = 8800.00
        beneficios = 1200.00
        imposto_percentual = 0.18
    else:
        cargo = ""

    if cargo == "":
        print("Código inválido! Funcionário " + nome + " não foi processado.")
    else:
        valor_hora = salario_base / 220
        valor_horas_extras = horas_extras * valor_hora * 1.5
        imposto = (salario_base + valor_horas_extras) * imposto_percentual
        salario_liquido = salario_base + valor_horas_extras + beneficios - imposto

        print(nome + " - " + cargo + " - Salário líquido: R$ " + str(round(salario_liquido, 2)))

        total_folha = total_folha + salario_liquido
        processados = processados + 1

print("Funcionários processados: " + str(processados))
print("Total da folha de pagamento: R$ " + str(round(total_folha, 2)))
