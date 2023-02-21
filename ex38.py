n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'\033[1;31mSUA MÉDIA FOI {media:.1f} VOCÊ ESTÁ REPROVADO!')
elif (media >= 5) and (media <= 6.9):
    print(f'\033[1;33mSUA MÉDIA FOI {media:.1f} VOCÊ VAI PARA RECUPERAÇÃO!')
else:
    print(f'\033[1;32mSUA MÉDIA FOI {media:.1f} VOCÊ FOI APROVADO(A)!')