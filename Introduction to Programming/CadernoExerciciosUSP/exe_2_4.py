#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Dados n e uma sequência de n números inteiros positivos, calcular a soma dos
números da sequência que são primos.
    """

    n = int(input("Digite um número inteiro: "))
    soma = 0

    for i in range(n):
        numero = int(input("Informe um número: "))
        e_primo = True

        if numero <= 1:
            e_primo = False

        else:
            j = 2
            while j < numero and e_primo == True:
                if numero % j == 0:
                    e_primo = False

                j = j + 1
                
        if e_primo == True:
            soma = soma + numero

    print(f'A soma dos números primos é {soma}.')
    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
