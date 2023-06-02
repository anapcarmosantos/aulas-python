lista1 = {"prof1":["Ana", 20, "Professora"], "prof2":["Maria", 40, "Professora"]}

def add():
    lista1["prof3"] = ["Andre", 50, "Professor"]

def delete()  :
    del lista1["prof1"]  

def relatorio():
    for index, lista in lista1.items ():
        print("Id......", index)
        print("Nome.....", lista[0])
        print("Idade.....", lista[1])
        print ("Cargo.....",lista[2])

relatorio()

        
      