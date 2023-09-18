import copy
import random


class SnakeNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next: SnakeNode = None
        self.color = [random.randint(122, 255), 188, random.randint(45, 199)]

    def forward(self, directional):
        self.x += directional.x
        self.y += directional.y


class SnakeMatrix:
    def __init__(self, maxX, maxY):
        self.directional = SnakeNode(1, 0)
        self.scores = 0
        self.maxX = maxX
        self.maxY = maxY
        self.minX = 0
        self.minY = 0
        self.snake = SnakeNode(5, 5)
        self.food = []
        self.end = False
        self.start()

    def start(self):
        curlNode = self.snake
        for _ in range(3):
            curlNode.next = SnakeNode(curlNode.x - 1, curlNode.y)
            curlNode = curlNode.next
        self.__shuffleFood()

    def down(self):
        if self.__checkTurn([0, 1]):
            self.directional.x = 0
            self.directional.y = 1

    def up(self):
        if self.__checkTurn([0, -1]):
            self.directional.x = 0
            self.directional.y = -1

    def left(self):
        if self.__checkTurn([-1, 0]):
            self.directional.x = -1
            self.directional.y = 0

    def right(self):
        if self.__checkTurn([1, 0]):
            self.directional.x = 1
            self.directional.y = 0

    def forward(self):
        if self.end:
            return
        if self.__checkEnd():
            return
        self.__eat()
        tmp = copy.copy(self.snake)
        self.snake.forward(self.directional)
        curlNode = tmp
        while curlNode.next:
            tmp = copy.copy(curlNode.next)
            curlNode.next.x = curlNode.x
            curlNode.next.y = curlNode.y
            curlNode = tmp

    def __eat(self):
        if self.snake.x + self.directional.x == self.food[0] \
                and self.snake.y + self.directional.y == self.food[1]:
            self.scores += 1
            tmp = self.snake
            self.snake = SnakeNode(self.food[0], self.food[1])
            self.snake.next = tmp
            self.__shuffleFood()

    def __checkEnd(self):
        if self.snake.x + self.directional.x < self.minX \
                or self.snake.y + self.directional.y < self.minY:
            self.end = True
        if self.snake.x + self.directional.x > self.maxX \
                or self.snake.y + self.directional.y > self.maxY:
            self.end = True
        tmp = self.snake
        curlNode = self.snake.next
        while curlNode:
            if curlNode.x == tmp.x and curlNode.y == tmp.y:
                self.end = True
                break
            curlNode = curlNode.next
        return self.end

    def __shuffleFood(self):
        x = random.randint(0, self.maxX)
        y = random.randint(0, self.maxY)

        while True:
            same = False
            curlNode = self.snake
            while curlNode:
                if curlNode.x == x and curlNode.y == y:
                    same = True
                    break
                curlNode = curlNode.next
            if not same:
                break

            x = random.randint(0, self.maxX)
            y = random.randint(0, self.maxY)
        self.food = [x, y]

    def __checkTurn(self, d):
        tmp = self.snake.next
        return tmp.x != self.snake.x + d[0] or tmp.y != self.snake.y + d[1]
