"""
Lista de Revisão 1 - Versão 1 - Problema 1
Gabarito
Linguagem de Programação I - Prof. Orlando Saraiva Júnior
"""

vendas = {
    "Ana":      [3200, 4100, 2800, 5000],
    "Bruno":    [2500, 2600, 3100, 2900],
    "Carla":    [4800, 5200, 4900, 5100],
    "Diego":    [1800, 2200, 1500, 2100],
    "Elisa":    [3900, 3700, 4200, 4400],
    "Fábio":    [2700, 3300, 2900, 3000],
    "Gabriela": [5100, 4700, 5300, 5200],
    "Henrique": [2000, 1900, 2400, 2300],
}

META = 12000

# Inicializa variáveis de controle
totais = {}
melhor_vendedor = ""
maior_total = 0
abaixo_meta = []

# --- Solução ---
for nome, valores in vendas.items():
    total = 0
    for valor in valores:
        total += valor
    totais[nome] = total

    if total > maior_total:
        maior_total = total
        melhor_vendedor = nome

    if total < META:
        abaixo_meta.append(nome)

print("Totais: " + str(totais))
print("Melhor vendedor: " + melhor_vendedor + " - R$ " + str(maior_total))
print("Abaixo da meta: " + str(sorted(abaixo_meta)))
