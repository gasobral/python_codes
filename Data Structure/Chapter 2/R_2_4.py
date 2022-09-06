#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Classes - - - - - - - - - - - - - - - - - - - - - -#
class Flower:
    """Uma classe que representa uma flor."""

    def __init__(self, pTipo = '', pNumero = 0, pPreco = 0.0):
        self.tipo = pTipo
        self.numero = pNumero
        self.preco = pPreco

    def set_valor(self, pValor):
        self.preco = pValor

    def set_tipo(self, pTipo):
        self.tipo = pTipo

    def set_numero(self, pNumero):
        self.numero = pNumero

    def get_preco(self):
        return self.preco

    def get_tipo(self):
        return self.tipo

    def get_numero(self):
        return self.numero


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Write a Python class, Flower, that has three instance variables of type
str, int and float, that respectively represent the name of the flower,
its number of petals, and its price. Your class must include a
constructor method that initializes each variable to an appropriate
value, and your class should include methods for setting the value of
each type, and retrieving the value of each type.
    """

    print(main.__doc__)

    flor = Flower("Margarida", 22, 80.0)
    print(f'tipo: {flor.get_tipo()} \t número: {flor.get_numero()} \t'
          f'preço: {flor.get_preco()}')

    return EX_OK


# Executa o script como módulo principal para efetuar testes - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
