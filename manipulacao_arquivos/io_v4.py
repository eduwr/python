#!/usr/bin/env python3.7

# Método usando Streamming

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {} / Idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    pass
finally:
    print('FINALLYYYY')
    arquivo.close()

if arquivo.closed:
    print('Arquivo foi fechado')
