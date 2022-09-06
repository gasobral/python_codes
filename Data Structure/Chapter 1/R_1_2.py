#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - -#
def is_even(k):
    """
Retorna true se k é par, caso contrário, retorna False.

Parametros
----------
k : int
    um inteiro

Retorno
-------
True
     se k é par.
False
     se k é ímpar.
    """

    if k & 1 == 0:
        return True

# solução alternativa, se k é par, então deslocar os bits dele uma
# ver para direita e depois para a esquerda, então o número resultante
# desta operação é igual a k. Caso contrário, k é impar.
#    if ((k >> 1) << 1) == k:
#        return True

    return False


def main(args):
    """
Write a short Python function, is_even(k), that takes an integer value
and returns True if k is even, and False otherwise. However, your
function cannot use the multiplifcation, modulo or divsion operators.
    """

    print(main.__doc__)

    k = int(input("Digite um inteiro: "))
    print(f'{k} é par: {is_even(k)}')
    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
