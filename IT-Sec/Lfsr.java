public class Lfsr {
    static void mensacard(long startwert, long zufallszahlZx) {

        long range = 0;
        long iteration = 0;
        long keep = startwert;

        while (true) {
            if (iteration == 8) {
                keep = startwert;
            }

            long polynomial = ((startwert & 1)
                    ^ ((startwert >> 1) & 1)
                    ^ ((startwert >> 2) & 1)
                    ^ ((startwert >> 3) & 1)
                    ^ ((startwert >> 5) & 1)
                    ^ ((startwert >> 6) & 1)
                    ^ ((startwert >> 7) & 1)
                    ^ ((startwert >> 12) & 1)
                    ^ ((startwert >> 13) & 1)
                    ^ ((startwert >> 14) & 1)
                    ^ ((startwert >> 17) & 1)
                    ^ ((startwert >> 19) & 1)
                    ^ ((startwert >> 21) & 1)
                    ^ ((startwert >> 23) & 1)) & 1;

            long newStartValue = (startwert >> 1) | (polynomial << 23);
            startwert = newStartValue;
            long newRange = (range >> 1) | (polynomial << 31);
            range = newRange;

            iteration++;

            if (range == zufallszahlZx) {
                iteration -= 32;
                System.out.println("Zufallszahl x: " + iteration + " Runden.\n");
                break;
            } else if (startwert == keep) {
                System.out.println("Fehler nach: " + iteration + " Runden.\n");
                break;
            }
        }
    }

    public static void main(String[] args) {
        long zufallszahlZx = 4258377449L;
        long startwert = 3087740581L;
        mensacard(startwert, zufallszahlZx);
    }
}