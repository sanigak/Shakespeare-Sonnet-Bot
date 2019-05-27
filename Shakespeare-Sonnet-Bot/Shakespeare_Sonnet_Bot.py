from textgenrnn import textgenrnn
from Phyme import Phyme
import random

textgen = textgenrnn()
textgen.train_from_file('sonnets.txt', num_epochs=3)


ph = Phyme()


def getRhymes(word):

    try:
        listy = ph.get_perfect_rhymes(word)
    except:
        return []

    num = len(listy)

    iterator = 1

    outputList = []
    while iterator <= num:
        if iterator in listy:
            listboi = listy[iterator]
            for word in listboi:
                output = word.replace("1","")
                output = output.replace("(","")
                output = output.replace(")","")
                outputList.append(str(output))
        iterator += 1
    return outputList


def generateLine():

    with open("sonnets.txt") as f:
        lineList = f.readlines()
        output = random.choice(lineList)
        output = output.strip("\n")
    return output

def generateNewLine():
    lineNEW = textgen.generate(temperature = .7, return_as_list=True)
    return str(lineNEW[0])



def lastWord(phrase):
    phraseSplit = phrase.split()
    last = phraseSplit[-1]
    last = last.replace(",","")
    last = last.replace(".","")
    last = last.replace("!","")
    last = last.replace(":","")
    last = last.replace(";","")
    last = last.replace("?","")
    return last
    


def generateRhymingLines():


    line1 = generateNewLine()
    line1 = str(line1)
    lastWord1 = lastWord(line1)

    rhymes = []
    rhymes = getRhymes(str(lastWord1))


    

    while len(rhymes) < 40:
        line1 = generateNewLine()
        line1 = str(line1)
        lastWord1 = lastWord(line1)
        rhymes = getRhymes(str(lastWord1))

    try:
        rhymes.remove(lastWord1)
    except:
        print("blarn")


    noRhyme = True
    ity = 0
    while noRhyme:
       
        line2 = generateNewLine()
        line2 = str(line2)
        lastWord2 = lastWord(line2)
        ity+=1
        if ity % 100 == 0:
            print(ity)

        if ity > 200:
            line1 = generateNewLine()
            line1 = str(line1)
            lastWord1 = lastWord(line1)
            rhymes = getRhymes(str(lastWord1))
            try:
                rhymes.remove(lastWord1)
            except:
                print("blarn")



        if str(lastWord2) in rhymes:
            noRhyme = False
    return [line1, line2]



def engine():

    
    usedRhymes = []

    couplet1 = generateRhymingLines()
    last1 = lastWord(couplet1[0])
    rhymes1 = getRhymes(last1)
    usedRhymes = rhymes1 + usedRhymes
    
    print(couplet1)


    couplet2 = generateRhymingLines()
    last2 = lastWord(couplet2[0])
    while last2 in usedRhymes:
        couplet2 = generateRhymingLines()
        last2 = lastWord(couplet2[0])
    rhymes2 = getRhymes(last2)
    usedRhymes = usedRhymes + rhymes2

    print(couplet2)

    couplet3 = generateRhymingLines()
    last3 = lastWord(couplet3[0])
    while last3 in usedRhymes:
        couplet3 = generateRhymingLines()
        last3 = lastWord(couplet3[0])
    rhymes3 = getRhymes(last3)
    usedRhymes = usedRhymes + rhymes3
    print(couplet3)


    couplet4 = generateRhymingLines()
    last4 = lastWord(couplet4[0])
    while last4 in usedRhymes:
        couplet4 = generateRhymingLines()
        last4 = lastWord(couplet4[0])
    rhymes4 = getRhymes(last4)
    usedRhymes = usedRhymes + rhymes4
    print(couplet4)


    couplet5 = generateRhymingLines()
    last5 = lastWord(couplet5[0])
    while last5 in usedRhymes:
        couplet5 = generateRhymingLines()
        last5 = lastWord(couplet5[0])
    rhymes5 = getRhymes(last5)
    usedRhymes = usedRhymes + rhymes5
    print(couplet5)


    couplet6 = generateRhymingLines()
    last6 = lastWord(couplet6[0])
    while last6 in usedRhymes:
        couplet6 = generateRhymingLines()
        last6 = lastWord(couplet6[0])
    rhymes6 = getRhymes(last6)
    usedRhymes = usedRhymes + rhymes6
    print(couplet6)


    couplet7 = generateRhymingLines()
    last7 = lastWord(couplet7[0])
    while last7 in usedRhymes:
        couplet7 = generateRhymingLines()
        last7 = lastWord(couplet7[0])
    rhymes7 = getRhymes(last7)
    usedRhymes = usedRhymes + rhymes7
    print(couplet7)

    print(couplet1[0])
    print(couplet2[0])
    print(couplet1[1])
    print(couplet2[1])

    print(couplet3[0])
    print(couplet4[0])
    print(couplet3[1])
    print(couplet4[1])

    print(couplet5[0])
    print(couplet6[0])
    print(couplet5[1])
    print(couplet6[1])

    print(couplet7[0])
    print(couplet7[1])




engine()
