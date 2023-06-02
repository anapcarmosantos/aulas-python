#Dados
nome = input("Entre com o nome do paciente: ")
idade = int(input("Entre com a idade do paciente: "))
doencas = input("Possue Doenças cronicas (S ou N): ").upper()
temperatura = float(input("Entre com a temperatura: "))
pressao = float(input("Entre com a pressão: "))
#Processamento
 
#Saida
 
if idade > 60:
    print("Atendimento prioritario!")
    if (pressao > 14.5 or temperatura > 40.5):
        print("Emergencia")
    elif (pressao > 12.8 or temperatura > 38):
        print("Urgencia")
    else:
        print("Vai pra observação!")
else:
    print("Fluxo etario normal!")
    if (pressao > 14.5 or temperatura > 40.5):
        print("Emergencia")
    elif (pressao > 12.8 or temperatura > 38) and doencas == "S":
        print("Urgencia")
    else:
        print("Vai pra casa!")
