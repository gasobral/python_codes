#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementações de Funções - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Write a Python program that repeatedly read lines from standard input
until an EOFError is raised, and then outputs those lines in reverse
order (a user can indicate end of input by typing ctrl-D)
    """

    print(main.__doc__)

    lista = []

    try:
        while True:
            linha = str(input())
            lista.append(linha)

    except EOFError:
        print(lista[::-1])

    return EX_OK


## Executa o script como módulo princial - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
