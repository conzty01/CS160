class State:
    """State object keeps track of the amount of 'water' in two jugs. If amount initialized is greater \
       than the size of the jug, then the jug is set to full"""
    def __init__(self, jug1, jug2, size1=4, size2=3):
        self.size1 = size1
        self.size2 = size2

        if jug1 > size1 or jug2 > size2:                # If start is larger than size, set to filled
            self.jar1 = size1
            self.jar2 = size2
        else:
            self.jar1 = jug1
            self.jar2 = jug2
    def __str__(self):
        return "J1: %i, J2: %i" % (self.jar1, self.jar2)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.jar1 == other.jar1 and self.jar2 == other.jar2
        else:
            return False
    def fillJug1(self):
        self.jar1 = self.size1
        return self
    def fillJug2(self):
        self.jar2 = self.size2
        return self
    def emptyJug1(self):
        self.jar1 = 0
        return self
    def emptyJug2(self):
        self.jar2 = 0
        return self
    def pourJug1Jug2(self):
        water = self.jar1 + self.jar2

        if water >= self.size2:                         # If pouring jar1 into jar2 overfills jar2:
            self.jar2 = self.size2                      #   Fill jar2
            self.jar1 = water - self.size2              #   Set jar1 to the amount of overfill

        else:
            self.jar2 += self.jar1                      # Else add jar1 to jar2
            self.emptyJug1()
        return self
    def pourJug2Jug1(self):
        water = self.jar1 + self.jar2

        if water >= self.size1:                         # If pouring jar1 into jar2 overfills jar2:
            self.jar1 = self.size1                      # Fill jar2
            self.jar2 = water - self.size1              # Set jar1 to the amount of overfill

        else:
            self.jar1 += self.jar2                      # Else add jar1 to jar2
            self.emptyJug2()
        return self
    def copy(self):
        return State(self.jar1, self.jar2, self.size1, self.size2)

def search(moveList, start, goal):

    if start in moveList:                               # Base Case
        return False
    if start == goal:                                   # Base Case
        moveList.append(start)
        return True

    moveList.append(start)
    if search(moveList, start.copy().fillJug1(),     goal) or \
       search(moveList, start.copy().fillJug2(),     goal) or \
       search(moveList, start.copy().pourJug1Jug2(), goal) or \
       search(moveList, start.copy().pourJug2Jug1(), goal) or \
       search(moveList, start.copy().emptyJug1(),    goal) or \
       search(moveList, start.copy().emptyJug2(),    goal):
        return True
    else:
        raise Exception("NO VALID MOVES")

def main():
    goal = State(0,2)
    start = State(0,0)
    moves = []
    search(moves, start, goal)

    print([str(x) for x in moves])

main()