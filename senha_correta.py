'''
Programa: Senha correta

1) Receba uma senha do usuário
2) Se a senha for '123mudar'
    2.1) Mostrar a mensagem "Acertou"
    2.2) Encerrar Programa
3) Se a senha não for '123mudar'
   3.1) Mostrar a mensagem "Errou!"
   3.2 ) Volte ao passo 1
'''
senha = input("digite a senha: ")

while senha != '123mudar':
    print("errou !")
    print("Tente outra vez")
    senha = input("digite a senha: ")

print('Você acertou a senha secreta do Orlando')