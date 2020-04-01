import pyAesCrypt
import os
bufferSize = 64 * 1024


def encrypt():
    inputFile = str(input("Bitte Pfad der datei eingeben: "))
    password = str(input("Bitte Gewünschtes Passwort eingeben: "))
    pyAesCrypt.encryptFile(inputFile, inputFile+".aes", password, bufferSize)
    os.remove(inputFile)

def decrypt():
    inputFile = str(input("Bitte Pfad der verschlüsselten Datei angeben: "))
    if inputFile.endswith('.aes'):
        outPutfile = inputFile[:-4]
        password = str(input("Passwort: "))
        pyAesCrypt.decryptFile(inputFile, outPutfile, password, bufferSize)
        os.remove(inputFile)
    else:
        print("Die eingegebene Datei ist nicht verschlüsselt oder existiert nicht!")


print("1. Verschlüsseln")
print("2. Entschlüsseln")
choice = int(input("Bitte Funktion Wählen: "))
if choice == 1:
    encrypt()
elif choice == 2:
    decrypt()
else:
    print("Nicht unterstütze Wahl, bitte erneut versuchen")