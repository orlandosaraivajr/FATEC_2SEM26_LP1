alunos = [("Ana", 8), ("Carlos", 5), ("Bruna", 10)]

# Usando lambda para dizer: "ordene pelo segundo item"
ordenado = sorted(alunos, key=lambda aluno: aluno[1])

print(ordenado)
# Resultado: [('Carlos', 5), ('Ana', 8), ('Bruna', 10)]
