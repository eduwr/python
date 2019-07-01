# [ expressão for item in list if condicional ]

dobros = [i * 2 for i in range(10)]
print(dobros)

# versão "normal"
dobros = []
for i in range(10):
    dobros.append(i * 2)
print(dobros)

# com condicional

dobros_dos_pares = []
for i in range(10):
    if i % 2:
        dobros_dos_pares.append(i * 2)
print(dobros_dos_pares)
