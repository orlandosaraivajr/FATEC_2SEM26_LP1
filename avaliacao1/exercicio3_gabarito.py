quantidade = int(input("Quantidade de produtos: "))

estoque_baixo = 0
estoque_normal = 0

for i in range(quantidade):
    nome = input("Nome do produto: ")
    preco = float(input("Preço unitário: "))
    qtd_estoque = int(input("Quantidade em estoque: "))
    valor_total = preco * qtd_estoque
    print(nome + " - Valor em estoque: " + str(valor_total))
    if qtd_estoque < 10:
        estoque_baixo = estoque_baixo + 1
    else:
        estoque_normal = estoque_normal + 1

print("Produtos com estoque baixo: " + str(estoque_baixo))
print("Produtos com estoque normal: " + str(estoque_normal))