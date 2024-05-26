import random
import math

'''
RSA, 
credit to Philipp
https://git.pptie.de/Schule/RSA/src/branch/main/main.py

#Sharing_is_caring
'''

# Way more efficient Prime Check
def isPrime(primeCandidate: int):
    for n in range(2, math.floor(math.sqrt(primeCandidate)) + 1): # Komplexe Mathe Zeug Primzahl-Zeug
        if primeCandidate % n == 0: # Modulo, Rest bei Division
            return False

    return True # Ist Primzahli


def randomPrime(start: int, end: int) -> int:
    while True: # So lange, bis eine Primzahl gefunden wurde
        primeCandidate = random.randint(start, end) | 0b01 # Oder-Verknüpfung, damit die Zahl ungerade ist
        if isPrime(primeCandidate): # Überprüfung mit Aufruf der Funktion
            return primeCandidate # Primzahli

def extendenEuclidianAlgorithm(e: int, m: int) -> int:
    eTable = [e] # Aufbau der Tabellen
    mTable = [m] #
    eDivMTable = [e // m] # // Integerdivision, 5/2 = 2 -> Kommawert wird abgeschnitten
    eModMTable = [e % m] #
    i = 0
    while True: # Solange, bis eModMTable[i] == 0, RSA: erste Tabellen-Abfolge/Rechnung (e & m & eDivM & eModM)
        i += 1
        eTable.append(mTable[i - 1])
        mTable.append(eModMTable[i - 1])

        eDivMTable.append(eTable[i] // mTable[i])
        eModMTable.append(eTable[i] % mTable[i])

        if eModMTable[i] == 0:
            break

    aTable = [0] * (i + 1)
    bTable = [1] * (i + 1)

    while True: # RSA: Zweite Tabellen-Abfolge/Rechnung (a & b)
        i -= 1

        aTable[i] = bTable[i + 1]
        bTable[i] = aTable[i + 1] - (eDivMTable[i] * bTable[i + 1])

        if i == 0:
            break

    return aTable[0] # Finished d, von der coolen Tabelle (letztes a)

def rsa():
    p = randomPrime(1000, 10000) # Random Primzahl
    q = randomPrime(1000, 10000)

    n = p * q # Mathe, RSA
    m = (p - 1) * (q - 1)

    while True: # Primfaktorzerlegung
        e = randomPrime(1000, m - 1)
        if m % e != 0: # Rest bei Modulo e soll nicht 0 sein
            break

    d = extendenEuclidianAlgorithm(e, m) # Ausgrechnetes d von der coolen Tabelle

    if d < 0: # RSA: d muss größer als 0 sein
        d += m

    if (0<d and (d*e) % m == 1):
        return [n,e], [n,d]