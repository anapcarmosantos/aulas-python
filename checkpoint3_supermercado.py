preco_atual = float(input("Informe o preco atual do produto: "))
quantidade_de_vendas  = int(input("Informe a quantidade de vendas: "))

preco_reajustado = 0

if preco_atual <= 30 and quantidade_de_vendas <= 500:
    preco_reajustado = preco_atual + (preco_atual * 10 / 100)
elif (preco_atual >= 30.1 and preco_atual <= 80) and (quantidade_de_vendas >= 501 and quantidade_de_vendas <= 1200):
    preco_reajustado = preco_atual + (preco_atual * 15 / 100)
else:
    preco_reajustado = preco_atual + (preco_atual * 20 / 100)
    

print("O reajuste foi de", preco_reajustado)