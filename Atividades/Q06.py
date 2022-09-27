convidados = [
    "Coringa", "Thor", "Jesus", "Naruto", "Loki"
]



for nome in convidados:
    mensagem = f"Bora pra balada. {nome}"
    print(mensagem)


#Quem não pode ir
print("Jesus: Infelizmente não \
    posso estar no mesmo ambiente que o Loki")

print("Coringa: Infelizmente não \
    posso estar no mesmo ambiente que o Naruto")

#Modifique sua lista, substitua os desistentes por novos convidados.
convidados[2] = "Madre Tereza"
convidados[0] = "Pinguim"


for nome in convidados:
    mensagem = f"Bora pra balada. {nome}"
    print(mensagem)