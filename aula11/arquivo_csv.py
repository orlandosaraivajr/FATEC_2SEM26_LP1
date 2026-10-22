import csv

# Dados a serem salvos
alunos = [
    {"nome": "Ana", "idade": 20, "curso": "IA"},
    {"nome": "Bruno", "idade": 22, "curso": "IA"},
    {"nome": "Carla", "idade": 19, "curso": "ESG"},
]

# Caminho do arquivo
arquivo_csv = "alunos.csv"

# Escrevendo os dados no arquivo CSV
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
    campos = ["nome", "idade", "curso"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    
    escritor.writeheader()  # Escreve os nomes das colunas
    for aluno in alunos:
        escritor.writerow(aluno)

print("Arquivo CSV criado com sucesso!")

# Lendo o arquivo CSV com DictReader
print("\n Dados lidos do CSV:")

with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        print(f"{linha['nome']} tem {linha['idade']} anos e cursa {linha['curso']}.")
