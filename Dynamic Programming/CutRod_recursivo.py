#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementações de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Implementação recursiva do algoritmo Cut-Rod para resolver o problema
rod-cuting.
    """

    print(main.__doc__)
    p = [1, 5, 8, 9, 10, 17, 20, 24, 30]
    print(cut_rod(p, len(p)))

    return EX_OK


def cut_rod(p, n):

    if n == 0:
        return 0

    q = -inf

    for i in range(n):
        q = max(q, p[i] + cut_rod(p, n -1))

    return q


# Executa o script como módulo principal - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from math import inf
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
