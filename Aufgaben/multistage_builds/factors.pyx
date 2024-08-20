# -*- coding: utf-8 -*-
""" docstring Module Beschreibung

    Das Modul 'factors.py' definiert eine 'find_factors()'-Funktion,
    die eine nicht-negative ganze Zahl als Argument annimmt und
    eine Liste von positiven ganzen Zahlen zurückgibt, die Faktoren des Arguments sind.

    Das Modul "factors" wird von "find_factors.py" verwendet.

"""

from typing import List
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)

def find_factors(int param):
    """
    Args:
        param (int): nicht-negative integer

    Returns:
        List[int]: eine Liste der Faktoren von param

    Anmerkung:
        Es wird angenommen, dass param positiv ist,
        wenn param Null oder negativ ist, gibt die Funktion [1] zurück.
        Das Modul 'factors_flask.py' führt eine Argumentprüfung durch
        und ruft find_factors nur mit positiven ganzzahligen Argumenten auf.
    """
    result = [1]
    cdef int i
    if param > 1:
        for i in range(2, param+1):
            if param % i == 0:
                result += [i]
    return result
