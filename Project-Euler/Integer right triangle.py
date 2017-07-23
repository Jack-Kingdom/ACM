# Integer right triangles
from math import sqrt

MAX_PERIMETER = 1000


class RightTriangle(object):
    def __init__(self, *args):
        self.__side1 = args[0]
        self.__side2 = args[1]
        self.__complete()

    # calculate side3 and perimeter
    def __complete(self):
        self.__side3 = sqrt(self.__side1 ** 2 + self.__side2 ** 2)
        self.__perimeter = self.__side1 + self.__side2 + self.__side3

    def perimeter(self):
        return self.__perimeter

    def jude(self):
        global MAX_PERIMETER
        if self.__perimeter % 1 == 0 and self.__perimeter <= MAX_PERIMETER:
            return True
        else:
            return False


if __name__ == '__main__':
    # store solution in MyList
    MyList = [0 for _ in xrange(0, MAX_PERIMETER + 1)]

    for i in xrange(1, MAX_PERIMETER / 2):
        for j in xrange(1, MAX_PERIMETER / 2):
            tmp = RightTriangle(i, j)
            if tmp.jude():
                # if jude is true, let solution number add one
                MyList[int(tmp.perimeter())] += 1

    # print perimeter of triangle that has max solutions
    Max_Solution = max(MyList)
    for i in xrange(1, MAX_PERIMETER + 1):
        if MyList[i] == Max_Solution:
            print(i)
