from textgenrnn import textgenrnn
from Phyme import Phyme
import random

textgen = textgenrnn()
textgen.train_from_file('sonnets.txt', num_epochs=3)


ph = Phyme()


def getRhymes(word):

    listy = ph.get_perfect_rhymes(word)

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


    try:
        rhymes = getRhymes(str(lastWord1))
    except:
        generateRhymingLines()

    try:
        rhymes.remove(lastWord1)
    except:
        print("blarn")

    while len(rhymes) < 5:
        line1 = generateNewLine()
        rhymes = getRhymes(str(lastWord1))

    noRhyme = True

    while noRhyme:
        print("LINE 1: " + line1)
        line2 = generateNewLine()
        line2 = str(line2)
        lastWord2 = lastWord(line2)


        if str(lastWord2) in rhymes:
            noRhyme = False
    return [line1, line2]


print(generateRhymingLines())