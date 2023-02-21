count = 0
maior = 0
media = 0
oldboy = ''
m = 0
for c in range(1, 5):
    print(f"\033[36m{f'{c}ª PESSOA ': ^20}")
    n = str(input('\033[mDigite o nome: ')).strip().upper()
    i = int(input('Idade: '))
    s = str(input('Sexo [F/M] : ')).strip().upper()
    media += i
    m = media / 4
    if s == 'M':
        if i == 1:
            maior = i
            oldboy = n
        else:
            if i > maior:
                maior = i
                oldboy = n
    if s == 'F':
        if i < 20:
            count += 1
print(f'A média de idade do grupo é {m:.1f} anos')
#condições singular mulheres
if count >= 2:
    print(f'Há {count} mulheres com menos de 20 anos no grupo')
elif count == 1:
    print(f'Há {count} mulher com menos de 20 anos no grupo')
elif count == 0:
    print('Não há nenhuma mulher com menos de 20 anos no grupo')
#condições homens
if maior == 0:
    print('Não há homens nesse grupo')
else:
    print(f'O homem mais velho se chama {oldboy} e tem {maior} anos')


