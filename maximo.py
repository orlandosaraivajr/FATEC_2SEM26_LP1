def maximo(n1, n2):
    if n1 > n2:
        return n1
    if n2 >= n1:
        return n2

print(maximo(5, 6)) # Espectativa: 6
print(maximo(2, 1)) # Espectativa: 2
print(maximo(2, 2)) # Espectativa: 2