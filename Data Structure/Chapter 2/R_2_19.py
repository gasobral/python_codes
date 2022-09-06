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


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""
    def __init__(self, increment = 1, start = 0):
        """
        Create a new arithmetic progression.
        increment the fixed constant to add to each term (default 1)
        start     the first term of the progression (default 0)
        """
        super.__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment."""
        self._current += self._incremnet


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
def main(args):
    """
When using the ArithmeticProgression class of Section 2.4.2 with an
increment of 128 and a start of 0, how many calls to next can we make
before we reach an integer of 2^63 or larger?
    """

    print(main.__doc__)
    print(f'a_n = 0 + (n-1)128 > 2^63')
    print(f'n > 2^59 +1 calls')
    return EX_OK


## Executa o script como módulo principal para testes - - - - - - - - #
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
