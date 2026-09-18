'''
Funções
'''
def soma(numero1, numero2):
    valor_somado = numero1 + numero2
    return valor_somado
    

numero = soma(4, 5)
print(numero)
numero = soma(7, 6)
print(numero)

# Exemplo com uso de input

def caixinha():
    valor1 = input("Digita aí...")
    print(valor1)
    valor2 = input("O que vou repetir ?")
    print(valor2)
    print(valor2)

caixinha()