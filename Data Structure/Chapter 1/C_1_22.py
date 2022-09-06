#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def dot_product(a, b):
    """
Returns an array of the dot product of a and b.
    """

    c = np.zeros(len(a))

    for i in range(len(a)):
        c[i] = a[i] * b[i]

    return c


def main(args):
    """
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it
returns an array c of length n such that c[i] = a[i] . b[i],
for i = 0, ..., n-1.
    """

    print(main.__doc__)

    a = np.array([1,2,3,4])
    b = np.array([5,6,7,8])
    print(dot_product(a,b))

    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    import numpy as np
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
