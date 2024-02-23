# Créé le 06/04/2023 en Python 3.7

def crypter(phrase_a_coder, clef):
    clef=int(clef)
    if clef > 26 :
        clef=clef%26

    acrypter=phrase_a_coder.upper()
    lg=len(acrypter)
    phrase_a_coder = ""

    for i in range(lg):
        if acrypter[i]==' ':
            phrase_a_coder+=' '
        else:
            asc=ord(acrypter[i])+clef
            phrase_a_coder+=chr(asc+26*((asc<65)-(asc>90)))
    return phrase_a_coder


def decrypter(phrase_a_decoder, clef):
    clef=int(clef)
    phrase_a_decoder = phrase_a_decoder.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat = ""

    for letter in phrase_a_decoder:
        if letter in alphabet: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alphabet.find(letter) - clef) % len(alphabet)

            resultat = resultat + alphabet[letter_index]
        else:
            resultat = resultat + letter

    return resultat
