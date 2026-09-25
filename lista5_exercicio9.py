'''
Exercício 9 feito em sala de aula
'''

nota1 = [0,0,0,0,0,0]
nota2 = [0,0,0,0,0,0]

print('Notas da primeira avaliação: ')
for nota in range(len(nota1)):
    nota1[nota] = float(input("Digite a nota 1 do aluno:"))

print('Notas da segunda avaliação: ')
for nota in  range(len(nota2)):
    nota2[nota] = float(input("Digite a nota 2 do aluno:"))

print(nota1)
print(nota2)

for item in range(len(nota1)):
    media = nota1[item] + nota2[item]
    media = media / 2
    print(media)
    if media <= 3:
        print("Reprovado")
    elif media <= 7:
        print('Exame')
    else:
        print("Aprovado")