class Bullet:

    def __init__(self):
        self.x = 0
        self.y = 0


class Plane:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.max_width = 95  # 最大宽度 95
        self.aerofoil_width = 35  # 机翼宽度
        self.max_height = 90  # 最大高度
        self.aerofoil_height = 15  # 机翼高度


class PlaneMatrix:

    def __init__(self, maxX, maxY):
        self.maxX = maxX
        self.maxY = maxY
        self.minX = 0
        self.minY = 0
        self.scores = 0
        self.end = False
        self.plane = Plane()
        self.__start()

    def __start(self):

        self.plane.x = 0
        self.plane.y = 0
        # self.maxY - 120

    def down(self):
        self.__move(y=2)

    def up(self):
        self.__move(y=-2)

    def left(self):
        self.__move(x=-2)

    def right(self):
        self.__move(x=2)

    # 飞机移动
    def __move(self, x=0, y=0):
        if self.plane.x + x < -self.plane.max_width / 2 or self.plane.y + y < 0:
            return
        if self.plane.x + self.plane.max_width / 2 + x > self.maxX or self.plane.y + self.plane.max_height + y > self.maxY:
            return
        self.plane.x += x
        self.plane.y += y
