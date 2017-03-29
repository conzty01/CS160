import os

def formatOutput(path):
    """This function duplicates the output files of the Shakespeare Monkey Results
       and formats them so that they can be analyzed.  Returns a formatted string.

       Specifically, this function reads an output file as a string and places ','
       where ' ' are located in the generated string."""

    alphabet = "abcdefghijklmnopqrstuvwxyz "

    with open(path, 'r') as inFile:
        l = inFile.read()                                       # Creates string of output file
        tempString = ""
        toggle = False                                          # If '|' has been seen in a line

        for pos, char in enumerate(l):

            if char == " " and toggle:                          # If character is ' ' and follows '|'
                if l[pos - 1] in alphabet and l[pos + 1] in alphabet:
                    tempString += ","
                else:
                    tempString += char

            elif char == "|":
                toggle = True
                tempString += char

            elif char == "\n":                                  # Reached end of 'line'
                toggle = False
                tempString += char

            else:
                tempString += char

    return tempString
def parseOutput(s):
    goalText = ""
    startTime = ""
    endTime = ""
    elapsedTime = ""
    bestPercent = 0.0
    avgPercent = 0.0
    numEntries = 0
    numIters = 0
    t = 0                                                       # Used to calculate avgPercent

    ss = s.split("\n")
    startTime = ss.pop(0)[20:-3]
    goalText = ss.pop(0)[12:-3]
    ss.pop()                                                    # Gets rid of empty line at end of file

    for line in ss:
        sl = line.split()

        if sl[0] == ">>>":                                      # Parses Percentage
            bestPercent = float(sl[-1])
            sl.pop(0)
        t += float(sl[-1])

        numEntries += 1                                         # Parses number of entries and iterations
        numIters = sl[6]

    endTime = line[:24]
    elapsedTime = timeDif(startTime, endTime)

    # return [goalText, startTime, endTime, elapsedTime, bestPercent, avgPercent, numEntries, numIters]
def timeDif(start, end):
    """Takes string representations of start and end times and returns the elapsed time
       Note: this function cannot calculate differences greater than 1 month"""

    if start[4:7] in ["Sep", "Apr", "Jun", "Nov"]:
        numDays = 30
    elif start[4:7] == "Feb":
        if int(start[-4:]) % 4 == 0 and int(start[-4:]) % 100 != 0 or int(start[-4:]) % 400 == 0:
            numDays = 29
        else:
            numDays = 28
    else:
        numDays = 31

    d = (numDays - int(end[8:10])) + int(start[8:10])
    h = (24 - int(end[11:13])) + int(start[11:13])
    m = (60 - int(end[8:10])) + int(start[8:10])
    s = (60 - int(end[8:10])) + int(start[8:10])

    print("{}days {}hours {}minutes {}seconds".format(d,h,m,s))
    return "{}days {}hours {}minutes {}seconds".format(d,h,m,s)

def main():
    path = "D:\\Documents\\Comp Sci\\160\\Monkey Outputs"
    numFiles = 0
    outputList = []
    resList = []

    for file in os.listdir(path):
        if ".txt" in file:
            outputList.append(formatOutput(path+"\\"+file))
            numFiles += 1

    # for output in outputList:
    #     resList.append(parseOutput(output))
    parseOutput(outputList[0])

main()
