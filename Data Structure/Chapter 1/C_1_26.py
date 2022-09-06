#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def verifica(a, b, c):
    if a + b == c:
        return True

    if a == b -c:
        return True

    if a * b == c:
        return True

    return False


def main(args):
    """
Write a short program that takes as input three integers, a, b, and c,
from the console and determines if they can be used in a correct
arithmetic formula (in the given order), like "a+b=c", "a=b-c", or
"a*b=c"
    """

    print(main.__doc__)

    a = int(input())
    b = int(input())
    c = int(input())
    print(f'{verifica(a, b, c)}')

    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
