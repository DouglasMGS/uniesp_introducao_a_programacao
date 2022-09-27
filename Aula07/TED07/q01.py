print('[ ! ] PROMOÇÃO: Apartir de 12 maçãs, o valor de cada uma será R$ 1,00. Valor normal sera R$ 1,30 [ ! ]')
macas = int(input('Digite o numero de maças que deseja comprar (0 Para sair do programa): '))

preco_promocao = 1.00
preco_normal = 1.30

if macas == 0: # Se digitado 0, encerra o programa
    print('Ate mais!')
    exit(0)
elif macas < 0: # caso digite  numero digitado nergativo, mostra messa mensagem de "Erro"
    print(f'O numero digitado e negativo: {macas}')
    exit(1)
elif macas >= 12: #Calcula o valor total incluso da promocao
    total = preco_promocao * macas
    print(f'Voce comprou {macas} e faz parte da promocao. Valor total; {total}')
else: # Calculando com o valor normal
    total= preco_normal * macas
    print(f'Voce comprou {macas} e não faz parte da promocao. Valor total: R$ {total}')