frase = str(input('Escreva uma frase: ')).strip()
print(f'Quantas vezes aparece a letra "A" na frase? : {frase.lower().count("a")}')
print(f'Em que posição a letra "A" aparece a 1ª vez?: {frase.lower().find("a")+1}')
print(f'Em que posição a letra "A" aparece a última vez?: {frase.lower().rfind("a")+1}')
