idade = int(input("Digite sua idade: "))

if idade > 18:
    print("Pode entrar na festa!")
elif idade > 16 and idade < 18:
    print("Éh hora de voltar para sua casa")
else:
    print("Vou chamar seus pais.")