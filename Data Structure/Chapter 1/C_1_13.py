#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
## Outra possibilidae seria fazer: lista[::-1]
## valores padrão do initial e end, initial = 0 e end = len(lista) -1
def reverso(l):
    """
Reverte a ordem dos elementos de uma lista
    """

    tam = len(l) // 2
    i = 0
    j = -1

    while i < tam:
        l[i], l[j] = l[j], l[i]
        i = i +1
        j = j -1

    return l


def main(args):
    """
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than
they were before, and compare this method to an equivalent Python
function for doing the same thing.
    """

    print(main.__doc__)
    lista = [1,2,3,4,5,6]
    print(reverso(lista))
    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
