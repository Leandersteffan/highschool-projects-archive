import random


def eintag(basis=0.1, Betrag=25):
    aktuellewette = basis
    while True:
        if Betrag >= 50:
            return 50
        if Betrag <= 0.2:
            return 0
        if spiel():
            Betrag += (aktuellewette)
            aktuellewette = basis
        else:
            Betrag -= aktuellewette
            aktuellewette = aktuellewette * 2

        if aktuellewette > Betrag:
            aktuellewette = basis

def spiel():
    if "red" == random.choices(["red", "black", "green"], [18 / 37, 18 / 37, 1 / 37])[0]:
        return True
    else:
        return False

def multidaysimulation(days):
    summe = 0
    for i in range(days):
        summe = summe + (eintag() - 25)
        print(summe)
    return summe



print(multidaysimulation(1000))