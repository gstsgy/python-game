import pygame
from Core import Matrix, Direction

keep_going = True
LINE_COLOR = (255, 0, 0)  # 红色，使用RGB颜色
LINE_WIDTH = 3
LINE_HEIGHT = 100
MARGE_LEFT = 5
MARGE_TOP = 45

# 初始设置
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode(
    (LINE_HEIGHT * 4 + MARGE_LEFT + LINE_WIDTH, LINE_HEIGHT * 4 + MARGE_TOP + LINE_WIDTH))  # Pygame窗口

pygame.display.set_caption("2048游戏----guyue")  # 标题

pygame.font.init()
print("获取系统中所有可用字体", pygame.font.get_fonts())
my_font = pygame.font.SysFont(['notosanstelugu', 'microsoftsansserif'], 50)
matrix = Matrix()
# 游戏循环
while keep_going:
    screen.fill([214, 231, 200])
    textSurfaceObj = my_font.render(f"{matrix.scores}", True, [0, 0, 0], [214, 231, 200])
    # get_rect()方法返回rect对象
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (
        200, 25)
    screen.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():  # 遍历事件
        if event.type == pygame.QUIT:  # 退出事件
            keep_going = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == 'w' or event.key == 1073741906 or event.unicode == '8':
                matrix.transformation(Direction.UP)
            elif event.unicode == 's' or event.key == 1073741905 or event.unicode == '2':
                matrix.transformation(Direction.DOWN)
            elif event.unicode == 'a' or event.key == 1073741904 or event.unicode == '4':
                matrix.transformation(Direction.LEFT)
            elif event.unicode == 'd' or event.key == 1073741903 or event.unicode == '6':
                matrix.transformation(Direction.RIGHT)
            # print("#", event.key, event.mod)
            else:
                pass
                # matrix.create(matrix.numbers[0])
            # print(event.unicode, event.key)
            # print(matrix.numbers)
    # 画横线
    for line in range(5):
        pygame.draw.line(screen, LINE_COLOR, (MARGE_LEFT + 0, MARGE_TOP + line * LINE_HEIGHT),
                         (MARGE_LEFT + 400, MARGE_TOP + line * LINE_HEIGHT), LINE_WIDTH)

    # 画竖线
    for cloum in range(5):
        pygame.draw.line(screen, LINE_COLOR, (MARGE_LEFT + cloum * LINE_HEIGHT, MARGE_TOP + 0),
                         (MARGE_LEFT + cloum * LINE_HEIGHT, MARGE_TOP + 400), LINE_WIDTH)
    # 写字

    for (i, sub) in enumerate(matrix.numbers):
        for (j, n) in enumerate(sub):
            if n != 0:
                textSurfaceObj = my_font.render(str(n), True, [0, 0, 0], [214, 231, 200])
                # get_rect()方法返回rect对象
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (
                    MARGE_LEFT + j * LINE_HEIGHT + LINE_HEIGHT / 2, MARGE_TOP + i * LINE_HEIGHT + LINE_HEIGHT / 2)
                screen.blit(textSurfaceObj, textRectObj)
    pygame.display.update()  # 刷新屏幕

# 退出程序
pygame.quit()
