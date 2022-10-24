clubs = []

for time in range(10):
    clubs.append(input("Digite os Clubes: "))

print("Digite o nome do seu clube para conferir se está na lista!!!")
print("*"*26)

x = input("Verifique aqui: ")
if x in clubs:
    print(f"Achei!! Otime {x} foi selecionado. ")
else:
    print(f"Não Achei!!!! o {x}, não foi selecionado. ")
