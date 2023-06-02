import random
alphabet = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q', 'R','S','T','U', 'V','W','X','Y','Z']
rotor = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q', 'R','S','T','U', 'V','W','X','Y','Z']
reflector = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q', 'R','S','T','U', 'V','W','X','Y','Z']

random.shuffle(rotor)

random.shuffle(reflector)
reflector.reverse()


def cifrar(mensagem):
  mensagemRetorno = ""
  posicaoAlfabeto = ""
  for letra in mensagem.upper():
    if letra == " ":
       mensagemRetorno += letra
    else:
      posicaoAlfabeto = alphabet.index(letra)
      if posicaoAlfabeto != None:
          letraNoRotor = rotor[posicaoAlfabeto]
          posicaoRefletor = reflector.index(letraNoRotor)
          mensagemRetorno +=  reflector[posicaoRefletor]
  return mensagemRetorno

def decifrar(mensagem):
  mensagemRetorno = ""
  posicaoRefletor = ""
  for letra in mensagem.upper():
    if letra == " ":
       mensagemRetorno += letra
    else:
      posicaoRefletor = reflector.index(letra)
      if posicaoRefletor != None:
          posicaoRotor = rotor.index(letra)
          letraAlfabeto = alphabet[posicaoRotor]
          mensagemRetorno +=  letraAlfabeto
  return mensagemRetorno


textocifrado = cifrar('proFESSOR PEGA LEVe NA GS ')
textodecifrado = decifrar(textocifrado)

print(alphabet)
print(rotor)
print(reflector)

print('TEXTO CIFRADO: ' + textocifrado)
print('TEXTO DECIFRADO: ' + textodecifrado)