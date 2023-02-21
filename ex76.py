produtos = ({"nome": "Pão", "preço": 5.89}, {"nome": "Queijo", "preço": 19.80},
            {"nome": "Linguiça", "preço": 13.99}, {"nome": "Coca-Cola", "preço": 8.20},
            {"nome": "Biscoito", "preço": 2.45}, {"nome": "Mussarela","preço": 2.00}, { "nome": "Batata","preço": 7.22})
print('Produto    | Preço')
print('~'*20)
for lista in produtos:
    print(f"{lista['nome']:<10} | R$ {lista['preço']:.2f}")
print('~'*20)