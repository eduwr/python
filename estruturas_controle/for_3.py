#!/usr/bin/env python3.7

produto = {'nome': 'Caneta Chic', 'preço': 9.99,
           'importada': True, 'estoque': 793}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, ' = ', valor)
