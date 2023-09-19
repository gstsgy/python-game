import pygame

from common.BaseGame import BaseGame
from snake.Core import SnakeMatrix
class SnakeGame(BaseGame):
    LINE_COLOR = (104, 188, 103)  # 红色，使用RGB颜色
    LINE_WIDTH = 1
    MARGE_LEFT = 5
    MARGE_TOP = 0
    BOX_MAX_X = 30
    BOX_MAX_Y = 20
    BOX_LENGTH = 20

    def __init__(self):
        width = SnakeGame.MARGE_LEFT + SnakeGame.BOX_LENGTH * (SnakeGame.BOX_MAX_X + 1) + 10
        height = SnakeGame.MARGE_TOP + SnakeGame.BOX_LENGTH * (SnakeGame.BOX_MAX_Y + 1) + 200
        super().__init__(width, height, "贪吃蛇----guyue")
        self.myFont = None
        self.myEvent = None
        self.isStart = False
        self.matrix = SnakeMatrix(SnakeGame.BOX_MAX_X, SnakeGame.BOX_MAX_Y)

    def startBefore(self):
        pygame.font.init()
        print("获取系统中所有可用字体", pygame.font.get_fonts())
        self.myFont = pygame.font.Font('../resouces/ChillKai.ttf', 45)
        # 设置 自定义事件
        self.myEvent = pygame.USEREVENT + 1
        pygame.time.set_timer(self.myEvent, 500)  #
        pygame.time.Clock()

    def eventListeners(self, event):
        if event.type == self.myEvent and self.isStart:
            self.matrix.forward()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == 'w' or event.key == 1073741906 or event.unicode == '8':
                self.matrix.up()
            elif event.unicode == 's' or event.key == 1073741905 or event.unicode == '2':
                self.matrix.down()
            elif event.unicode == 'a' or event.key == 1073741904 or event.unicode == '4':
                self.matrix.left()
            elif event.unicode == 'd' or event.key == 1073741903 or event.unicode == '6':
                self.matrix.right()
            elif event.unicode == 'z' and self.matrix.end:
                self.matrix = SnakeMatrix(SnakeGame.BOX_MAX_X, SnakeGame.BOX_MAX_Y)
            elif event.key == pygame.K_SPACE:
                self.isStart = not self.isStart

    def rending(self):

        # 画横线
        for line in range(self.BOX_MAX_Y + 2):
            pygame.draw.line(self.screen, self.LINE_COLOR,
                             (self.MARGE_LEFT + 0, self.MARGE_TOP + line * self.BOX_LENGTH),
                             (self.MARGE_LEFT + (self.BOX_LENGTH * (self.BOX_MAX_X + 1)),
                              self.MARGE_TOP + line * self.BOX_LENGTH), self.LINE_WIDTH)

        # 画竖线
        for cloum in range(self.BOX_MAX_X + 2):
            pygame.draw.line(self.screen, self.LINE_COLOR,
                             (self.MARGE_LEFT + cloum * self.BOX_LENGTH, self.MARGE_TOP + 0),
                             (self.MARGE_LEFT + cloum * self.BOX_LENGTH,
                              self.MARGE_TOP + (self.BOX_LENGTH * (self.BOX_MAX_Y + 1))), self.LINE_WIDTH)

        # 画蛇
        curlNode = self.matrix.snake
        while curlNode:
            pygame.draw.rect(self.screen, curlNode.color,
                             [curlNode.x * self.BOX_LENGTH + self.MARGE_LEFT + 2,
                              curlNode.y * self.BOX_LENGTH + self.MARGE_TOP + 2, SnakeGame.BOX_LENGTH - 4,
                              SnakeGame.BOX_LENGTH - 4], 0)
            curlNode = curlNode.next

        # 画食物

        pygame.draw.rect(self.screen, [198, 198, 225],
                         [self.matrix.food[0] * self.BOX_LENGTH + self.MARGE_LEFT + 2,
                          self.matrix.food[1] * self.BOX_LENGTH + self.MARGE_TOP + 2, SnakeGame.BOX_LENGTH - 4,
                          SnakeGame.BOX_LENGTH - 4], 0)



    def rendingBefore(self):
        self.screen.fill([0xf3, 0xf4, 0xf5])
        relativeY = self.MARGE_TOP + (self.BOX_LENGTH * (self.BOX_MAX_Y + 2)) +30

        if self.matrix.end:

            # game over
            textSurfaceObj = self.myFont.render(f"GAME OVER， z键重新开始", True, [0, 0, 0], [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (SnakeGame.MARGE_LEFT+300, relativeY)
            self.screen.blit(textSurfaceObj, textRectObj)
        else:
            # 写分数
            textSurfaceObj = self.myFont.render(f"分数：{self.matrix.scores}", True, [0, 0, 0], [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (SnakeGame.MARGE_LEFT + 100, relativeY)
            self.screen.blit(textSurfaceObj, textRectObj)


        #空格暂停/开始
        textSurfaceObj = self.myFont.render(f"空格:{'开始'if not self.isStart else '暂停'}", True, [0, 0, 0], [214, 231, 200])
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (SnakeGame.MARGE_LEFT+100, relativeY+100)
        self.screen.blit(textSurfaceObj, textRectObj)


if __name__ == '__main__':
    game = SnakeGame()
    game.start()
