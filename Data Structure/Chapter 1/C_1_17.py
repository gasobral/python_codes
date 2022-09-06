#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def scale(data, factor):
    """
    """
    for val in data:
        val *= factor


def main(args):
    """
    """

    data = [1,2]
    factor = 3
    print(f'data: {data} \t factor: {factor}')

    scale(data, factor)
    print(f'data: {data}')
    # o código não funciona, pois val é uma variável local da
    # função scale

    return EX_OK


## Executa o script como módulo principal - - - - - - - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
