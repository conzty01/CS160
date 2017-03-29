import math
import random

class Matrix:
    def __init__(self, col, row):
        self.numRows = row
        self.numCol = col
        # Create matrix of specified dimensions with empty values
        self.container = [[0 for r in range(row)] for c in range(col)]

    def __repr__(self):
        return "Matrix(%i x %i)" % (self.numCol, self.numRows)

    def __str__(self):
        retStr = ""
        for col in self.container:
            retStr = retStr + str(col) + "\n"
        return retStr

    def __mul__(self, other):
        # http://www.mathwarehouse.com/algebra/matrix/multiply-matrix.php
        pass

    def insert(self, number, ypos, xpos):
        self.container[ypos][xpos] = number

class Neural_Network:
    def __init__(self):
        # Define HyperParameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3

        # Weight (parameters)
        self.W1 = random.randint(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = random.randint(self.hiddenLayerSize, self.outputLayerSize)

    def forward(self, x):
        # Propagate inputs through network
        self.z2 = x * self.W1
        self.a2 = self.sigmoid(self.z2)
        self.z3 = self.a2 * self.W2
        yHat = self.sigmoid(self.z3)
        return yHat

    def sigmoid(self, z):
        # Apply sigmoid activation function
        return 1/(1+math.e**(-z))

matrix = Matrix(3,3)
print(matrix)
matrix.insert(5,1,1)
print(matrix)
