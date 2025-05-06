#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Libaries - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import sys


## Implementation of functions - - - - - - - - - - - - - - - - - - - - -#
def min_machine(M) -> int:
    """
Given M machines, retuns the index of the machine which has the mininum
amount of workload
    """

    k = 0
    sum_task = sum(M[0])

    for i in range(1, len(M)):
        if sum(M[i]) < sum_task:
            sum_task = sum(M[i])
            k = i

    return k


def graham_scheduling(m, n, T) -> list:
    """
Implementation of Graham algoritm to solve scheduling problem, that is,
to find optimal scheduling for M equal machines, n tasks and T times (one
for each task)

Parameters
----------

m: int
    number of machines (considered to be equal)

n: int
    number of tasks

T: list
    list of tasks (each element is the amount of time)

Returns
-------
list
    A partition of t in m elements (an assingment of the tasks into the
    m machines)
    """

    ## create a list with m sets, which represents the m machines
    M = [set() for _ in range(m)]

    ## assign a task to a machine which has the minimum workloads
    for t in T:
        ## find the maxime with minimum amout of tasks assigned
        k = min_machine(M)
        M[k] = M[k] | {t}

    return M


def print_scheduling(M):
    """
Given a scheduling M, return by graham_scheduling, prints its elements
and cost
    """

    ## print element of the scheduling M
    for m in M:
        print(m)

    ## print the cost of scheduling M
    cost = sum(max(M, key=lambda machine: sum(machine)))
    print(f"Cost of scheduling: {cost}")


## Main part of script - - - - - - - - - - - - - - - - - - - - - - - - -#
M = graham_scheduling(3, 7, [4,2,1,5,9,2,6])
print_scheduling(M)
