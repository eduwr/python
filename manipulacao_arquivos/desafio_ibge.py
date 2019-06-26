#!/usr/bin/env python3.7

# Método usando Streamming

import csv

with open('desafio-ibge.csv', 'r', encoding="ISO-8859-1") as entrada:
    for campo in csv.reader(entrada):
        print('{}: {}'.format(campo[8], campo[3]))
