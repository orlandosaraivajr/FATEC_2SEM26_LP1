"""
Lista de Revisão 1 - Versão 1 - Problema 3
Gabarito
Linguagem de Programação I - Prof. Orlando Saraiva Júnior
"""

quantidade = int(input("Quantidade de alunos: "))

aprovados = 0
recuperacao = 0
reprovados = 0
soma_medias = 0

for i in range(quantidade):
    nome = input(f"Nome do aluno {i + 1}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    media = (nota1 + nota2) / 2
    soma_medias += media

    if media >= 6:
        situacao = "Aprovado"
        aprovados += 1
    elif media >= 4:
        situacao = "Recuperação"
        recuperacao += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    print(f"{nome} - Média: {media:.1f} - {situacao}")

print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
if quantidade > 0:
    print(f"Média geral da turma: {soma_medias / quantidade:.2f}")
