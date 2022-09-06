#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Classes - - - - - - - - - - - - - - - - - - - - - -#
class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False

        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - -#
def main(args):
    """
Modify the declaration of the first loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually one of the three credit
cards to go over its credit limit. Which credit is it?
    """

    print(main.__doc__)

    wallet = []
    wallet.append(CreditCard('John Bowman' , 'California Savings',\
                             '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman' , 'California Federal',\
                             '3485 0399 3395 1954' , 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance',\
                             '5391 0375 9387 5309', 5000))
    val = 1

    while wallet[0].charge(val) != False and\
          wallet[1].charge(val) != False and\
          wallet[2].charge(val) != False:
        val = val +1

#    for val in range(1, 17):
#        wallet[0].charge(val)
#        wallet[1].charge(val * 2)
#        wallet[2].charge(val * 3)


    for c in range(3):
        print(f'Customer = {wallet[c].get_customer()}')
        print(f'Bank = {wallet[c].get_bank()}')
        print(f'Account = {wallet[c].get_account()}')
        print(f'Limit = {wallet[c].get_limit()}')
        print(f'Balance = {wallet[c].get_balance()}\n')

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print(f'New balance = {wallet[c].get_balance()}')

    return EX_OK


# Executa o script como módulo principal para efetuar testes - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK
    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
