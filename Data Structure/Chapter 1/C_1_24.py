#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementaçoes de Funções - - - - - - - - - - - - - - - - - - - - -#
def conta_vogais(frase):
    """
Return the number os vowels in the sentence frase.
    """

    qtde_vogais = 0
    vogais = ['a', 'e', 'i', 'o', 'u']

    for letra in frase:
        if letra in vogais:
            qtde_vogais += 1

    return qtde_vogais


def main(args):
    """
Write a short Python function that counts the number of vowels in a
given character string.
    """

    print(main.__doc__)
    frase = input()
    print(f'Conta vogais: {conta_vogais(frase)}')
    return EX_OK


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
