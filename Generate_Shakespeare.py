# This simulation has          10,888,869,450,418,352,160,768,000,000         unique combinations
# Taking an average of                    108,888,694,504,183,521,608         hours
# Which is approximately                    4,537,028,937,674,313,400.333     days
# Or...                                        12,421,708,248,252,740.31576   years
# The average human lifespan is                                    71.0       years

# The current longest time running is:       10:17:13  with  1,027,000,000  iterations
# The highest score (percent correct) is:    0.39285714285714285  reached at  05:01:48

import random
import time

def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res += alphabet[random.randrange(27)]
    return res

def score(goal, testString):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == testString[i]:
            numSame += 1
    return numSame/len(goal)

def main():
    goalString = "methinks it is like a weasel"
    l = len(goalString)
    newString = generateOne(l)
    best = 0
    newScore = score(goalString, newString)
    iteration = 0

    with open("ShakespeareMonkeysOutput.txt", "w") as outFile:
        outFile.write("-- Program began on {} --\n-- String: '{}'\n".format(time.ctime(), goalString))

    while newScore < 1:
        iteration += 1

        if newScore > best:
            t = time.ctime()
            best = newScore
            bestString = newString

            outFile = open("ShakespeareMonkeysOutput.txt", "a")
            outFile.write(">>>"+" "+t+" "+"|"+" "+str(iteration)+" "+bestString+" "+str(best)+"\n")
            outFile.close()

            print(">>>", t, "|", iteration, bestString, best)

        if iteration % 1000000 == 0:
            outFile = open("ShakespeareMonkeysOutput.txt", "a")
            t = time.ctime()
            outFile.write(t+" "+"|"+" "+str(iteration)+" "+newString+" "+str(newScore)+"\n")
            outFile.close()
            print(t, "|", iteration, newString)

        newString = generateOne(l)
        newScore = score(goalString, newString)

    t = time.ctime()
    best = newScore
    bestString = newString

    outFile = open("ShakespeareMonkeysOutput.txt", "a")
    outFile.write(t+" "+"|"+" "+str(iteration)+" "+bestString+" "+str(best))
    outFile.close()

    print(t, "|", iteration, bestString, best)

main()
