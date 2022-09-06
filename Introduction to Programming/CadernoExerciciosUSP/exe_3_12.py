#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


# Implementação de Funções - - - - - - - - - - - - - - - - - - - - - - - - - -#
def main():
    """
Dadas as populações de Uauá (BA) e Nova York (PI) e sabendo que a população de
Uauá tem um cresimento anual de x e a população de Nova York tem um
crescimento anual de y determine:

* Se a população da cidade menor ultrapasa a da maior
* Quantos anos passarão antes que isso ocorra
    """

    print(main.__doc__)

    populacao_uaua = int(input("Digite a população de Uauá: "))
    taxa_cres_uaua = int(input("Digite a taxa de crescimento: "))

    populacao_nova_york = int(input("Digite a população de Nova York: "))
    taxa_cres_nova_york = int(input("Digite a taxa de crescimento: "))

    if populacao_uaua < populacao_nova_york:
        if taxa_cres_uaua < taxa_cres_nova_york:
            print("Não ultrapassará!")

        else:
            qtde_anos = 0

            while populacao_uaua < populacao_nova_york:
                populacao_uaua = populacao_uaua + taxa_cres_uaua
                populacao_nova_york = populacao_nova_york + taxa_cres_nova_york
                qtde_anos = qtde_anos +1

            print(f'A populacao ultrapassará em {qtde_anos} ano(s).')

    else:
        if taxa_cres_uaua > taxa_cres_nova_york:
            print("Não ultrapassará!")

        else:
            qtde_anos = 0

            while populacao_uaua > populacao_nova_york:
                populacao_uaua = populacao_uaua + taxa_cres_uaua
                populacao_nova_york = populacao_nova_york + taxa_cres_nova_york
                qtde_anos = qtde_anos +1

            print(f'A populacao ultrapassará em {qtde_anos} ano(s).')

    return EX_OK


# Executa o script como sendo o módulo principal - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    import sys
    from os import EX_OK

    codigo_retorno = main(sys.argv)
    sys.exit(codigo_retorno)
