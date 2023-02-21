c = str(input('Digite o nome de uma cidade: ')).strip()
s = c.lower().split()
print(f'Ela começa com SANTO? : {"santo" in s[0]}')
