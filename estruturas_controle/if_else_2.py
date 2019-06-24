#!/usr/bin/env python3.7


def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'menor de idade'
    elif idade in range(18, 64):
        return 'adulto'
    elif idade in range(65, 100):
        return 'melhor idade'
    elif idade >= 100:
        return 'centenário'
    else:
        return 'idade inválida'


if __name__ == "__main__":
    for idade in (5, -5, 18, 65, 100, 150):
        print(f'{idade}: {faixa_etaria(idade)}')
