# Variação 4 - Conjuntos
#
# A prefeitura criou um programa de isenção de IPTU. O imóvel é isento se:
#   - estiver em um bairro do conjunto BAIRROS_ISENTOS; ou
#   - o proprietário tiver pelo menos uma das condições do conjunto
#     CONDICOES_ISENCAO.
#
#   BAIRROS_ISENTOS   = {"Vila Nova", "Jardim Esperança", "Parque das Flores"}
#   CONDICOES_ISENCAO = {"aposentado", "pcd", "ex-combatente"}
#
# Faça um programa que leia:
#   a) o valor venal do imóvel;
#   b) o bairro;
#   c) as condições do proprietário separadas por vírgula
#      (ex.: "aposentado, professor"). O usuário pode repetir condições.
#
# Use operações de conjuntos para descobrir quais condições do proprietário dão
# direito à isenção (interseção). Se não houver isenção, calcule o IPTU pelas
# faixas do exercício 4.

BAIRROS_ISENTOS = {"Vila Nova", "Jardim Esperança", "Parque das Flores"}
CONDICOES_ISENCAO = {"aposentado", "pcd", "ex-combatente"}

FAIXAS = (
    (100000.00, 0.0, 0.00),
    (250000.00, 0.005, 500.00),
    (500000.00, 0.01, 1750.00),
    (1000000.00, 0.015, 4250.00),
    (float("inf"), 0.02, 9250.00),
)

valor_venal = float(input("Informe o valor venal do imóvel: R$ "))
bairro = input("Informe o bairro: ").strip()
texto = input("Condições do proprietário (separadas por vírgula): ")

# O conjunto elimina condições repetidas automaticamente
condicoes = set()
for condicao in texto.split(","):
    condicao = condicao.strip().lower()
    if condicao != "":
        condicoes.add(condicao)

condicoes_validas = condicoes & CONDICOES_ISENCAO

if bairro in BAIRROS_ISENTOS:
    print("Imóvel isento: o bairro " + bairro + " faz parte do programa de isenção.")
elif len(condicoes_validas) > 0:
    print("Imóvel isento pelas condições: " + ", ".join(sorted(condicoes_validas)))
else:
    for limite, aliquota, parcela in FAIXAS:
        if valor_venal <= limite:
            break
    iptu = valor_venal * aliquota - parcela
    if iptu == 0:
        print("Imóvel isento pelo valor venal. Não há IPTU a pagar.")
    else:
        print("Alíquota aplicada: " + str(aliquota * 100) + "%")
        print("IPTU a pagar: R$ " + str(round(iptu, 2)))
