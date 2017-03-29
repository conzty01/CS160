import random

class Card:

    def __init__(self, rank, suit):
        self.__suit = suit
        self.__rank = rank

    def __str__(self):
        return str(self.__rank)+" of "+str(self.__suit)

    def __repr__(self):
        return "Card(%s of %s)" % (self.__rank, self.__suit)

    def getRank(self):
        return self.__rank
    rank = property(getRank)

    def getSuit(self):
        return self.__suit
    suit = property(getSuit)
class Deck:

    def __init__(self):
        self.__cardList = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in range(2,11):
                self.__cardList.append(Card(rank,suit))
            self.__cardList.append(Card("Jack",suit))
            self.__cardList.append(Card("Queen",suit))
            self.__cardList.append(Card("King",suit))
            self.__cardList.append(Card("Ace",suit))

    def __str__(self):
        return str([str(item) for item in self.__cardList])

    def __len__(self):
        return len(self.__cardList)

    def __repr__(self):
        return "Deck(%i Cards)" % (len(self.__cardList))

    def shuffle(self):
        for c in range(random.randint(3,6)):
            for i in self.__cardList:
                self.__cardList.append(self.__cardList.pop(random.randrange(0,len(self.__cardList))))

    def draw(self):
        return self.__cardList.pop(0)

    def restock(self, cardList):
        topCard = cardList.pop(0)
        for card in cardList:
            self.__cardList.insert(random.randint(0,len(cardList)), card)
        self.__cardList.insert(0,topCard)

    def size(self):
        return len(self.__cardList)
class Pile:

    def __init__(self):
        self.cardList = []

    def __str__(self):
        return str([str(item) for item in self.cardList])

    def __len__(self):
        return len(self.cardList)

    def __repr__(self):
        return "Pile(%i Cards)" % (len(self.cardList))

    def add(self, card):
        self.cardList.insert(0, card)

    def remove(self):
        return self.cardList.pop(0)

    def removeAll(self):
        a = self.cardList
        self.cardList = []
        return a

    def topRank(self):
        return self.cardList[0].getRank()

    def topSuit(self):
        return self.cardList[0].getSuit()
class CrazyPile(Pile):

    def __init__(self):
        super().__init__()
        self.crazySuit = None

    def add(self, card):
        if self.crazySuit != None:
            if card.getSuit() == self.crazySuit:
                self.cardList.insert(0, card)
                self.crazySuit = None
            elif card.getRank() == 8 or len(self.cardList) == 0:
                self.cardList.insert(0, card)
            else:
                raise Exception("INVALID ACTION: '%s' on '%s'" % (card, self.cardList[0]))
        else:
            if card.getRank() == 8 or len(self.cardList) == 0:
                self.cardList.insert(0, card)
            elif card.getRank() == self.topRank() or card.getSuit() == self.topSuit():
                self.cardList.insert(0, card)
            else:
                raise Exception("INVALID ACTION: '%s' on '%s'" % (card, self.cardList[0]))

    def setCrazySuit(self, suitName):
        self.crazySuit = suitName
        print("Suit set to %s" % suitName)

    def getCrazySuit(self):
        return self.crazySuit
class Hand:

    def __init__(self):
        self.__cardList = []

    def __getitem__(self, pos):
        return self.__cardList[pos]

    def __str__(self):
        return str([str(item) for item in self.__cardList])

    def __repr__(self):
        return "Hand(%i Cards)" % (len(self.__cardList))

    def add(self, card):
        self.__cardList.append(card)

    def remove(self, pos):
        return self.__cardList.pop(pos)

    def numInSuit(self, suit):
        count = 0
        for card in self.__cardList:
            if card.getSuit() == suit:
                count += 1
        return count

    def numInRank(self, rank):
        count = 0
        for card in self.__cardList:
            if card.getRank() == rank:
                count += 1
        return count

    def findCard(self, rank, suit):
        for index in range(len(self.__cardList)):
            if self.__cardList[index].getSuit() == suit and self.__cardList[index].getRank() == rank:
                return index

        return -1

    def findRank(self, rank):
        rankList = []
        for index in range(len(self.__cardList)):
            print(index, self.__cardList[index])
            if self.__cardList[index].getRank() == rank:
                rankList.append(index)
        return rankList
        return [index for index in range(len(self.__cardList)) if self.__cardList[index].getRank() == rank]

    def findSuit(self, suit):
        suitList = []
        for index in range(len(self.__cardList)):
            print(index, self.__cardList[index])
            if self.__cardList[index].getSuit() == suit:
                suitList.append(index)
        return suitList
        return [index for index in range(len(self.__cardList)) if self.__cardList[index].getSuit() == suit]

    def cardAt(self, pos):
        return self.__cardList[pos]

    def size(self):
        return len(self.__cardList)
