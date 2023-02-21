lista = []
for p in range(1,6):
    lista.append(float(input(f'Digite o peso da {p}ª pessoa: ')))
print(f'O maior peso é: {max(lista)}KG \nE o menor peso é: {min(lista)}KG')