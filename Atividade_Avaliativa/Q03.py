from ast import Break


print("\n*** escolha a opção desejada ***\n")

opcao = int(input("1 para adição \n2 para subtração \n3 para multiplicação \n4 para divisão n\5 para potencialização \n0 para parar a execução: "))
if 1 <= opcao <= 5:
    n1 = int(input("digite seu primeiro valor: "))
    n2 = int(input("digite seu segundo valor: "))

if opcao == 1:
    soma = n1 + n2
    print(f"soma de {n1} + {n2} : {soma} \n")

elif opcao == 2:

    soma = n1 - n2
    print(f"subtração de {n1} + {n2} : {soma} \n")

elif opcao == 3:
    soma = n1 * 2
    print(f"multiplicação de {n1} + {n2}: {soma} ")

elif opcao == 4:
    soma = n1 / n2
    print(f"divisão de {n1} + {n2}: {soma} ")

elif opcao == 5:

    soma =n1**n2
    print(f"potencialização de {n1} + {n2} : {soma} ")

elif opcao ==0:
    Break
else:
    print("Nenhuma das opções escolhidas \n")