#!/usr/bin/env python3.7

for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)

for x in range(1, 11):
    if x == 5:
        break
    print(x)

print('Fim!')
