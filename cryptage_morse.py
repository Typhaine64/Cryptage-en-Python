# Créé le 05/04/2023 en Python 3.7

"crypte un(e) mot/phrase donné(e)"

alphabet_morse = {"A" : ".-", "À" : ".--.-", "B" : "-...", "C" : "-.-.", "Ç" : "-.-..", "D" : "-..", "E" : ".", "É" : "..-..", "È" : ".-..-", "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--..", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.", "0" : "-----", "." : ".-.-.-", "," : "--..--", "?" : "..--..", "!" : "-.-.--", "'" : ".----.", "/" : "-..-.", "(" : "-.--.", ")" : "-.--.-", "&" : ".-...", ":" : "---...", ";" : "-.-.-.", "=" : "-...-", "+" : ".-.-.", "-" : "-....-", "_" : "..--.-", "$" : "...-..-", "@" : ".--.-.", " " : " "}

def cryptage(phrase_a_crypter):
    a_crypter = phrase_a_crypter.upper()
    message_morse = ""
    for lettre in a_crypter :
        message_morse += alphabet_morse[lettre]
    return message_morse

def decrypt(message_morse):
    #necessite des espaces entre chaque lettre/element (en morse)
    message_morse += ' '
    mot_decrypte = ''
    citext = ''
    for letter in message_morse:
        if (letter != ' '):
            i = 0
            #stock de code morse d'un seul caractère
            citext += letter
        else:
            #si i = 1, ça indique un nouveau caractère
            i += 1
            if i == 2 :
                #si i = 2 ça indique un nouveau mot
                mot_decrypte += ' '
            else:
                #accede aux clefs en utilisant leur valeur
                mot_decrypte += list(alphabet_morse.keys())[list(alphabet_morse.values()).index(citext)]
                citext = ''
    return mot_decrypte
