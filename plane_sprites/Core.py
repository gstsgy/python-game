import random


class Bullet:

    def __init__(self, x, y, speed=4):
        self.x = x
        self.y = y
        self.speed = speed
        self.length = 6


class Plane:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.max_width = 95  # 最大宽度 95
        self.aerofoil_width = 35  # 机翼宽度
        self.max_height = 90  # 最大高度
        self.aerofoil_height = 15  # 机翼高度
        self.hp = 20  # 血量默认 20

    def shoot(self):
        # 射击出一颗子弹
        return Bullet(self.x + self.max_width / 2 + 3, self.y - 10)


class PlaneMatrix:

    def __init__(self, maxX, maxY):
        self.maxX = maxX
        self.maxY = maxY
        self.minX = 0
        self.minY = 0
        self.scores = 0
        self.end = False
        self.plane = Plane()
        self.enemys = []
        self.bullets = []
        self.__start()

    def __start(self):

        self.plane.x = 100
        self.plane.y = self.maxY - self.plane.max_height
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
        if self.plane.x + x < -self.plane.max_width / 2 - 5 or self.plane.y + y < 0:
            return
        if self.plane.x + self.plane.max_width / 2 + x > self.maxX or self.plane.y + self.plane.max_height + y > self.maxY:
            return
        self.plane.x += x
        self.plane.y += y

    def shoot(self):
        # 子弹射击
        tmp = []
        for b in self.bullets:
            b.y -= b.speed * b.length
            if b.y > 0:
                tmp.append(b)
        self.bullets = tmp
        self.bullets.append(self.plane.shoot())
        # 击毁判断
        self.__wrecked()

    def planeFall(self):

        # 敌机 降落
        tmp = []
        for e in self.enemys:
            e.y += 10
            if e.y < self.maxY:
                tmp.append(e)
        self.enemys = tmp
        posiX = random.randint(25, self.maxY - 30)
        enemy = Plane()
        enemy.x = posiX
        enemy.y = 0
        enemy.hp = 5
        enemy.max_height = 30
        enemy.max_width = 45
        self.enemys.append(enemy)
        tmp = []
        for e in self.enemys:
            if abs(self.plane.x - (e.x + 25)) < self.plane.max_width / 2 + e.max_width / 2 and abs(
                    self.plane.y - e.y) < self.plane.max_height / 2 + e.max_height / 2:
                self.plane.hp -= e.hp
            else:
                tmp.append(e)
        self.enemys = tmp
        if self.plane.hp<=0:
            self.end = True

    def __wrecked(self):
        tmpBullets = []

        for b in self.bullets:
            tmpEnemys = []
            isHit = False
            for e in self.enemys:
                # 判断子弹有没有打到敌机

                if abs(b.x - (e.x + 25)) < 2 / 2 + e.max_width / 2 and abs(b.y - e.y) < 6 / 2 + e.max_height / 2:
                    e.hp -= 1
                    self.scores += 1
                    isHit = True
                if e.hp > 0:
                    tmpEnemys.append(e)
            if not isHit:
                tmpBullets.append(b)
            self.enemys = tmpEnemys
        self.bullets = tmpBullets
