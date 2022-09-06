#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implemenetação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
São dados dois números inteiros positivos p e q, sendo que o número e dígitos\
de p é menor igual ao número de dígitos de q. Verificar se p é um subnúmero\
de q.

Exemplos:
p = 23, q = 57238, p é subnúmero de q.
p = 23, q = 258347, p não é subnúmero de q.
    """

    print(main.__doc__)

    print("Digite o valor de q:")
    q = int(input())
    print("Digite o valor de p:")
    p = int(input())

    div_q = q
    div_p = p
    achou = False

    while div_q != 0 and achou == False:
        dezena_q = div_q % 10
        dezena_p = div_p % 10

        if dezena_p == dezena_q:
            div_p = div_p // 10
            dezena_p = div_p % 10

            if dezena_p == 0 and div_p == 0:
                achou = True

        else:
            div_p = p
            dezena_p = div_p % 10

        div_q = div_q // 10

    if achou == True:
        print(f'{p} é subnúmero de {q}')
    else:
        print(f'{p} não é subnúmero de {q}')

    return EX_OK


# Script Principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
