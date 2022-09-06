#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementações de Funções - - - - - - - - - - - - - - - - - - - - -#
def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k

        k = k +1

    while k > 0:
        if n % k == 0:
            yield n // k
        k  = k -1


def main(args):
    """
In Section 1.8, we provided three different implementations of a
generator that computes factors of a given integer. The third of those
implementations, from page 41, was the most efficient, but we noted
that it did not yield the factor in increasing order. Modify the
generators so that it reports in increasing order, while maintaining
its general perfomance advantages.
    """

    print(main.__doc__)
    n = int(input("Digite um inteiro: "))

    for fator in factors(n):
        print(fator)

    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
