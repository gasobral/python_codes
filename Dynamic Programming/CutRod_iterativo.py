#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementações de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Implementação iterativa do algoritmo Cut-Rod para resolver o problema
rod-cuting.
    """

    print(main.__doc__)
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    if len(args) == 2:
        n = int(args[1])

    else:
        n = len(p)

    r,s = cut_rod(p, n)
    print(f'{len(r)}\t {r}')
    print(f'{len(s)}\t {s}')
    print(f'Valor ótimo: {r[n]}')
    print_cut_rod_solution(s, n)
    return EX_OK


def cut_rod(p, n):

    r = [0 for i in range(n+1)]
    s = [0 for i in range(n+1)]

    for j in range(1, n+1):
        q = -inf

        for i in range(1, j+1):
            if q < p[i-1] + r[j-i]:
                q = p[i-1] + r[j-i]
                s[j] = i

        r[j] = q

    return r,s


def print_cut_rod_solution(s, n):

    while n > 0:
        print(s[n], end = ' ')
        n = n -s[n]

    print("")


# Executa o script como módulo principal - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from math import inf
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
