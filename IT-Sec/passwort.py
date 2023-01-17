import hashlib

SALT = "311a36bd7490101b085462b1b9eb9f24"
HASH = "c6dd41240f239cf1a4afc36b39053f3c5ad33652f2fb4c3c00536009db5a2d0a"

SUB_MAP = {
    "a": "6", "e": "7", "i": "8", "o": "4", "u": "8",
    "A": "#", "E": "~", "I": "?", "O": "!", "U": "_"
}

def check_password(password):
    password = SALT + password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password == HASH

def main():
    with open("C:\\Programmieren\\IT-Sec\\Wortliste_Deutsch.txt") as file:
        for word in file:
            word = word.strip()
            for i in range(len(word)):
                for case in [word, word.upper()]:
                    for j in range(2):
                        new_word = case[:i] + SUB_MAP.get(case[i], case[i]) + case[i+1:]
                        print(new_word)
                        if check_password(new_word):
                            print("Found password: ", new_word)
                            return

if __name__ == "__main__":
    main()
