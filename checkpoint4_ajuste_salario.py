cargo = str(input(" Informe o cargo "))
salario = float (input("Informe o salario do funcionario "))
percentual_reajuste = float (input("Informe o reajuste do funcionario "))

salario_reajustado = salario + (salario * percentual_reajuste/ 100)
salario_reajustado_bonus = 0

if cargo == "Analista Jr":
    salario_reajustado_bonus = salario_reajustado + (salario_reajustado * 2.0 / 100)
elif cargo == "Analista Pleno":
     salario_reajustado_bonus = salario_reajustado + (salario_reajustado * 2.5 / 100)
elif cargo == "Analista Senior":
     salario_reajustado_bonus = salario_reajustado + (salario_reajustado * 3.0 / 100)
elif cargo == "Arquiteto":
     salario_reajustado_bonus = salario_reajustado + (salario_reajustado * 4.0 / 100)
elif cargo == "Gerente":
     salario_reajustado_bonus = salario_reajustado + (salario_reajustado * 4.5 / 100)
     
print("O reajuste foi de", salario_reajustado_bonus)




