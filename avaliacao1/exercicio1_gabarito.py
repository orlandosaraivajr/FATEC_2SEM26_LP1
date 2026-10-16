alunos = (
{"nome": "Lucas", "notas": [7, 8, 6]},
{"nome": "Mariana", "notas": [9, 10, 9]},
{"nome": "Rafael", "notas": [5, 4, 6]},
{"nome": "Beatriz", "notas": [8, 8, 7]},
{"nome": "Thiago", "notas": [6, 7, 5]},
{"nome": "Larissa", "notas": [10, 10, 9]},
{"nome": "Pedro", "notas": [4, 5, 3]},
{"nome": "Camila", "notas": [8, 7, 8]},
{"nome": "Rodrigo", "notas": [7, 6, 7]},
{"nome": "Sofia", "notas": [9, 9, 8]},
)

# Inicializa variáveis para controle do melhor aluno
melhor_aluno = ''
notas_melhor_aluno = [ ]
maior_media = -1

for aluno in alunos:
    soma = 0
    contador = 0
    for nota in aluno["notas"]:
        soma = soma + nota
        contador = contador + 1
    media = soma / contador
    if media > maior_media:
        maior_media = media
        melhor_aluno = aluno["nome"]
        notas_melhor_aluno = aluno["notas"]

print("Aluno com maior média: " + melhor_aluno)
print("Notas: " + str( notas_melhor_aluno ) )
print("Média: " + str( maior_media ) )