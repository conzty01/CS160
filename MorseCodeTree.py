#   Morse code is binary -> either . or -

#                           (Root)
#                          ./    \-
#                         (e)    (t)
#                        ./ \-  ./ \-
#                       (i) (a) (n) (m)
#           .. = i
#           -. = n   etc...         left child is 2p, right child is 2p+1
from pythonds import BinaryTree

class Morse:
    """Creates a binary tree with ASCII characters that correspond with morse code
       Can encode and decode to and from morse code"""

    def __init__(self, file):
        self.morseTree = BinaryTree(" ")                        # Tree root is a space because I say so

        f = open(file, "r")
        for line in f:
            current = self.morseTree
            t = line.split()

            while t[1]:

                if t[1][0] == ".":                              # If the next character is a .
                    child = current.getLeftChild()
                    if child is None:
                        if len(t[1]) == 1:                      # If the current character is the last character
                            current.insertLeft(t[0])            # Insert new child with the decoded character
                        else:
                            current.insertLeft("INV CHAR")      # Else insert a placeholder "internal" node
                            current = current.getLeftChild()
                    else:                                       # If child is not None (placeholder present)
                        if len(t[1]) == 1:                      # If current character is the last character
                            child.setRootVal(t[0])              # Set child root to decoded character
                        else:
                            current = child                     # Else continue crawling through the tree
                else:
                    child = current.getRightChild()             # Repeat above steps for next character of -
                    if child is None:
                        if len(t[1]) == 1:
                            current.insertRight(t[0])
                        else:
                            current.insertRight("INV CHAR")
                            current = current.getRightChild()
                    else:
                        if len(t[1]) == 1:
                            child.setRootVal(t[0])
                        else:
                            current = child

                t[1] = t[1][1:]                                 # Remove first character from while string
    def decode(self, s):
        """Takes morse code string and returns decoded string"""
        res = ""
        for chrStr in s.lower().split():
            res += self._recDec(chrStr, self.morseTree)
        return res
    def _recDec(self, s, tree):                                 # Recursive helper to decode()
        """Recusive helper to decode method"""
        if len(s) > 0:
            if s[0] == ".":
                return self._recDec(s[1:], tree.getLeftChild())
            else:
                return self._recDec(s[1:], tree.getRightChild())
        else:
            return tree.getRootVal()
    def encode(self, s):
        """Takes a string and returns morse code rep of string"""
        res = ""
        for char in s.lower():
            if char != "(":
                res += str(self._recEnc(char, self.morseTree, "")) + " "
            else:
                res += "-.--.- "
        return res
    def _recEnc(self, char, tree, res):                          # Recursive helper to encode()
        """recursive helper to encode method"""
        if tree:
            if tree.getRootVal() == char:
                return res
            else:
                o1 = self._recEnc(char, tree.getLeftChild(), res+".")
                if o1 is None:
                    return self._recEnc(char, tree.getRightChild(), res+"-")
                else:
                    return o1
def main():
    t = Morse("morse.dat")
    print(t.encode(input("MorseCodePlz")))
    main()

main()
# if __name__ == "__main__":
#     import random
#     t = Morse("morse.dat")
#     print(t.morseTree)
#
#     print(t.encode("hello"))
#     print(t.decode(t.encode("hello")))
#     print(t.decode(t.encode("woah")))
#     print(t.encode("this is a test"))
#     print(t.decode(t.encode("this is a test")))
#     print(t.encode("abcdefghijklmnopqrstuvqxyz.,?;:'_-()/1234567890"))
#     print(t.decode(t.encode("abcdefghijklmnopqrstuvqxyz.,?;:'_-()/1234567890")))
#
#     letters = "abcdefghijklmnopqrstuvqxyz.,?;:'_-()/1234567890"
#     for i in range(10000):
#         test = ""
#         for a in range(random.randrange(1,20)):
#             test += letters[random.randint(0, len(letters)-1)]
#         print(t.encode(test))
#         print(t.decode(t.encode(test)))
