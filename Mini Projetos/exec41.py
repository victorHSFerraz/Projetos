# classificação de atletas por idade; até 9 mirim ate 14 infantil ate 19 junior ate 25 senior acima master
idade = int(input("Sua Idade: "))
if idade <= 9:
    print("Sua Categoria: \033[1;32mMirim\033[m")
elif idade <= 14:
    print("Sua Categoria: \033[1;32mInfantil\033[m")
elif idade <= 19:
    print("Sua Categoria: \033[1;32mJunior\033[m")
elif idade <= 25:
    print("Sua Categoria: \033[1;32mSênior\033[m")
elif idade > 25:
    print("Sua Categoria: \033[1;32mMaster\033[m")
