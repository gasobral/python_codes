#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Implementação de Classes - - - - - - - - - - - - - - - - - - - - - #
class Progression:
    """
Iterator producing a generic progression.
Default iterator produces the numbers 0,1,2,...
    """
    def __init__(self, start = 0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """
        Update self._current to a new value.
        This sohuld be overriden by a subclass to customize
        progression. By convention, if current is set to None, this
        designates the end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """
        Return the next element, or else raise StopIteration error.
        """
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """
        By convention, an iterator must return itself as an iterator.
        """
        return self

    def print_progression(self, n):
        """
        Print next n values of the progression.
        """
        print(' '.join(str(next(self)) for j in range(n)))


class FibonacciProgression(Progression):
    """Iterator produciing a generalized Fibonacci progression."""

    def __init__(self, first = 0, second = 1):
        """
        Create a new Fibonacci progression.
        first  the first term of the progression (default 0)
        second the secod term of the progression (default 1)
        """
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current,\
            self._prev + self._current


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to find the 8th value of a Fibonacci progression
that starts with 2 and 2 as its first two values.
    """

    print(main.__doc__)

    fibo = FibonacciProgression(2, 2)
    fibo.print_progression(8)

    return EX_OK


## Executa o script como módulo principal para testes - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