class Player:                                           # Computer AI

    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.turnNum = 0

    def __repr__(self):
        return "Player('%s', %d card(s): %s)" % (self.name, self.hand.size(), self.hand)

    def __str__(self):
        return "'%s' has %d card(s): %s" % (self.name, self.hand.size(), self.hand)

    def organizeHand(self):
        pass

    def drawOneCard(self, deck):
        self.hand.add(deck.draw())

    def mostOfSuit(self):                               # Determines which suit in hand has most cards
        indexOf8s = self.hand.findRank(8)               # Used to exclude '8's from tally since they can be played anytime
        tempStore8s = []

        indexOf8s.reverse()                             # Negates pop() out of range error
        for index in indexOf8s:
            tempStore8s.append(self.hand.remove(index)) # Removes '8's from hand before tally
        indexOf8s.reverse()

        tempList = [
            ("Hearts",self.hand.numInSuit("Hearts")),
            ("Diamonds",self.hand.numInSuit("Diamonds")),
            ("Clubs",self.hand.numInSuit("Clubs")),
            ("Spades",self.hand.numInSuit("Spades"))
            ]
        tempList = sorted(tempList, key= lambda suit: suit[1], reverse=True)
        # Above sorts the tuples in tempList with respect to index 1 of each tuple and sorts them in descending order

        for index in range(len(indexOf8s)):             # Puts '8's back in hand where they were
            self.hand.add(tempStore8s[index])

        return tempList[0][0]                           # Returns suit with most cards

    def mostOfRank(self, rank):                         # Determines which suit of given rank has most cards
        indexOf8s = self.hand.findRank(8)               # Used to exclude '8's from tally since they can be played anytime
        tempStore8s = []

        indexOf8s.reverse()                             # Negates pop() out of range error
        for index in indexOf8s:
            tempStore8s.append(self.hand.remove(index)) # Removes '8's from hand before tally
        indexOf8s.reverse()

        indexOfRank = self.hand.findRank(rank)

        tempSuitList = [self.hand.cardAt(cIndex).getSuit() for cIndex in indexOfRank]
                                                        # Append suit of all cards with rank to tempSuitList

        tempList = [(cardSuit, self.hand.numInSuit(cardSuit)) for cardSuit in tempSuitList]
                                                        # Append suit of rank cards to tempList

        tempList = sorted(tempList, key=lambda theSuit: theSuit[1], reverse=True)
        # Above sorts the tuples in tempList with respect to index '1' of each tuple and sorts them in descending order

        for card in tempStore8s:                        # Puts '8's back in hand
            self.hand.add(card)

        return tempList[0][0]                           # Returns suit of rank with most cards

    def considerChange(self, tRank, num8):              # Consider changing suit
        indexOf8s = self.hand.findRank(8)               # Used to exclude '8's from tally since they can be played anytime
        tempStore8s = []

        indexOf8s.reverse()                             # Negates pop() out of range error
        for index in indexOf8s:
            tempStore8s.append(self.hand.remove(index)) # Removes '8's from hand before tally
        indexOf8s.reverse()

        posRank = self.hand.findRank(tRank)             # Creates list of indexes for cards matching desired rank
                                                        #   this is used to avoid errors with an 8 on top of pile
        for card8 in tempStore8s:
            self.hand.add(card8)

        if len(posRank) == 0:
            if num8 > 0:                                # If player can only by an '8' card
                mostSuit = self.mostOfSuit()
                return (self.hand.findRank(8)[0], mostSuit)
            else:                                       # If player cannot change
                return None
        else:                                           # If player can change by rank
            mostSuit = self.mostOfRank(tRank)
            re = (self.hand.findCard(tRank,mostSuit),)
            return re

    def canPlay(self, tSuit):                           # Determine if card can be played from hand to pile
        posList = self.hand.findSuit(tSuit)
        tempList = []

        for pos in posList:                             # Exclude the '8's
            if self.hand[pos].getRank() == 8:
                tempList.append(posList.pop(posList.index(pos)))

        if len(posList) > 0:                            # If number of suit cards in hand is greater than 0
            for index in range(len(tempList)):          # Put '8's back in hand
                self.hand.add(tempList[index])
            return True
        else:
            for index in range(len(tempList)):          # Put '8's back in hand
                self.hand.add(tempList[index])
            return False

    def playOneTurn(self, deck, diPi):                  # Player AI returns True if hand is empty
        self.turnNum += 1
        num8 = self.hand.numInRank(8)
        if diPi.getCrazySuit() == None:                 # If there is NOT an '8' on the discard pile
            tSuit = diPi.topSuit()                      # get suit and rank of top card
            tRank = diPi.topRank()
        else:
            tSuit = diPi.getCrazySuit()                 # get the suit the 8 changed to
            tRank = 8

        if self.canPlay(tSuit) == True:                 # If the player can play on suit
            playedCard = self.hand.remove(self.hand.findSuit(tSuit)[0])
            diPi.add(playedCard)
            # adds first card found of playable suit  -> should not be an 8 since 8s are appended to back of hand
            print("%s played %s from hand" % (self.getName(), playedCard))

        else:                                           # If the player can change the suit
            changeToPos = self.considerChange(tRank, num8)
            if changeToPos != None:
                if len(changeToPos) == 2:
                    playedCard = self.hand.remove(changeToPos[0])
                    diPi.add(playedCard)
                    diPi.setCrazySuit(changeToPos[1])
                    print("%s played %s from hand" % (self.getName(), playedCard))
                    print("%s set suit to %s" % (self.getName(), diPi.getCrazySuit()))
                else:
                    playedCard = self.hand.remove(changeToPos[0])
                    diPi.add(playedCard)
                    print("%s played %s from hand" % (self.getName(), playedCard))

            else:                                       # Player cannot not change suit and cannot play
                self.drawOneCard(deck)
                print("%s drew from the deck" % self.getName())

        if self.hand.size() == 0:                       # Checks if player hand is empty
            return True
        else:
            return False

    def getName(self):
        return self.name

    def myHand(self):
        return self.hand
