#!/usr/bin/env python3.7

from random import randint


def sortear():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 != 0:
        continue

    if i == sortear():
        print('Acertou', i)
        break

else:
    print('ERRRROOOOUU', i)
