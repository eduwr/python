#! usr/local/bin/python3
# 0, 1, 1, 2, 3, 5, 8, 13, 21,...


def fibonacci(quantidade, sequencia=(0, 1)):
    #importante! Condição de parada

    if len(sequencia) == quantidade:
        return sequencia
    
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]), ))


print(fibonacci(20))