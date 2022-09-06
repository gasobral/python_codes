#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def minha_choice(lista):

    indice = randrange(len(lista))
    return lista[indice]


def main(args):
    """
Python's random module includes a function choice(data) tha returns a
random element from a non-empty sequence. The random module includes a
more basic function randrange, with parametrization similar to the
built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version of
the choice function.
    """

    print(main.__doc__)
    print(minha_choice([1,2,3,4,5]))
    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from random import randrange
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
