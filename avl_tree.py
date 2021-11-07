
from stack.StackOnList import StackOnList



class TreeN(object):
    def __init__(self, value):
        self.intitValue = value
        self.left = None
        self.right = None
        self.height = 1


class Avl(object):

    def adde(self, r, key):

        if not r:
            return TreeN(key)
        elif key < r.intitValue:
            r.left = self.adde(r.left, key)
        else:
            r.right = self.adde(r.right, key)
        r.height = 1 + max(self.findH(r.left),
                           self.findH(r.right))

        b = self.getb(r)

        if b > 1 and key < r.left.intitValue:
            return self.right(r)

        if b < -1 and key > r.right.intitValue:
            return self.left(r)

        if b > 1 and key > r.left.intitValue:
            r.left = self.left(r.left)
            return self.right(r)

        if b < -1 and key < r.right.intitValue:
            r.right = self.right(r.right)
            return self.left(r)
        return r

    def left(self, b):
        a = b.right
        t = a.left
        a.left = b
        b.right = t
        b.height = 1 + max(self.findH(b.left),
                           self.findH(b.right))
        a.height = 1 + max(self.findH(a.left),
                           self.findH(a.right))
        return a

    def right(self, b):
        a = b.left
        tr = a.right
        a.right = b
        b.left = tr
        b.height = 1 + max(self.findH(b.left),
                           self.findH(b.right))
        a.height = 1 + max(self.findH(a.left),
                           self.findH(a.right))
        return a

    def findH(self, r):
        if not r:
            return 0
        return r.height

    def getb(self, r):
        if not r:
            return 0
        return self.findH(r.left) - self.findH(r.right)

    @staticmethod
    def porder(r):
        result = []
        if r is None:
            return
        mass = []
        mass.append(r)
        while (len(mass) > 0):
            n = mass.pop()
            result.append(n.intitValue)

            if n.right is not None:
                mass.append(n.right)
            if n.left is not None:
                mass.append(n.left)
        return result
    @staticmethod
    def iorder(r):
        now = r
        arr = []
        result = []

        while True:
            if now is not None:
                arr.append(now)
                now = now.left

            elif (arr):
                now = arr.pop()
                result.append(now.intitValue)
                now = now.right
            else:
                break
        print()
        return result
    @staticmethod
    def posorder(r):
        myStack = []
        result = []
        while (True):
            while (r != None):
                myStack.append(r)
                myStack.append(r)
                r = r.left
            if (len(myStack) == 0):
                return result
            r = myStack.pop()
            if len(myStack) > 0 and myStack[-1] == r:
                r = r.right
            else:
                result.append(r.intitValue)
                r = None

    def level(self, r, level, result):
        if r is None:
            return
        if level == 1:
            result.append(r.intitValue)
        elif level > 1:
            self.level(r.left, level - 1, result)
            self.level(r.right, level - 1, result)

    def level_ord(self, r):
        result = []
        height = self.findH(r)
        for i in range(1, height + 1):
            self.level(r, i, result)
        return result
    @staticmethod
    def sort(mas):
        T = Avl()
        a = None
        for i in mas:
            a = T.adde(a, i)
        return Avl.iorder(r)
if __name__ == "__main__":
    Tree = Avl()
    r = None
    r = Tree.adde(r, 1)
    r = Tree.adde(r, 2)
    r = Tree.adde(r, 3)
    r = Tree.adde(r, 4)
    r = Tree.adde(r, 5)
    r = Tree.adde(r, 6)
    print(Avl.iorder(r))
    print(Avl.porder(r))
    print(Avl.posorder(r))
    print(Tree.level_ord(r))
    mas = [10,9,8,7,6,5,4,3,2,1]
    print(Avl.sort(mas))

