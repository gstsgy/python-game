import random
import copy

from tetris.Mino import Mino


class Matrix:
    def __init__(self):
        self.scores = 0

    def isEnd(self):
        pass


class BaseBox:
    def __init__(self):
        self.initX = 4
        self.initY = 2
        self.O = Mino(self.initX, self.initY)
        self.O.block.append([0, 0])
        self.O.block.append([1, 0])
        self.O.block.append([0, 1])
        self.O.block.append([1, 1])
        self.O.color = (125, 125, 223)

        self.I = Mino(self.initX, self.initY)
        self.I.block.append([0, 0])
        self.I.block.append([1, 0])
        self.I.block.append([2, 0])
        self.I.block.append([-1, 0])
        self.I.color = (125, 223, 223)

        self.T = Mino(self.initX, self.initY)
        self.T.block.append([0, 0])
        self.T.block.append([0, 1])
        self.T.block.append([1, 1])
        self.T.block.append([-1, 1])
        self.T.color = (223, 125, 223)

        self.L = Mino(self.initX, self.initY)
        self.L.block.append([1, 0])
        self.L.block.append([-1, 1])
        self.L.block.append([0, 1])
        self.L.block.append([1, 1])
        self.L.color = (125, 125, 123)

        self.J = Mino(self.initX, self.initY)
        self.J.block.append([-1, 0])
        self.J.block.append([-1, 1])
        self.J.block.append([0, 1])
        self.J.block.append([1, 1])
        self.J.color = (189, 125, 223)

        self.S = Mino(self.initX, self.initY)
        self.S.block.append([0, 0])
        self.S.block.append([1, 0])
        self.S.block.append([0, 1])
        self.S.block.append([-1, 1])
        self.S.color = (125, 189, 223)

        self.Z = Mino(self.initX, self.initY)
        self.Z.block.append([0, 0])
        self.Z.block.append([-1, 0])
        self.Z.block.append([0, 1])
        self.Z.block.append([1, 1])
        self.Z.color = (189, 125, 189)

    def getGroup(self):
        minos = []
        minos.append(self.O)
        minos.append(self.I)
        minos.append(self.T)
        minos.append(self.L)
        minos.append(self.J)
        minos.append(self.S)
        minos.append(self.Z)
        return minos


class TetrisMatrix(Matrix):

    def __init__(self):
        super().__init__()
        self._bm = BaseBox()
        self.minos = self._bm.getGroup()
        self.readyMino = None
        self.activeMino = None
        self.currentIndex = 0
        self.start()
        self.minX = 0
        self.minY = 0
        self.maxX = 9
        self.maxY = 19
        self.matrix = [[False] * 20 for _ in range(10)]
        self.allMinos = []

    def start(self):
        random.shuffle(self.minos)
        self.shuffleMino()

    # 再来一个新块
    def shuffleMino(self):
        self.activeMino = copy.deepcopy(self.minos[self.currentIndex])
        if self.currentIndex == len(self.minos) - 1:
            self.currentIndex = -1
            random.shuffle(self.minos)
        self.readyMino = copy.deepcopy(self.minos[self.currentIndex + 1])
        self.currentIndex += 1

    # 快速下降
    def down(self):
        if self.isColliding(x=0, y=1):
            self.archived()
            self.shuffleMino()
        else:
            self.activeMino.relativeY += 1
            self.upgrade()

    # 左移
    def left(self):
        if not self.isColliding(x=-1, y=0):
            self.activeMino.relativeX -= 1
            self.upgrade()

    # 右移
    def right(self):
        if not self.isColliding(x=1, y=0):
            self.activeMino.relativeX += 1
            self.upgrade()

    # 变换
    def up(self):
        if not self.isColliding(x=0, y=0, isRotate=True):
            self.activeMino.rotate()
            self.upgrade()

    # 方块落底了 归档
    def archived(self):
        self.allMinos.append(self.activeMino)
        for b in self.activeMino.block:
            fb = self.activeMino.getFinalyBlock(b)
            self.matrix[fb[0]][fb[1]] = True

    # 消行判断
    def upgrade(self):
        for row in range(len(self.matrix[0])):
            isGrade = True
            for i in range(len(self.matrix)):
                if not self.matrix[i][row]:
                    isGrade = False
            if isGrade:
                self.scores += 1
                tmpMinos = []
                # 消行
                for m in self.allMinos:
                    tmpList = []
                    for b in m.block:
                        if m.getFinalyBlock(b)[1] != row:
                            tmpList.append(b)
                    if len(tmpList) > 0:
                        m.block = tmpList
                        tmpMinos.append(m)
                self.allMinos = tmpMinos
                # 下移一行
                for m in self.allMinos:
                    for b in m.block:
                        if m.getFinalyBlock(b)[1] < row:
                            b[1] += 1
                self.matrix = [[False] * 20 for _ in range(10)]
                for m in self.allMinos:
                    for b in m.block:
                        fb = m.getFinalyBlock(b)
                        self.matrix[fb[0]][fb[1]] = True

    # 碰撞检测
    def isColliding(self, x=0, y=0, isRotate=False):
        for b in self.activeMino.block:
            fb = self.activeMino.getRotateFinalyBlock(b) if isRotate else self.activeMino.getFinalyBlock(b)

            if fb[0] + x < self.minX or fb[0] + x > self.maxX:
                return True
            if fb[1] + y < self.minY or fb[1] + y > self.maxY:
                return True
            if self.matrix[fb[0] + x][fb[1] + y]:
                return True
        return False
