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

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
In Section 2.3.3, we note that our Vector class supports a syntax such
as v = u + [5,3,10,-2,1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5,3,10,-2,1] + u os illegal.
Explain how the Vector class defintion can be revised so that this
syntax generates a new vector.
    """

    print(main.__doc__)

    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    u = [5,3,10,-2,1] + v
    print(u)
    total = 0

    for entry in v:
        total += entry

    print(f'total: {total}')
    return EX_OK


## Executa o script como módulo principal para testes - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
