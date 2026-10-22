
import csv

try:
    arquivo_csv = open("../alunos.csv", mode="r", newline="", encoding="utf-8")
    leitor = csv.DictReader(arquivo_csv)
    
    for linha in leitor:
        nome = linha.get("nome", "Desconhecido")
        idade = linha.get("idade", "N/A")
        curso = linha.get("curso", "N/A")

        print(f"{nome} tem {idade} anos e cursa {curso}.")
    
    arquivo_csv.close()

except FileNotFoundError:
    print("Erro: o arquivo 'alunos.csv' não foi encontrado.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
