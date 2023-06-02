frutas = {} 


frutas = {'maça': 5, 'banana': 8, 'laranja': 12}
frutas ['abacaxi'] = 7
qtde_macas = frutas['maça']

def temItemNoDicionario(item):
   if item in frutas:
     return True
   
   return False


temItemNoDicionario('pêssego')
del frutas["laranja"]  

print(frutas)
print(qtde_macas)