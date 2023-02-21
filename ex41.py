print('\033[36m=*'*8)
print('\033[mCALCULE SEU IMC')
print('\033[36m=*'*8)

altura = float(input('\033[mDigite sua altura: (m) '))
peso = float(input('Digite seu peso: (Kg) '))
imc = peso / (altura**2)

if imc <= 18.5:
    print(f'Seu imc é de {imc:.1f} e você está ABAIXO DO PESO!')
elif imc <= 25:
    print(f'Seu imc é de {imc:.1f} você está com o PESO IDEAL!')
elif imc <= 30:
    print(f'Seu imc é de {imc:.1f} você está com SOBREPESO!')
elif imc <= 40:
    print(f'Seu imc é de {imc:.1f} e você está com OBESIDADE!')
else:
    print(f' Seu imc é de {imc:.1f} e você está com OBESIDADE MÓRBIDA!')
