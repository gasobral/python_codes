#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Classes - - - - - - - - - - - - - - - - - - - - - #
class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):

        if len(self) != len(other):
            raise ValueError('dimensions must agree')

        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')

        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] - other[j]

        return result

    def __neg__(self):
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = -self[j]

        return result

    def __mul__(self, escalar):
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] * 3

        return result

    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Exercise R-2.12 asks for an implementation of __mul__, for the Vector
class of Section 2.3.3, to provide support for the syntax v * 3.
Implement the __rmull__ method, to provide additional support for
syntax 3 * v.
    """

    print(main.__doc__)

    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    u = 3 * v
    print(u)

    return EX_OK


## Executa o script como módulo principal para testes - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
