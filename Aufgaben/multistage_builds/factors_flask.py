# -*- coding: utf-8 -*-
"""
    'factors_flask.py' Module Beschreibung
    Dieses Modul definiert den Code für den Betrieb eines Webservers für die Faktorisierung von Zahlen.
    Das Modul definiert Funktionen, die den folgenden Pfaden entsprechen:

        '/<int:numer>'   - Die Funktion factor ruft find_factors aus dem Modul 'factors.py' auf
                           und gibt einen String zurück, der eine Liste der berechneten Faktoren enthält
                           Rückgabe Status Code von HTTP_200_OK
        '/'              - Die Funktion hello_world gibt eine Zeichenkette mit dem Statuscode HTTP_200_OK zurück.
        '/<path:path>'   - Die Funktion unsupported liefert Informationen über nicht unterstützte Pfade
                           und Nutzungsinformationen mit dem Statuscode HTTP_400_BAD_REQUEST
"""

from timeit import default_timer
from flask import Flask
from flask_api import status
from factors import find_factors

APP = Flask(__name__)

@APP.route('/')
def hello_world() -> str:
    """
        Args:
            keine Argumente erwartet

        Returns:
            str: Begrüssung und Verwendung Hinweistext und Statuscode HTTP_200_OK

        Anmerkung:
            hello_world wird aufgerufen, wenn auf den root-Pfad der Anwendungen zugegriffen wird
    """
    return 'Hallo vom Factoring Server. Bitte versuchen Sie localhost:5000/number mit positiver Ganzzahl'

@APP.route('/<path:path>')
def unsupported(path: str) -> str:
    """
        Args:
            path (path): ein beliebiger Pfad, ausser root und /<int:number>

        Returns:
            str: Begrüssung, Info, dass der Pfad nicht unterstützt wird und Hinweis auf die Verwendung,
                 plus Status Code von HTTP_400_BAD_REQUEST

        Anmerkung:
             unsupported ist eine Auffangfunktion für alle Pfade ausser root oder positive Ganzzahl
    """
    return 'Hallo vom Factoring Server. Faktorisierung von "' \
            + path \
            + '" wird nicht unterstützt. Bitte versuchen Sie localhost:5000/number mit einer positiven Ganzzahl', \
            status.HTTP_400_BAD_REQUEST

@APP.route('/<int:number>')
def factor(number: int) -> str:
    """
        Args:
            number (int): nicht negativerinteger

        Returns:
            str: Zeichenkette mit einer Liste der für das Argument berechneten Faktoren,
                 oder eine Information, dass jede positive ganze Zahl ein Faktor von Null ist.
                 Die Zeit für die Berechnung wird ebenfalls zurückgegeben. Status Code ist HTTP_200_OK.

        Anmerkung:
            Dieser Pfad wird nur bei nicht-negativen ganzen Zahlen verwendet.
            Die Funktion gibt die für die Berechnung der Faktoren benötigte Zeit in Sekunden zurück.
    """
    if number == 0:
        return "Jede positive ganze Zahl ist ein Faktor von 0."
    start = default_timer()
    result = find_factors(number)
    end = default_timer()
    return "Faktoren der " \
           + str(number) \
           + " sind " \
           + str(result).strip('[]') \
           + ". Berechnet in " \
           + str(end-start) \
           + " Sekunden."

if __name__ == '__main__':
    APP.run(debug=False, host='0.0.0.0')
