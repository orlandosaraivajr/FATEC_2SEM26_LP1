def exibir_dados(**kwargs):
    for ch, v in kwargs.items():
        print(ch)
        print(v)
        print(10 * '=')


exibir_dados()
exibir_dados(nome='Orlando',cargo='professor')
exibir_dados(nome='Orlando',cargo='professor',fatec='Rio Claro')