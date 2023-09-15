from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


import random


class Matrix:
    def __init__(self):
        self.lineCount = 4
        self.numbers = [[0] * 4 for _ in range(4)]
        self.scores = 0
        self.havingScore = False
        self.create(Direction.UP)

    def transformation(self, d: Direction):
        self.havingScore = False
        for i in range(4):
            # 外层
            if d == Direction.LEFT:
                l = list(self.numbers[i])
                l = self.convert(l)
                self.numbers[i] = [n for n in l]
            elif d == Direction.RIGHT:
                l = list(self.numbers[i])
                l.reverse()
                l = self.convert(l)
                l.reverse()
                self.numbers[i] = [n for n in l]
            elif d == Direction.UP:
                l = list([self.numbers[n][i] for n in range(4)])
                l = self.convert(l)
                for n in range(4):
                    self.numbers[n][i] = l[n]
            elif d == Direction.DOWN:
                l = list([self.numbers[n][i] for n in range(4)])
                l.reverse()
                l = self.convert(l)
                l.reverse()
                for n in range(4):
                    self.numbers[n][i] = l[n]
        if self.havingScore:
            self.create(d)

    def convert(self, l, cs=True):
        # ---> 最下面的位置为第一个  0 0 2 0 -> 2 0 0 0
        # 去掉0
        notZero = []
        zero = []
        for n in l:
            if n == 0:
                zero.append(n)
            else:
                notZero.append(n)
            if n != 0 and len(zero) > 0:
                self.havingScore = True
        notZero.extend(zero)
        l = notZero
        # 合并
        for i in range(3):
            if l[i] == l[i + 1] and l[i] != 0:
                l[i] *= 2
                l[i + 1] = 0
                self.havingScore = True
                if cs:
                    self.scores += l[i]

        notZero = []
        zero = []
        for n in l:
            if n == 0:
                zero.append(n)
            else:
                notZero.append(n)
        notZero.extend(zero)
        return notZero

    def create(self, d: Direction):
        if d == Direction.LEFT:
            zeroIndex = []
            for i in range(4):
                if self.numbers[i][3] == 0:
                    zeroIndex.append(i)
            i = random.choice(zeroIndex)
            n = random.choice([2, 4])
            self.numbers[i][3] = n
        elif d == Direction.RIGHT:
            zeroIndex = []
            for i in range(4):
                if self.numbers[i][0] == 0:
                    zeroIndex.append(i)
            i = random.choice(zeroIndex)
            n = random.choice([2, 4])
            self.numbers[i][0] = n
        elif d == Direction.UP:
            zeroIndex = []
            for i in range(4):
                if self.numbers[3][i] == 0:
                    zeroIndex.append(i)
            i = random.choice(zeroIndex)
            n = random.choice([2, 4])
            self.numbers[3][i] = n
        elif d == Direction.DOWN:
            zeroIndex = []
            for i in range(4):
                if self.numbers[0][i] == 0:
                    zeroIndex.append(i)
            i = random.choice(zeroIndex)
            n = random.choice([2, 4])
            self.numbers[0][i] = n

    def isEnd(self):
        self.havingScore = False
        for i in range(4):
            # 外层

            l = list(self.numbers[i])
            self.convert(l, cs=False)

            l = list(self.numbers[i])
            l.reverse()
            self.convert(l, cs=False)

            l = list([self.numbers[n][i] for n in range(4)])
            self.convert(l, cs=False)

            l = list([self.numbers[n][i] for n in range(4)])
            l.reverse()
            self.convert(l, cs=False)
        return not self.havingScore
