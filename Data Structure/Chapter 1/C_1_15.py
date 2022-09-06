#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def verifica_distinto(lista):
    """
Verifica se os elementos da lista são distintos.
    """

    i = 0

    while i < len(lista):
        j = i +1

        while j < len(lista):
            if lista[i] == lista[j]:
                return False

            j += 1

        i += 1

    return True


def main(args):
    """
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they
are distinct)
    """

    print(main.__doc__)
    lista = [1,2,3,4,5,1]
    print(verifica_distinto(lista))
    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
