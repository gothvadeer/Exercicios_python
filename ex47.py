n = int(input('Digite um número para ver sua tabuada: '))
print(f' \033[36m=*'*10)
for c in range(0,11):
    print(f'\033[m{n} x {c} = {n*c}')
print(f'\033[36m=*'*10)