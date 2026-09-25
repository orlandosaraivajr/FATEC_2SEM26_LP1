'''
Exercício 9 feito em sala de aula
Segunda versão
'''

def situacao_aluno(media):
    if media <= 3:
        return("Reprovado")
    elif media <= 7:
        return('Exame')
    else:
        return("Aprovado")


lista_de_notas = []
NUMERO_ALUNOS = 2

'''
Primeira parte: receber as notas dos alunos
'''
for x in range(NUMERO_ALUNOS):
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    notas = [nota1, nota2]
    lista_de_notas.append(notas)

print(lista_de_notas)
'''
Segunda parte: calcular as médias
'''
for aluno in lista_de_notas:
    media = sum(aluno)/len(aluno)
    print(media)
    print(situacao_aluno(media))
