zahlZufall = 4258377449
startWert = 3087740581
iIdx, erg, r = 0,0,0
polArr = [0, 1, 2, 3, 5, 6, 7, 12, 13, 14, 17, 19, 21, 23]
x = startWert
while True:
    if iIdx == 8:
        x = startWert
    pol = sum([(startWert >> i) & 1 for i in polArr]) & 1
    startWert = (startWert >> 1) | (pol << 23)
    r = (r >> 1) | (pol << 31)
    iIdx += 1
    if r == zahlZufall:
        iIdx = iIdx - 32
        erg = iIdx
        break
print(iIdx)