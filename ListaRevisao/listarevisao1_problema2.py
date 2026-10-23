"""
Lista de Revisão 1 - Versão 1 - Problema 2
Gabarito
Linguagem de Programação I - Prof. Orlando Saraiva Júnior
"""

python = ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Ana", "Fábio",
          "Gabriela", "Hugo", "Igor", "Júlia", "Carla"]

banco_dados = ["Bruno", "Carla", "Elisa", "Gabriela", "Igor",
               "Karen", "Lucas", "Marina", "Bruno"]

redes = ["Carla", "Diego", "Elisa", "Igor", "Lucas",
         "Nathan", "Olívia", "Pedro"]

# Conversão para conjuntos (remove os nomes repetidos)
py = set(python)
bd = set(banco_dados)
rd = set(redes)

# 2.1 Interseção: alunos nas três disciplinas
print("2.1 Nas três disciplinas:", py & bd & rd)

# 2.2 União: total de alunos diferentes
todos = py | bd | rd
print("2.2 Total de alunos diferentes:", len(todos))

# 2.3 Diferença simétrica: Python ou Banco de Dados, mas não as duas
print("2.3 Somente Python ou somente BD:", py ^ bd)

# 2.4 Diferença: somente Python
print("2.4 Somente Python:", py - bd - rd)
