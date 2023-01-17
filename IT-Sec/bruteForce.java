import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class bruteForce {

	public static String SALT = "311a36bd7490101b085462b1b9eb9f24";
	public static String HASH = "c6dd41240f239cf1a4afc36b39053f3c5ad33652f2fb4c3c00536009db5a2d0a";

	public static char ASUBSONDER = '#';
	public static char ESUBSONDER = '~';
	public static char ISUBSONDER = '?';
	public static char OSUBSONDER = '!';
	public static char USUBSONDER = '_';

	public static char ASUBZAHL = '6';
	public static char ESUBZAHL = '7';
	public static char ISUBZAHL = '8';
	public static char OSUBZAHL = '4';
	public static char USUBZAHL = '8';

	public static void main(String[] args) {

		Scanner scan = null;
		try {
			scan = new Scanner(new File("C:\\GitProgrammieren\\Python\\Python\\IT-Sec\\Wortliste_Deutsch.txt"));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		while (scan.hasNext()) {

			String word = scan.nextLine();
			String word1Upper = lower2Upper(word, 0);
			String word2Upper = lower2Upper(word, 1);

			for (int i1 = 0; i1 < 2; i1++) {
				if (i1 == 1) { // Zweite Runde zweiter Buchstaben Gro�
					word1Upper = word2Upper;
				}
				System.out.println(word1Upper);
				int[] vokalPos = new int[50];
				for (int i = 0; i < vokalPos.length; i++) {
					vokalPos[i] = -1;
				}

				int vokalCounter = 0;
				for (int i = 0; i < word1Upper.length(); i++) {
					if (word1Upper.charAt(i) == 'a' || word1Upper.charAt(i) == 'e' || word1Upper.charAt(i) == 'i'
							|| word1Upper.charAt(i) == 'o' || word1Upper.charAt(i) == 'u') {
						vokalPos[vokalCounter] = i;
						vokalCounter++;
					}
				}

				String wordVokalSwap1 = word1Upper;
				for (int j = 0; j < vokalPos.length; j++) {
					if (vokalPos[j] == -1) {
						break;
					}
					// Erste Vertauschung

					if (wordVokalSwap1.charAt(vokalPos[j]) == 'a') {
						wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j]) + ASUBZAHL
								+ wordVokalSwap1.substring(vokalPos[j] + 1);
					}
					if (wordVokalSwap1.charAt(vokalPos[j]) == 'e') {
						wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j]) + ESUBZAHL
								+ wordVokalSwap1.substring(vokalPos[j] + 1);
					}
					if (wordVokalSwap1.charAt(vokalPos[j]) == 'i') {
						wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j]) + ISUBZAHL
								+ wordVokalSwap1.substring(vokalPos[j] + 1);
					}
					if (wordVokalSwap1.charAt(vokalPos[j]) == 'o') {
						wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j]) + OSUBZAHL
								+ wordVokalSwap1.substring(vokalPos[j] + 1);
					}
					if (wordVokalSwap1.charAt(vokalPos[j]) == 'u') {
						wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j]) + USUBZAHL
								+ wordVokalSwap1.substring(vokalPos[j] + 1);
					}

					String wordVokalSwap1zws = wordVokalSwap1; // EINE Sub Zahl

					for (int j2 = 0; j2 < vokalPos.length; j2++) { // Erste Sub festgehalten, f�r alle M�glichen 2
																	// durchgef�hrt
						if (j == j2)
							continue; // Kann man machen sicherer
						if (vokalPos[j2] == -1)
							break;

						// Tauschen zum zweiten
						if (wordVokalSwap1.charAt(vokalPos[j2]) == 'a') {
							wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j2]) + ASUBSONDER
									+ wordVokalSwap1.substring(vokalPos[j2] + 1);
						}
						if (wordVokalSwap1.charAt(vokalPos[j2]) == 'e') {
							wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j2]) + ESUBSONDER
									+ wordVokalSwap1.substring(vokalPos[j2] + 1);
						}
						if (wordVokalSwap1.charAt(vokalPos[j2]) == 'i') {
							wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j2]) + ISUBSONDER
									+ wordVokalSwap1.substring(vokalPos[j2] + 1);
						}
						if (wordVokalSwap1.charAt(vokalPos[j2]) == 'o') {
							wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j2]) + OSUBSONDER
									+ wordVokalSwap1.substring(vokalPos[j2] + 1);
						}
						if (wordVokalSwap1.charAt(vokalPos[j2]) == 'u') {
							wordVokalSwap1 = wordVokalSwap1.substring(0, vokalPos[j2]) + USUBSONDER
									+ wordVokalSwap1.substring(vokalPos[j2] + 1);
						}

						// An diesem Punkt zwei Substitustuionen Stattgefunden
						// Zahlen einf�gen und Hash berechnen
						for (int i = 1; i < 21; i++) {
							String counterWord = wordVokalSwap1 + i;
							try {
								String hash = toHexString(getSHA(counterWord + SALT));
								if (hash.equals(HASH)) {
									System.out.println("Pass: " + counterWord + " Hash: " + hash);
									System.exit(1);
								}
							} catch (NoSuchAlgorithmException e) {
								System.out.println("Exception thrown for incorrect algorithm: " + e);
							}

						}

						wordVokalSwap1 = wordVokalSwap1zws;
					}

					wordVokalSwap1 = word1Upper;

				}

			}

		}
		scan.close();

	}

	public static String lower2Upper(String message, int pos) {
		char newChar = message.charAt(pos);
		newChar = Character.toUpperCase(newChar);
		message = message.replaceFirst(String.valueOf(message.charAt(pos)),
				String.valueOf(newChar));

		return message;
	}

	public static byte[] getSHA(String input) throws NoSuchAlgorithmException {
		// Static getInstance method is called with hashing SHA
		MessageDigest md = MessageDigest.getInstance("SHA-256");

		// digest() method called
		// to calculate message digest of an input
		// and return array of byte
		return md.digest(input.getBytes(StandardCharsets.UTF_8));
	}

	public static String toHexString(byte[] hash) {
		// Convert byte array into signum representation
		BigInteger number = new BigInteger(1, hash);

		// Convert message digest into hex value
		StringBuilder hexString = new StringBuilder(number.toString(16));

		// Pad with leading zeros
		while (hexString.length() < 64) {
			hexString.insert(0, '0');
		}

		return hexString.toString();
	}

}
