import pygame

# 初始化设置
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("加载图片")
keep_going = True
pic = pygame.image.load("head.png") # 图片加载

# 游戏循环
while keep_going:
    for event in pygame.event.get(): # 循环遍历事件
        if event.type == pygame.QUIT:
            keep_going = False

    screen.blit(pic,(100,100)) # 在Surface上绘制图片
    pygame.display.update()
# 游戏退出
pygame.quit()