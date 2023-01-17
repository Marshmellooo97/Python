from typing import List

def lfsr(Zx: int, start: int, polynomial: int) -> int:
    # Anzahl der Iterationen (Zeiteinheiten)
    iterations = 0

    # LFSR simulieren, bis Zx erreicht wurde
    while start != Zx:
        # nächster Wert des LFSR berechnen
        next = (start >> 1) ^ (polynomial if start & (1 << 23) else 0)
        start = next
        iterations += 1

    # Ergebnis zurückgeben
    return iterations

# Test des LFSR
print(lfsr(833235991, 2260308005, 0b1000001011100010000010100001))