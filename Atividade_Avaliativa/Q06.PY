from re import I


a = int(input("Digite seu valor: "))
i = a - 1
r = 0
pos = 0
while i<=a and i >= 1:
    if pos == 0:
        r = a * 1
        i -= 1
        pos += 1
    else:
        r = r * I
        i -= 1
        pos += 1
print("Resultado: " ,r)