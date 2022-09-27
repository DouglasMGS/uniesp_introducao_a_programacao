cadastros = []

botao = 1000
while botao !=0:
    print("Digite 1 para cadastrar um nome usuario")
    print("Digite 2 para imprimir todos os usuarios")
    print("Digite 0 para sair")
    botao = int(input("Digite a opçao desejada: "))

    if botao == 1:
    #Entrada dos dados
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o e-mail: ")
        #Folha de cadastro
        dados = [nome, idade, email]
        #Guardando a folha na pasta
        cadastros.append(dados)
    elif botao == 2:

        for p in cadastros:
            print(p)

    elif botao == 0:
            print("Obrigado por acessar esse software!")    

    else:
        print("Digite um numero valido!")       