#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

# Description - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Code written by gasobral@gmail.com                                          #
# This program loads bibtex files and make annotations to it.                 #

# Module Import - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys

# Functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def read_cmd():
    """
    Function      : read_cmd
    Arguments     : none
    Description   :
    Reads a command from command from keyboard
    Return Values :
    pointer to function \t if it's a valid command it's the address to it
    None \t if Ctrl-D or Ctrl-C is typed
    """

    user_cmd = ""

    while (user_cmd in know_cmd.keys()) == False :
        try :
            user_cmd = input()

        except (KeyboardInterrupt, EOFError) :
            return None

    return know_cmd[user_cmd]


def main(args) :
    """
    Function      : main
    Arguments     : sys.argv
    Description   :
    This program loads bibtex files, create notes to it and remove unused\n\
    references.
    Return Values :
    0 \t if executed without errors
    1 \t if an error has occurred
    """

    print(main.__doc__)

    # --> variable initialization #
    exit_status = False # used to control if leave the program or not #
    user_cmd = ""       # it has the command read from keyboard       #

    # --> main loop of the script, which commands are read and executed #
    while exit_status == False :
        user_cmd = read_cmd()

        if user_cmd == None :
            exit_status = True

    return 0


# Data Structures - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# { function_name = key : function_pointer = value } #
know_cmd = {'main' : main}

# Main Script - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
return_code = 0

if __name__ == "__main__" :
    return_code = main(sys.argv)

sys.exit(return_code)
