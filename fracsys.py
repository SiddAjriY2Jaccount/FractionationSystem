'''
ADFGVX Cipher
'''
import string
import numpy as np

#to read input from a file
f=open("sample", "r")
if f.mode == 'r':
    contents = f.read()
print(contents.upper())
plaintext = contents.upper()

lengthplain = len(plaintext)
print(plaintext)
alphabet = list(string.ascii_uppercase)
#Fractionation system consists of 2-level encryption
#Substitution Cipher + Transposition Cipher = Fractionation System

keysquare = "ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8"
keysquare = keysquare.upper()
print(keysquare)

def populateSubsMatrix(text, keysquare):
    z=0
    listtoencrypt = [['P' for i in range(6)] for j in range(6)]
    while z!=len(keysquare):
        for i in range(6):
            for j in range(6):
                listtoencrypt[i][j] = keysquare[z]
                z+=1
        return listtoencrypt

listtoencrypt = populateSubsMatrix(plaintext, keysquare)
print(listtoencrypt)

dict1 = {0:"A", 1:"D", 2:"F", 3:"G", 4:"V", 5:"X"}

#Key to encrypt, can accept from user as well
key = "612345"

#First, Poly alphabetic substitution encryption
def encrypt1(text, listtoencrypt, dict1, keysquare):
    result = ""
    replace = ""
    row = column = i = j = otherchars = 0
    for x in text:
        if x in keysquare:
            for i in range(6):
                for j in range(6):
                    if listtoencrypt[i][j] == x:
                        row = i
                        column = j
                        break
            replace = dict1[row] + dict1[column]
            result += replace
        else:
            otherchars +=1
            continue
    return result

ciphertext1 = encrypt1(plaintext, listtoencrypt, dict1, keysquare)
print(ciphertext1)

keysize = len(key)

#Second, Transposition -> Columnar Transposition
def encrypt2(ciphertext1, keysize, key):
    result = ""
    numRows = numCols = z = o = x1 = 0
    for x in ciphertext1:
        if len(ciphertext1)%keysize==0 :
            print(ciphertext1)
            break
        else:
            ciphertext1 += 'J' #Padding

    numRows = int((len(ciphertext1))/keysize)
    numCols = keysize

    listtotranspose = [['P' for i in range(numCols)] for j in range(numRows)]
    #for x in ciphertext1:
    while z!=len(ciphertext1):
        for i in range(numRows):
            for j in range(numCols):
                listtotranspose[i][j] = ciphertext1[z]
                z+=1

    print("List to transpose :\n")
    print(listtotranspose)

    #finallist = [['P' for i in range(numCols)] for j in range(numRows)]
    finallist = np.array(listtotranspose)
    print(finallist)
    keyaslist = []
    for x in key:
        x1 = int(x)-1
        keyaslist.append(x1)
    print(keyaslist)
    keyasarray = np.array(keyaslist)
    finalenclist = finallist[:,keyasarray]
    print(finalenclist)
    finalenclist = finalenclist.tolist()
    print(finalenclist)
    for i in range(numRows):
        for j in range(numCols):
            result += finalenclist[i][j]
    print(result)
    return(result)

finalenctext = encrypt2(ciphertext1, keysize, key)
print("\n\nFinal encrypted result :\n")
print(finalenctext)
