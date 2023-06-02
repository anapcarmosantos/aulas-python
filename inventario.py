codigo = [123, 412, 543, 654321, 765, 1234]
produto = ["Tv", "Notebook", "Banana", "Pão", "Carro", "X-box"]
qtd = [1, 2, 12, 5, 1, 1]
valor = [2000, 5000, 1, 1.5, 70000, 1500]

def relatorio():
    for index in range(0, len(codigo)):
        print("\nCodigo......", codigo[index])
        print("Nome........", produto[index])
        print("Quntidate...", qtd[index])
        print("Valor.......", valor[index])

def busca():
    buscar = input("Entre com o nome do produto: ").title()
    if buscar in produto:
        for index in range(0, len(codigo)):
            if buscar == produto[index]:
                print("\nCodigo......", codigo[index])
                print("Nome........", produto[index])
                print("Quntidate...", qtd[index])
                print("Valor.......", valor[index])
    else:
        print("Voce não possui esse produto!")
        relatorio()

def adicionar():
    codigo.append(int(input("Entre com o codigo do produto: ")))
    produto.append(input("Entre com o nome do produto: "))
    qtd.append(int(input("Entre com a quantidade do item: ")))
    valor.append(float(input("Entre com o valor do item: ")))

def alterar():
    buscar = input("Entre com o nome do produto: ").title()
    if buscar in produto:
        for index in range(0, len(codigo)):
            if buscar == produto[index]:
                valor[index] = float(input("Entre com o novo valor: "))
                print("\nCodigo......", codigo[index])
                print("Nome........", produto[index])
                print("Quntidate...", qtd[index])
                print("Valor.......", valor[index])
    else:
        print("Voce não possui esse produto!")
        relatorio()

def inflacao():
    infla = float(input("Informe o percentual de inflação: "))
    percento = infla/100
    for index in range(0, len(codigo)):
        valor[index] = valor[index]*(1 + percento)
        relatorio()

def remover():
    buscar = input("Entre com o nome do produto: ").title()
    if buscar in produto:
        for index in range(0, len(codigo)):
            if buscar == produto[index]:
                del codigo[index]
                del produto[index]
                del qtd[index]
                del valor[index]
                break
    else:
        print("Voce não possui esse produto!")
    relatorio()


def main(): 
    adicionar()
    # print('produto adicionado!!!!!\n\n\n\n\n')
    # print('!!!!RELATORIO!!!!')
    # relatorio()


main()