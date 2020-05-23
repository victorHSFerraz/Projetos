# calcular preço viagem 0,50 por km ate 200km, acima disso 0,45 por km
kmViagem = float(input("Km da viagem: "))
if kmViagem <= 200:
    custo = kmViagem * 0.50
else:
    custo = kmViagem * 0.45
print("O custo da viagem é de R${:.2f}".format(custo))

