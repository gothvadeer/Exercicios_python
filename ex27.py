from time import sleep

km = int(input('Escreva há quantos km/h você está: '))
print('\033[1;32mCALCULANDO A VELOCIDADE...\033[m')
sleep(3)
if km > 80:
    print('\033[1mVOCÊ ESTÁ MUITO RÁPIDO!!!')
    print(f'\033[1;31mVOCÊ FOI MULTADO EM R$ \033[40m{(km-80)*7:.2f}\033[m ')
else:
    print('\033[1mDentro do limite!')
