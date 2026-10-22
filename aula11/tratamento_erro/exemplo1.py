
import csv

with open("../alunos.csv", mode="r", newline="", encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    
    for linha in leitor:
        nome = linha.get("nome", "Desconhecido")
        idade = linha.get("idade", "N/A")
        curso = linha.get("curso", "N/A")

        print(f"{nome} tem {idade} anos e cursa {curso}.")
