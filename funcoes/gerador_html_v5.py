#!/usr/bin/env python3.7
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **kwargs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **kwargs)
    atributos = get_atrs(kwargs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **kwargs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {get_atrs(kwargs, ul_atrs)}>{lista}</ul>'


if __name__ == "__main__":
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'sábado', 'domingo',
                    classe='info', inline=True))

    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_acesskey='m', bloco_id='conteudo', ul_id='lista'))
