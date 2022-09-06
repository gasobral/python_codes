#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação das Funções - - - - - - - - - - - - - - - - - - - - -#
def minha_shuffle(lista):
    for i in range(len(lista)):
        novo_indice = random.randint(i, len(lista) -1)
        lista[novo_indice], lista[i] = lista[i], lista[novo_indice]


def main(args):
    """
Python's random module includes a function shuffle(data) that accepts a
list of elementos and randomly reorders the elements so that each
possible order occurs with equal probability. The random module
includes a more basic function randint(a, b) that returns a uniformily
random integer from a to b (including both endpoints). Using only the
randint function, implement you own version of the shuffle function.
    """

    print(main.__doc__)
    lista = [1,2,3,4,5,6]
    minha_shuffle(lista)
    print(lista)
    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    import random
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
