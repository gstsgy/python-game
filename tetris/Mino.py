class Mino:

    def __init__(self, initX, initY):
        self.block = []
        self.initX = initX
        self.initY = initY
        self.relativeX = 0
        self.relativeY = 0
        self.color = None
        # (x, y)绕(0, 0)顺时针转90度后坐标为(y, -x)

    def getFinalyBlock(self, b):
        return [b[0] + self.relativeX + self.initX, b[1] + self.relativeY + self.initY]

    def getRotateFinalyBlock(self, b):
        return [b[1] + self.relativeX + self.initX, -b[0] + self.relativeY + self.initY]

    def rotate(self):
        for b in self.block:
            [b[0], b[1]] = [b[1], -b[0]]
