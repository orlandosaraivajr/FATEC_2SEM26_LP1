import unittest
from calculadora import somar, subtrair
from calculadora import dividir, multiplicacao

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(subtrair(5, 2), 3)

    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(10, 0), "Erro: divisão por zero")

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(2, 2), 4)
        self.assertEqual(multiplicacao(2, 0), 0)
        self.assertEqual(multiplicacao(2, 1), 2)
        self.assertEqual(multiplicacao(1, 2), 2)

if __name__ == '__main__':
    unittest.main()


