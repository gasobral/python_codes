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

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError('dimension must agree!')

        result = 0

        for j in range(len(self)):
            result = result + self[j] * other[j]

        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Implement the __mull__ method for the Vector class of Section 2.3.3, so
that the expression u * v returns a scalar that represents the dot
product the of vectors.
    """

    print(main.__doc__)

    v = Vector(5)
    v[0] = 1
    v[1] = 2
    v[2] = 3
    v[3] = 4
    v[4] = 5

    u = Vector(5)
    u[0] = 0
    u[1] = 1
    u[2] = 0
    u[3] = 1
    u[4] = 0

    print(u * v)

    return EX_OK


## Executa o script como módulo principal para testes - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
