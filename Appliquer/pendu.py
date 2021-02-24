import random
def chooseWord():
    words =["rhinoceros", "dinosaure","xylophone", "montre", "ameublement", "sardine","diagonale", "trigonometrie", "gargantuesque","ver"]
    return (random.choice(words))

randomWord = chooseWord()

def replaceCharacters(randomWord):
    wordSplit = list(randomWord)
    #print (wordSplit)
    for x in wordSplit:
        wordSplit = x.replace(x,"*")
        #print(wordSplit)
        print (wordSplit)
    print (wordSplit)        
        
replaceCharacters(randomWord)


def getLoneDifferentLetter(pastLetters):

#x = words.replace(mot[0], "apples")
#print (x)

