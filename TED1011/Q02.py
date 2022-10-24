import random
list = []

for x in range(30):
    x = random.randint(1, 15)
    list.append(x)

meu_numero = int(input("Digite um numero de 1 a 15: "))
contador = 0
for x in list:

    if x == meu_numero:
        contador += 1

print(f"Eu escolhi o numero: {meu_numero}. ")
print(f"Meu numero repetiu, {contador} vezes. ")
print(f"Os numeros sorteados são: {list}. ")