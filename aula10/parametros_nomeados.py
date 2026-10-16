def retangulo(altura, largura, caracter='*'):
    linha = caracter * largura
    for i in range(altura):
        print(linha)


retangulo(6, 10,'*')
# Aplicação de parâmetros nomeados
retangulo(caracter='$',altura=5,largura=20)
