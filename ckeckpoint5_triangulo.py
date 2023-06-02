A = int (input(" Informe o lado A: " ))
B = int (input(" Informe o lado B: " ))
C = int (input(" Informe o lado C: " ))


if A < B + C and B < A + C and C < A + B:
    if A == B and B == C:
        print("É um Triângulo Equilátero")
    elif A != B and B != C:
        print("Triângulo Escaleno")
    elif A == B and B != C:
        print("Triângulo Isósceles")
else:
    print ("Não é um triangulo")


