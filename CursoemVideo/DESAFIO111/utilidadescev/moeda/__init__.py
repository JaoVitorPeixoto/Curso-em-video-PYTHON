def aumentar(num, porc, show=False):
    resu = num + (num * (porc/100))

    if show:
        return moeda(resu)
    else:
        return resu


def diminuir(num, porc, show=False):
    resu = num - (num * (porc/100))

    if show:
        return moeda(resu)
    else:
        return resu


def dobro(num, show=False):
    if show:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num, show=False):
    if show:
        return moeda(num / 2)
    else:
        return num / 2


def moeda(valor):
    return f'\033[32mR${valor:.2f}\033[m'


def resumo(num, porcAU, porcDI):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(num):}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{porcAU}% de aumento: \t{aumentar(num, porcAU, True)}')
    print(f'{porcDI}% de redução: \t{aumentar(num, porcDI, True)}')
    print('-'*30)