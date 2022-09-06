#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def norm(v, p):
    """
Computes the p-norm of a vector v = (v1, v2, ..., vn).
    """

    norma = 0

    for componente in v:
        norma = norma + componente ** 2

    return sqrt(norma)


def main(args):
    """
    """

    v = [4,3]
    p = 2
    print(norm(v, p))
    return EX_OK


## Executa o script como módulo principal, para testes de             #
## implementação                                                      #
if __name__ == "__main__":
    import sys
    from math import sqrt
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
