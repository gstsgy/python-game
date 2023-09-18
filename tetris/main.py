import pygame

from common.BaseGame import BaseGame
from tetris.Core import TetrisMatrix


class TetrisGame(BaseGame):
    LINE_COLOR = (215, 125, 25)  # 红色，使用RGB颜色
    LINE_WIDTH = 3
    LINE_HEIGHT = 50
    MARGE_LEFT = 5
    MARGE_TOP = 0
    MAX_X = 9
    MAX_Y = 15
    def __init__(self):
        super().__init__(TetrisGame.LINE_HEIGHT * (TetrisGame.MAX_X+1) + TetrisGame.MARGE_LEFT + TetrisGame.LINE_WIDTH+200,
                         TetrisGame.LINE_HEIGHT * (TetrisGame.MAX_Y+1) + TetrisGame.MARGE_TOP + TetrisGame.LINE_WIDTH,
                         "俄罗斯方块----guyue")
        self.myFont = None
        self.myEvent = None
        self.matrix = TetrisMatrix(TetrisGame.MAX_X,TetrisGame.MAX_Y)
        self.isStart = False

    def startBefore(self):
        pygame.font.init()
        print("获取系统中所有可用字体", pygame.font.get_fonts())
        self.myFont = pygame.font.Font('../resouces/ChillKai.ttf', 45)
        # 设置 自定义事件
        self.myEvent = pygame.USEREVENT + 1
        pygame.time.set_timer(self.myEvent, 1000)  #
        clock = pygame.time.Clock()

    def eventListeners(self, event):
        if event.type == self.myEvent and self.isStart:
            self.matrix.down()
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
                self.matrix =  TetrisMatrix(TetrisGame.MAX_X,TetrisGame.MAX_Y)
            elif event.key == pygame.K_SPACE:
                self.isStart = not self.isStart

    def rending(self):

        # 画横线
        for line in range(self.matrix.maxY+2):
            pygame.draw.line(self.screen, self.LINE_COLOR, (self.MARGE_LEFT + 0, self.MARGE_TOP + line * self.LINE_HEIGHT),
                             (self.MARGE_LEFT + (self.LINE_HEIGHT*(self.MAX_X+1)), self.MARGE_TOP + line * self.LINE_HEIGHT), self.LINE_WIDTH)

        # 画竖线
        for cloum in range(self.matrix.maxX+2):
            pygame.draw.line(self.screen, self.LINE_COLOR, (self.MARGE_LEFT + cloum * self.LINE_HEIGHT, self.MARGE_TOP + 0),
                             (self.MARGE_LEFT + cloum * self.LINE_HEIGHT, self.MARGE_TOP + (self.LINE_HEIGHT*(self.MAX_Y+1))), self.LINE_WIDTH)

        # 画箱子
        for b in self.matrix.activeMino.block:
            pygame.draw.rect(self.screen, self.matrix.activeMino.color,
                             [self.matrix.activeMino.getFinalyBlock(b)[0] * self.LINE_HEIGHT + self.MARGE_LEFT + 5,
                              self.matrix.activeMino.getFinalyBlock(b)[1] * self.LINE_HEIGHT + self.MARGE_TOP + 5, 40, 40], 0)

        # 画所有箱子
        # 画箱子
        for m in self.matrix.allMinos:

            for b in m.block:
                pygame.draw.rect(self.screen, m.color,
                                 [m.getFinalyBlock(b)[0] * self.LINE_HEIGHT + self.MARGE_LEFT + 5,
                                  m.getFinalyBlock(b)[1] * self.LINE_HEIGHT + self.MARGE_TOP + 5, 40, 40], 0)

    def rendingBefore(self):
        self.screen.fill([214, 231, 200])
        relativeX = self.MARGE_LEFT + (self.LINE_HEIGHT * (self.MAX_X + 1)) + 100
        if self.matrix.isEnd():
            # 画分数面板
            # 写分数
            textSurfaceObj = self.myFont.render(f"分数：{self.matrix.scores}", True, [0, 0, 0], [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (relativeX, 25)
            self.screen.blit(textSurfaceObj, textRectObj)

            # 下一个方块
            textSurfaceObj = self.myFont.render(f"GAME OVER!", True, [0, 0, 0], [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (relativeX, 125)
            self.screen.blit(textSurfaceObj, textRectObj)

            textSurfaceObj = self.myFont.render(f"z键重开!", True, [0, 0, 0], [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (relativeX, 225)
            self.screen.blit(textSurfaceObj, textRectObj)
        else:
            # 画分数面板
            # 写分数
            textSurfaceObj = self.myFont.render(f"分数：{self.matrix.scores}", True, [0, 0, 0], [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (relativeX, 25)
            self.screen.blit(textSurfaceObj, textRectObj)

            # 下一个方块
            textSurfaceObj = self.myFont.render(f"下一个", True, [0, 0, 0], [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (relativeX, 125)
            self.screen.blit(textSurfaceObj, textRectObj)

            relativeY = 225
            # 画箱子
            for b in self.matrix.readyMino.block:
                pygame.draw.rect(self.screen, self.matrix.readyMino.color,
                                 [b[0] * 30 + 2 + relativeX-20,
                                  b[1] * 30 + 2 + relativeY, 25, 25], 0)

        # 空格暂停/开始
        textSurfaceObj = self.myFont.render(f"空格:{'开始'if not self.isStart else '暂停'}", True, [0, 0, 0], [214, 231, 200])
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (relativeX, 325)
        self.screen.blit(textSurfaceObj, textRectObj)

if __name__ == '__main__':
    game = TetrisGame()
    game.start()