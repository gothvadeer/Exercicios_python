n = str(input('Digite seu nome: ')).strip().capitalize()
s = str(input('Digite seu gênero [F/M]: ')).strip().upper()[0]
while s != 'M' and s != 'F':
    print('\033[1;31mSEXO INVÁLIDO!')
    s = str(input('\033[mDigite seu gênero [F/M]: ')).strip().upper()[0]
if s == 'M':
    print(f'Seja bem vindo, {n}! Seu gênero [MASCULINO] foi registrado com sucesso!')
if s == 'F':
    print(f'Seja Bem vinda, {n}! Seu gênero [FEMININO] foi registrado com sucesso! ')