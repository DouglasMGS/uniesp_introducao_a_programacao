x1 = float(input("coordenada x do primeiro ponto: "))
y1 = float(input("coordenada y do primeiro ponto: "))
x2 = float(input("coordenada x do segundo ponto: "))
y2 = float(input("coordenada y do segundo ponto: "))
dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(f"A distância entre os pontos é de {dist}")
