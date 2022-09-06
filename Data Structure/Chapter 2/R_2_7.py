#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Classes - - - - - - - - - - - - - - - - - - - - - -#
class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, nonzero = None):
        """Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g. 'John Bowman')
        bank     the name of the bank (e.g. 'California Savings')
        acnt     the account identifier (e.g. '5391 0375 9387 5309')
        limit    credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit

        if nonzero == None:
            self._balance = 0

        else:
            self._balance = nonzero

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a
           string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given prive to the card, assuming sufficient credit
        limit.
        Return True if charge was processed; False if charga was
        denied."""

        if not isinstance(price, (int, float)):
            raise TypeError('price must be numeric')

        if price + self._balance > self._limit:
            return False

        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""

        if not isinstance(amount, (int, float)):
            raise TypeError('amount must be numeric')

        if self._balance - amount < 0:
            raise ValueError('balance is negative')

        self._balance -= amount


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
The CreditCard class of Section 2.3 initializes the balance of a new
account to zero. Modify that class so that a new account can be given a
nonzero balance using an optinal fifth parameter to the constructor.
The four-parameter constructor syntax should continue to produce an
account with zero balance.
    """

    print(main.__doc__)
    return EX_OK


# Executa o módulo principal para fazer testes - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
