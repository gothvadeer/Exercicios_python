from time import sleep
import emoji
print('\033[1;36m=*'*20)
print(f"\033[1;33m{'QUEIMAÇÃO DE FOGOS EM 10 SEGUNDOS!!!' : ^40}")
print('\033[1;36m=*'*20)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(":fireworks:"*20, language='alias'))
print(emoji.emojize(":boom:"*20, language='alias'))