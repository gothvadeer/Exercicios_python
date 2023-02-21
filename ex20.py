
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome com letras maiúsculas fica: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas fica: {nome.lower()}')
espaço = nome.replace(" ", "")
print(f'A quantidade de letras do seu nome é: {len(espaço)}')
dividir = nome.split()
print(f'A quantidade de letras do primeiro nome é: {len(dividir[0])}')
