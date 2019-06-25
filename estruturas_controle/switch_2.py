#!/usr/bin/env python3.7

# SIMULANDO SWITCH CRIAR FUNÇÂO QUE DIZ SE O DIA É DA SEMANA OU FIM DE SEMANA


# def dia_semana(dia):
#     dias = {
#         1: 'Domingo não é dia da semana',
#         2: 'Segunda é dia de semana',
#         3: 'Terça é dia de semana',
#         4: 'Quarta é dia de semana',
#         5: 'Quinta é dia de semana',
#         6: 'Sexta é dia de semana',
#         7: 'Sábado não é dia da semana',
#     }
#     return dias.get(dia, 'dia inválido')


# dia = int(input('informe o dia: '))

# print(dia_semana(dia))

def get_tipo_dia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, '**inválido**')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')
