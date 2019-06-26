#!/usr/bin/env python3.7

# Método usando Streamming

arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')), end='\n')
arquivo.close()