class RealPlayer(Player):                               # Real-Life player

    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return "RealPlayer('%s', %d card(s): %s)" % (self.name, self.hand.size(), self.hand)

    def __str__(self):
        return "'%s' has %d card(s): %s)" % (self.name, self.hand.size(), self.hand)

    def playOneTurn(self, deck, diPi):
        self.turnNum += 1

        print(self,"\n")
        action = input("What would you like to do?\n   Draw, Play Card, Quit\n").lower()

        if action == "draw":                            # If player would like to draw
            drawnCard = deck.draw()
            self.hand.add(drawnCard)
            print("You drew the %s" % drawnCard)

        elif action == "play" or action == "play card":  # If player would like to play a card
            validRankNums = "123456789"                  # Used to check if rank should be converted to an int()
            doSetCrazy = False

            playCard = input("What card would you like to play?\n   ex: _____ of _____\n").lower()
            splitList = playCard.split("of")
            for i in range(len(splitList)):             # Get rid of white space
                splitList[i] = splitList[i].strip()

            rank = splitList[0].capitalize()            # Format to match the rank of suit of cards
            suit = splitList[1].capitalize()

            if rank[0] in validRankNums:                # Turn str numbers to int numbers
                rank = int(rank)
                if rank == 8:
                    doSetCrazy = True

            diPi.add(self.hand.remove(self.hand.findCard(rank, suit)))
            if doSetCrazy == True:
                diPi.setCrazySuit(input("What suit would you like to change the pile to?\n   Hearts, Diamonds, Clubs, Spades\n").capitalize())

        elif action == "quit":                          # Quit the game
            raise Exception("You Quit The Game.")

        else:                                           # Input did not match options
            raise Exception("Invalid Action")

        if self.hand.size() == 0:                       # Checks if player hand is empty
            return True
        else:
            return False

def randomizeOrder(playerList):
    order = []
    for player in playerList:
        order.insert(random.randint(0,len(order)), player)

    return order

#random.seed(42)

numAI = int(input("How many Computer players would you like?\nMax number: 7  Current number: 0\n"))
numReal = int(input("How many live players would you like?\nMax number: 7  Current number: %i \n" % numAI))
if numAI + numReal > 7:
    raise Exception("ERROR: Too many players.  Max number: 7  Requested number: %i" % (numAI + numReal))

aiList = [Player("Comp %i" % num) for num in range(numAI)]
realList = []
for num in range(numReal):
    name = input("Enter name of real player %i  " % (num + 1))
    realList.append(RealPlayer(name))

order = randomizeOrder(aiList + realList)

# Initialize Deck and Discard Pile
d = Deck()
disPile = CrazyPile()
d.shuffle()

# Deal to hands
for i in range(7):
    for player in order:
        player.drawOneCard(d)
print(order)
disPile.add(d.draw())

doneDict = dict.fromkeys(order, False)
finished = False
turnNum = 0
while not finished:
    turnNum += 1

    for player in order:
        print("top of pile:   %s of %s\n" % (disPile.topRank(), disPile.topSuit()))
        if disPile.getCrazySuit() != None:
            print("Suit is set to %s" % disPile.getCrazySuit())

        isDone = player.playOneTurn(d, disPile)
        if isDone:                                      # If player has empty hand, set doneDict key to True,
            doneDict[player] = isDone                   #  break turn cycle, and set finished to terminate game
            finished = True
            break

        if d.size() == 0:
            temp = disPile.remove()
            d.restock(disPile.removeAll())
            disPile.add(temp)

        print("---------------------------------------------\n")

for player in doneDict.keys():
    if doneDict[player]:
        print("Player %s has won!\n" % player.getName())

    print(player)
