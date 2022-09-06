#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementações de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Implementação recursiva do algoritmo Cut-Rod para resolver o problema
rod-cuting.
    """

    print(main.__doc__)
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    if len(args) == 2:
        n = int(args[1])
    else:
        n = len(p)

    print(f'Valor da solução:  {memo_cut_rod(p, n)}')
    return EX_OK


def memo_cut_rod(p, n):

    r = [-inf for i in range(n+1)]
    s = [0 for i in range(n+1)]
    val = memo_cut_rod_aux(p, n, r, s)
    print(s)
    i = n
    print('Comprimento dos cortes: ', end = '')

    while i > 0:
        print(s[i], end = ' ')
        i = i -s[i]

    print("")
    return val


def memo_cut_rod_aux(p, n, r, s):

    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0

    else:
        q = -inf
        for i in range(1, n+1):
            t = max(q, p[i-1] + memo_cut_rod_aux(p, n-i, r, s))

            if t > q:
                q = t
                s[n] = i

    r[n] = q
    return q


# Executa o script como módulo principal - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from math import inf
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
