from modulo_calculadora.calculadora import somar
from modulo_calculadora.calculadora import subtrair
from modulo_calculadora.calculadora import dividir

if __name__ == '__main__':
    n1 = 10
    n2 = 5
    print(f'Soma:   \t {somar(n1, n2)}')
    print(f'Subtração:   \t {subtrair(n1, n2)}')
    print(f'Divisão:\t {dividir(n1, n2)}')
