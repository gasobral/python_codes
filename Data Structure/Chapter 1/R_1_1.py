#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - -#
def is_multiple(n, m):
    """
Retorna True se n é multiplo de m, caso contrário, retorna False.

Parâmetros
----------
n: um inteiro
m: um inteiro

Retorno
-------
boolean
    True se n é múltiplo de m, caso contrário, False
    """

    if  n % m == 0:
        return True

    return False


def main(args):
    """
Write a short Python function, is_multiple(n, m), that takes two
integers values and returns True if n is multiple of m, that is, n = mi
for some integer i, and False otherwise.
    """

    print(main.__doc__)

    n = int(input("Digite um inteiro: "))
    m = int(input("Digite um inteiro: "))

    print(f'{n} é multiplo de {m}? {is_multiple(n, m)}')
    return EX_OK


# Executa o script como módulo principal - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
