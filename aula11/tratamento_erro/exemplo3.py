import csv

caminho_csv = "../alunos.csv"
caminho_txt = "alunos_formatado.txt"

try:
    # Lê o CSV com with e trata se o arquivo não existe
    with open(caminho_csv, mode="r", newline="", encoding="utf-8") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)

        # Abre o arquivo de saída TXT para escrita
        with open(caminho_txt, mode="w", encoding="utf-8") as arquivo_txt:
            for linha in leitor:
                nome = linha.get("nome", "Desconhecido")
                idade = linha.get("idade", "N/A")
                curso = linha.get("curso", "N/A")

                texto = f"{nome} tem {idade} anos e cursa {curso}.\n"
                arquivo_txt.write(texto)

    print(f"Dados foram exportados com sucesso para {caminho_txt}.")

except FileNotFoundError:
    print(f"Erro: o arquivo {caminho_csv} não foi encontrado.")

except KeyError as e:
    print(f"Erro: coluna ausente no CSV - {e}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
