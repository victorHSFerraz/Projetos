# ler nome idade e sexo de 4 pessoas media idade nome do homem mais velho mulheres com menos de 20 anos
media = 0
cont = 0
maioridadehomem = 0
homemmaisvelho = ""
for x in range(1, 5):
    print("----------{}° PESSOA ----------".format(x))
    nome = str(input("Nome: ")).strip().title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]: ")).strip().title()
    media = media + idade
    if sexo == "M" and maioridadehomem < idade:
        maioridadehomem = idade
        homemmaisvelho = nome
    if sexo == "F" and idade < 20:
        cont = cont + 1
print("Média de idade: {} anos".format(media/4))
print("Homem com maior idade: {}".format(homemmaisvelho))
print("Mulheres com menos de 20 anos: {}".format(cont))

