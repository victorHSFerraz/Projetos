from datetime import date

anoAtual = date.today().year


# ETAPA 1
def obter_limite():
    input("Press Enter to Continue...")
    print("\n\033[1;30mSeja bem-vindo! Aqui quem fala é Victor Ferraz\033[m")
    print("\nPara prosseguir com a análise de crédito, preencha os campos abaixo.")
    cargo = input("Cargo atual: ")
    salario = float(input("Salário: "))
    ano = int(input("Ano de Nascimento: "))
    print("\n\033[32mDados Pessoais\033[m:", end=" ")
    print("Cargo: {}".format(cargo))
    print("\t\t\t\tSalário: R${:.2f}".format(salario))
    print("\t\t\t\tAno de Nascimento: {}".format(ano))
    # ETAPA 2
    idade = anoAtual - ano
    print("\t\t\t\tIdade: {} anos".format(idade))
    limiteGasto = ((salario * (idade / 1000)) + 100)
    print("\n\033[4;32mSeu limite de crédito na loja é de R${:.2f}\033[m".format(limiteGasto))

    return limiteGasto, idade


tudo = 0


# ETAPA 3
def verificar_produto(limiteGasto, idade):
    global tudo
    print("\n\033[1;30mEscolha um produto\033[m")
    produto = input("\nNome do produto: ")
    precoProduto = float(input("Preço do produto: "))
    tudo = tudo + precoProduto
    print("\nProduto: {} \nPreço: R${:.2f}".format(produto, precoProduto))
    if precoProduto <= 0.6 * limiteGasto:
        print("\n\033[4;32mLiberado!\033[m")
    elif precoProduto <= 0.9 * limiteGasto:
        print("\nLiberado ao parcelar em 2x.")
    elif precoProduto <= limiteGasto:
        print("\nLiberado ao parcelar em 3x ou mais.")
    elif precoProduto > limiteGasto:
        print("\n\033[4;31mBloqueado\033[m")
    else:
        print("ERRO")
    meuNome = "Victor Ferraz"
    primeiroNome = "Victor"
    if len(meuNome) <= precoProduto <= idade:
        print("\nParabéns! Você ganhou um desconto de", len(primeiroNome), "%")
        descFinal = precoProduto * (len(primeiroNome) / 100)
        print("Total: R${:.2f}".format(precoProduto - descFinal))
    else:
        print("\nTotal: R${:.2f}".format(precoProduto))


dados = obter_limite()
limite = dados[0]
idade = dados[1]
produtosQuantidade = int(input("\nQuantos produtos deseja cadastrar? "))
for vezes in range(0, produtosQuantidade):
    verificar_produto(limite, idade)
# Valor total nao esta com o desconto aplicado
print(f"\nValor TOTAL dos produtos: {tudo}")
