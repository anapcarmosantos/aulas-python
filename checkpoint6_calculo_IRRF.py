salario_bruto = float (input(" Informe o salario bruto: "))
numero_dependentes = int ( input (" informe numero dos dependentes:" ))
aliquota_IRRF = 0

contribuicao_INSS = 0
deducao_por_dependente = 179.71

if salario_bruto <= 1903.98:
    print ("Contribuinte insento")
else:
    if salario_bruto >= 1903.99 and salario_bruto <= 2826.65:
        aliquota_IRRF = 7.5
    elif salario_bruto >= 2826.66 and salario_bruto <= 3751.05:
        aliquota_IRRF = 15
    elif salario_bruto >= 3751.06 and salario_bruto <= 4664.68:
        aliquota_IRRF = 22.5
    elif salario_bruto >= 4664.68 : 
        aliquota_IRRF = 27.5

    if salario_bruto >= 1302.01 and salario_bruto <= 2571.29:
        contribuicao_INSS = (salario_bruto /100) * 9.0
    elif salario_bruto >= 2571.30 and salario_bruto <= 3856.94:
        contribuicao_INSS = (salario_bruto /100) * 12.0
    elif salario_bruto >= 7507.49:
        contribuicao_INSS = (salario_bruto /100) * 14.0
        
salario_DESCONTADO = salario_bruto - contribuicao_INSS- ( numero_dependentes* deducao_por_dependente)
print("SALARIO DESCONTADO", salario_DESCONTADO)
        



