#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
def FibonacciBottomUp(n):
    f = [0 for i in range(n)]
    f[0] = 0
    f[1] = 1
    i = 2

    while i < n:
        res = f[i-1] + f[i-2]
        f[i] = res
        i = i +1

    return f[n-1]


def FibonacciTopDown(n):

    f = [-inf for i in range(n)]
    f[0] = 0
    f[1] = 1
    return FibonacciMemo(n-1, f)


def FibonacciMemo(n, f):

    if n <= 1:
        return f[n]

    if f[n] >= 0:
        return f[n]

    res = FibonacciMemo(n-1, f) + FibonacciMemo(n-2, f)
    return res


def main(args):
    """
Script que testa a implementação de um algoritmo de programação
dinâmica para calcular o n-ésimo termo da sequência de Fibonacci.
    """

    print(main.__doc__)
    n = int(input("Digite um natural: "))
    print(FibonacciBottomUp(n))
    print(FibonacciTopDown(n))
    return EX_OK


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    from math import inf

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
