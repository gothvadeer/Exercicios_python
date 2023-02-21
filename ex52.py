from datetime import date
data = date.today().year
menor = 0
maior = 0

for c in range(1, 8):
    y = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if data - y < 21:
        menor += 1
    else:
        maior += 1
print(f'{menor} pessoas ainda são menor de idade! E {maior} pessoas são maiores de idade!')