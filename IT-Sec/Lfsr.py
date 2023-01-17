def mensacard(startwert, zufallszahlZx):
    range_ = 0
    iteration = 0
    keep = startwert

    while True:
        if iteration == 8:
            keep = startwert
        polynomial = (
            (startwert & 1)
            ^ (startwert >> 1 & 1)
            ^ (startwert >> 2 & 1)
            ^ (startwert >> 3 & 1)
            ^ (startwert >> 5 & 1)
            ^ (startwert >> 6 & 1)
            ^ (startwert >> 7 & 1)
            ^ (startwert >> 12 & 1)
            ^ (startwert >> 13 & 1)
            ^ (startwert >> 14 & 1)
            ^ (startwert >> 17 & 1)
            ^ (startwert >> 19 & 1)
            ^ (startwert >> 21 & 1)
            ^ (startwert >> 23 & 1)
        ) & 1
        new_start_value = (startwert >> 1) | (polynomial << 23)
        startwert = new_start_value
        new_range = (range_ >> 1) | (polynomial << 31)
        range_ = new_range

        iteration += 1

        if range_ == zufallszahlZx:
            iteration -= 32
            print("Zufallszahl x: " + str(iteration) + " Runden.\n")
            break
        elif startwert == keep:
            print("Fehler nach: " + str(iteration) + " Runden.\n")
            break

zufallszahlZx = 4258377449
startwert = 3087740581
mensacard(startwert, zufallszahlZx)
