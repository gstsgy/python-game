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
        super().__init__(PlaneGame.WIDTH, PlaneGame.HEIGHT, "飞机大战----guyue")
        self.myFont = None
        self.myEvent = None
        self.isStart = False
        self.matrix = PlaneMatrix(480, 700)

    def startBefore(self):
        pygame.key.set_repeat(10, 15)
        pygame.font.init()
        print("获取系统中所有可用字体", pygame.font.get_fonts())
        self.myFont = pygame.font.Font('../resouces/ChillKai.ttf', 16)
        # 设置 自定义事件
        self.bulletSpeed = pygame.USEREVENT + 1
        pygame.time.set_timer(self.bulletSpeed, 100)  #
        pygame.time.Clock()

        # 设置 自定义事件
        self.planeFall = pygame.USEREVENT + 2
        pygame.time.set_timer(self.planeFall, 1000)  #
        pygame.time.Clock()

    def eventListeners(self, event):
        if event.type == self.bulletSpeed and self.isStart:
            self.isStart = not self.matrix.end
            self.matrix.shoot()
        if event.type == self.planeFall and self.isStart:
            self.isStart = not self.matrix.end
            self.matrix.planeFall()
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
                self.matrix = PlaneMatrix(480, 700)
            elif event.key == pygame.K_SPACE:
                self.isStart = True

    def rending(self):
        bg_img = pygame.image.load(PlaneGame.PLANE_PATH).convert_alpha()  # 战机
        bullet_img = pygame.image.load(PlaneGame.BULLET_PATH).convert_alpha()
        enemy_img = pygame.image.load(PlaneGame.ENEMY_PATH).convert_alpha()
        self.screen.blit(bg_img, (self.matrix.plane.x, self.matrix.plane.y))  # 绘制战机
        for b in self.matrix.bullets:
            self.screen.blit(bullet_img, (b.x, b.y))  # 绘制子弹

        for e in self.matrix.enemys:
            self.screen.blit(enemy_img, (e.x, e.y))  # 绘制敌机

    def rendingBefore(self):
        self.screen.fill([0xf3, 0xf4, 0xf5])
        bg_img = pygame.image.load(PlaneGame.BD_PATH).convert()  # 背景图片
        self.screen.blit(bg_img, (0, 0))  # 绘制背景
        # 空格暂停/开始
        textSurfaceObj = self.myFont.render(f"按空格开始", True, [0, 0, 0])

        self.screen.blit(textSurfaceObj, (0, 700))

        # 分数
        textSurfaceObj = self.myFont.render(f"分数:{self.matrix.scores}", True, [0, 0, 0])
        self.screen.blit(textSurfaceObj, (0, 720))

        # 血量
        textSurfaceObj = self.myFont.render("生命：", True, [0, 0, 0])
        self.screen.blit(textSurfaceObj, (0, 740))
        if self.matrix.end:
            textSurfaceObj = self.myFont.render("您已阵亡，输入z重新开始", True, [0, 0, 0])
            self.screen.blit(textSurfaceObj, (0, 760))

        pygame.draw.rect(self.screen, [125, 125, 125], [45, 740, 400, 20], 0)
        hp = self.matrix.plane.hp / 20 * 400
        pygame.draw.rect(self.screen, [255, 121, 121], [45, 740, hp, 20], 0)


if __name__ == '__main__':
    game = PlaneGame()
    game.start()
