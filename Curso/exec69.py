# ler sexo e idade de cada pessoa perguntar se o usuario quer continuar. no final mostrar quantos homens mulheres e maiores de 18
maiorIdade = 0
masc = 0
fem = 0
while True:
    print("CADASTRO")
    idade = int(input("\nIdade:"))
    sexo = input("Sexo: M/F ").upper().strip()
    if sexo == "M":
        masc = masc + 1
    if sexo == "F":
        fem = fem + 1
    if idade >= 18:
        maiorIdade = maiorIdade + 1
    escolha = input("Quer Continuar: S/N ").upper().strip()
    if escolha == "S":
        print()
    if escolha == "N":
        break
print(f"\nForam registrados: {masc} homens e {fem} mulheres.\nMaiores de idade: {maiorIdade}.")


