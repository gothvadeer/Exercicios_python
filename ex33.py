r1 = float(input('Digite o 1º comprimento de reta: '))
r2 = float(input('Digite o 2º comprimento de reta: '))
r3 = float(input('Digite o 3º comprimento de reta: '))
if (r2 + r3 > r1) and (r3 + r1 > r2) and (r1 + r2 > r3):
    print(f'\033[1;32mSim, é possível fazer um triangulo!')
else:
   print(f'\033[31mNão, não é possível fazer um triângulo')