
import requests
import csv

# Lista de Pokémons para buscar
nomes_pokemon = ["pikachu", "bulbasaur", "charmander", "squirtle"]

# Arquivos de saída
arquivo_csv = "pokemons.csv"
arquivo_txt = "pokemons.txt"

# Lista para armazenar os dados coletados
dados_pokemons = []

# Consulta à API
for nome in nomes_pokemon:
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        pokemon_info = {
            "nome": dados["name"],
            "altura": dados["height"],
            "peso": dados["weight"]
        }
        dados_pokemons.append(pokemon_info)
    else:
        print(f" Não foi possível obter dados de {nome} (código {resposta.status_code})")

# Salvando em CSV
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as csvfile:
    campos = ["nome", "altura", "peso"]
    escritor = csv.DictWriter(csvfile, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(dados_pokemons)

# Salvando em TXT
with open(arquivo_txt, mode="w", encoding="utf-8") as txtfile:
    for p in dados_pokemons:
        linha = f"{p['nome'].capitalize()} - Altura: {p['altura']}, Peso: {p['peso']}\n"
        txtfile.write(linha)

print(" Dados salvos com sucesso em CSV e TXT.")
