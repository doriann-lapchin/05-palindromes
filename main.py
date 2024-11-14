"""Module providing a function"""

#### Fonction secondaire

def ispalindrome(p):
    """Function printing python version."""
    alphabet = [chr(i) for i in range(65, 123)]
    for i in range(0,10):
        alphabet.append(str(i))
    liste = []
    tsil = []
    a = str.maketrans("À, Â, Ä, É, È, Ê, Ë","A, A, A, E, E, E, E")
    b = str.maketrans("Î, Ï, Ô, Ö, Ù, Û, Ü, Ç","I, I, O, O, U, U, U, C")
    p = p.upper()
    p = p.translate(a)
    p = p.translate(b)
    q = p[::-1] # la chaîne inversée
    for letters in p:
        if letters in alphabet:
            liste.append(letters)
    for letters in q:
        if letters in alphabet:
            tsil.append(letters)
    if liste == tsil:
        return True
    return False

#### Fonction principale

def main():
    """Function printing python version."""
    ispalindrome('azerty')
    ispalindrome('kàyàk')
    ispalindrome('azereza')
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
