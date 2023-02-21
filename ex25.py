nome = str(input('Digite seu nome completo: ')).strip()
d = nome.split()
print(f'Primeiro nome: {d [0].capitalize()}')
print(f'Último nome: {d [-1].capitalize()}')