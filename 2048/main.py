import pygame
import common.BaseGame as BaseGame
from Core import Matrix, Direction


class Game2048(BaseGame.BaseGame):
    # 定义常量
    LINE_COLOR = (123, 123, 123)  # 线段颜色
    LINE_WIDTH = 3  # 线段宽度
    LINE_HEIGHT = 100  # 线段间距
    MARGE_LEFT = 5  # 距离屏幕左边位置
    MARGE_TOP = 45  # 距离屏幕上方位置
    TITLE = "2048游戏----guyue"  # 标题

    def __init__(self):
        super().__init__(Game2048.LINE_HEIGHT * 4 + Game2048.MARGE_LEFT + Game2048.LINE_WIDTH,
                         Game2048.LINE_HEIGHT * 4 + Game2048.MARGE_TOP + Game2048.LINE_WIDTH,
                         title=Game2048.TITLE)
        self.myFont = None
        self.fontInit()
        self.matrix = Matrix()
        self.isEnd = False

    # 初始化字体
    def fontInit(self):
        pygame.font.init()
        # print("获取系统中所有可用字体", pygame.font.get_fonts())
        self.myFont = pygame.font.Font('../resouces/ChillKai.ttf', 45)

    def eventListenBefore(self):
        self.screen.fill([214, 231, 200])
        if self.matrix.isEnd():
            self.isEnd = True

    def eventListeners(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'z' and self.isEnd:
                self.isEnd = False
                self.matrix = Matrix()
            if event.unicode == 'w' or event.key == 1073741906 or event.unicode == '8':
                self.matrix.transformation(Direction.UP)
            elif event.unicode == 's' or event.key == 1073741905 or event.unicode == '2':
                self.matrix.transformation(Direction.DOWN)
            elif event.unicode == 'a' or event.key == 1073741904 or event.unicode == '4':
                self.matrix.transformation(Direction.LEFT)
            elif event.unicode == 'd' or event.key == 1073741903 or event.unicode == '6':
                self.matrix.transformation(Direction.RIGHT)

    def rending(self):
        if self.isEnd:
            # 写分数
            textSurfaceObj = self.myFont.render(f"小伙子厉害呀，", True, [0, 0, 0], [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (200, 25)
            self.screen.blit(textSurfaceObj, textRectObj)

            textSurfaceObj = self.myFont.render(f"得了{self.matrix.scores}分", True, [0, 0, 0],
                                                [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (200, 125)
            self.screen.blit(textSurfaceObj, textRectObj)

            textSurfaceObj = self.myFont.render(f"再接再厉吧", True, [0, 0, 0],
                                                [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (200, 225)
            self.screen.blit(textSurfaceObj, textRectObj)

            textSurfaceObj = self.myFont.render(f"输入z键重新开始!", True, [0, 0, 0],
                                                [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (200, 325)
            self.screen.blit(textSurfaceObj, textRectObj)
        else:
            # 写分数
            textSurfaceObj = self.myFont.render(f"分数：{self.matrix.scores}", True, [0, 0, 0], [214, 231, 200])
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (200, 25)
            self.screen.blit(textSurfaceObj, textRectObj)
            # 画横线
            for line in range(5):
                pygame.draw.line(self.screen, self.LINE_COLOR,
                                 (self.MARGE_LEFT + 0, self.MARGE_TOP + line * self.LINE_HEIGHT),
                                 (self.MARGE_LEFT + 400, self.MARGE_TOP + line * self.LINE_HEIGHT), self.LINE_WIDTH)

            # 画竖线
            for cloum in range(5):
                pygame.draw.line(self.screen, self.LINE_COLOR,
                                 (self.MARGE_LEFT + cloum * self.LINE_HEIGHT, self.MARGE_TOP + 0),
                                 (self.MARGE_LEFT + cloum * self.LINE_HEIGHT, self.MARGE_TOP + 400), self.LINE_WIDTH)
            # 写字

            for (i, sub) in enumerate(self.matrix.numbers):
                for (j, n) in enumerate(sub):
                    if n != 0:
                        textSurfaceObj = self.myFont.render(str(n), True, [0, 0, 0], [214, 231, 200])
                        # get_rect()方法返回rect对象
                        textRectObj = textSurfaceObj.get_rect()
                        textRectObj.center = (
                            self.MARGE_LEFT + j * self.LINE_HEIGHT + self.LINE_HEIGHT / 2,
                            self.MARGE_TOP + i * self.LINE_HEIGHT + self.LINE_HEIGHT / 2)
                        self.screen.blit(textSurfaceObj, textRectObj)


if __name__ == '__main__':
    game = Game2048()
    game.start()
