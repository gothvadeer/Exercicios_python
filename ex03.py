a = input ('Digite um algo: ')
print(f'1- Qual o tipo primitivo? {type(a)}')
print(f'2- É númerico? {a.isnumeric()}')
print(f'3- É albético? {a.isalpha()} ')
print(f'4- É um digito? {a.isdigit()}')
print(f'5- Contém letras ou/e números? {a.isalnum()} ')
print(f'6- Está em letras maiúsculas? {a.isupper()} ')
print(f'7- É printável? {a.isprintable()}')
