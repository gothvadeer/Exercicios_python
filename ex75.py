valores = []
pares = []
pos = nove = 0
while len(valores) < 4:
    num = int(input('Digite um número: '))
    valores.append(num)
    tupla = tuple(valores)
    if num == 9:
        nove += 1
    elif num == 3:
        pos = tupla.index(3) + 1
    elif num % 2 == 0:
        pares.append(num)

print(f'os números digitados foram {tupla}')
print(f'O maior número é {max(tupla)} e o menor número é {min(tupla)}')
print(f'Os números pares digitados são: {pares}')
if 3 in tupla:
    print(f'O valor 3 foi digitado na {pos}º posição')
else:
    print('Não existe 3 na lista digitada')
if nove == 1:
    print('O número 9 foi digitado apenas uma vez')
elif nove >= 2:
    print(f'O valor 9 foi digitado {nove} vezes')
elif nove == 0:
    print(f'O número 9 não foi digitado nenhuma vez')