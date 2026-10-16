def soma(*args):
    # Args permite receber múltiplos parâmetros e trabalhar
    # internamente como uma tupla
    soma = 0
    for elemento in args:
        soma = soma + elemento
    return soma


print(soma(2,4))        # Espero imprimir 6
print(soma(2,4,2))      # Espero imprimir 8
print(soma(2,4,2,1))    # Espero imprimir 9
print(soma(2,4,2,1,4,2,1,4,2,1,4,2,1,4,2,1))