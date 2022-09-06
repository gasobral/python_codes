#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - -#
def verificar_par_produto_impar(lista):
    """
Given a list, check if there is two numbers whose product is odd.
Just scan the list and check if there is at least two odd numbers.
If there is so, then returns True, since the product of two odd numbers
is odd.
    """

    qtde_numeros_impares = 0

    for x in lista:
        if x % 2 == 1:
            qtde_numeros_impares += 1

    if qtde_numeros_impares > 1:
        return True

    return False


def main(args):
    """
Write a short Python function that takes a sequence of integer values
and determines if there is a disctin pair of numbers in the sequence
whose product is odd.
    """

    print(main.__doc__)
    lista = [1,2,4,5]
    print(f'lista: {lista}')
    print(verificar_par_produto_impar(lista))
    return EX_OK


# Executa o script como módulo principal - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
