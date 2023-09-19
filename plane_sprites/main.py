import pygame

from common.BaseGame import BaseGame
from plane_sprites.Core import PlaneMatrix


class PlaneGame(BaseGame):
    LINE_COLOR = (104, 188, 103)  # 红色，使用RGB颜色
    LINE_WIDTH = 1
    WIDTH = 480
    HEIGHT = 800

    PLANE_PATH = './img/zz.png'
    ENEMY_PATH = './img/dd.png'
    BULLET_PATH = './img/zd.png'
    BD_PATH = './img/planbg.png'
    def __init__(self):
        super().__init__(PlaneGame.WIDTH, PlaneGame.HEIGHT, "贪吃蛇----guyue")
        self.myFont = None
        self.myEvent = None
        self.isStart = False
        self.matrix = PlaneMatrix(480,700)

    def startBefore(self):
        pygame.key.set_repeat(10, 15)
        pygame.font.init()
        print("获取系统中所有可用字体", pygame.font.get_fonts())
        self.myFont = pygame.font.Font('../resouces/ChillKai.ttf', 45)
        # 设置 自定义事件
        self.myEvent = pygame.USEREVENT + 1
        pygame.time.set_timer(self.myEvent, 500)  #
        pygame.time.Clock()

    def eventListeners(self, event):
        pass
        if event.type == self.myEvent and self.isStart:
            pass
            #self.matrix.forward()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == 'w' or event.key == 1073741906 or event.unicode == '8':
                self.matrix.up()
            elif event.unicode == 's' or event.key == 1073741905 or event.unicode == '2':
                self.matrix.down()
            elif event.unicode == 'a' or event.key == 1073741904 or event.unicode == '4':
                self.matrix.left()
            elif event.unicode == 'd' or event.key == 1073741903 or event.unicode == '6':
                self.matrix.right()
            # elif event.unicode == 'z' and self.matrix.end:
            #     self.matrix = SnakeMatrix(SnakeGame.BOX_MAX_X, SnakeGame.BOX_MAX_Y)
            elif event.key == pygame.K_SPACE:
                self.isStart = not self.isStart

    def rending(self):
        bg_img = pygame.image.load(PlaneGame.PLANE_PATH).convert_alpha()  # 战机

        self.screen.blit(bg_img, (self.matrix.plane.x, self.matrix.plane.y))  # 绘制战机


    def rendingBefore(self):
        self.screen.fill([0xf3, 0xf4, 0xf5])
        bg_img = pygame.image.load(PlaneGame.BD_PATH).convert()  # 背景图片
        self.screen.blit(bg_img, (0, 0))  # 绘制背景


if __name__ == '__main__':
    game = PlaneGame()
    game.start()
