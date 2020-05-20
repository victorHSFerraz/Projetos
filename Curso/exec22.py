# crie um programa que leia o nome completo de uma pessoa e mostre o nome em maiusculo minusculo total de letras do nome
name = (input("Seu nome: "))
print(name.upper())
print(name.lower())
print(len(name.strip()) - name.count(" "))
name = name.split()
print(len(name[0]))
