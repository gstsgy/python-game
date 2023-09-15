# 游戏基类
import pygame


class BaseGame:
    keep_going = True

    def __init__(self, width, height, title):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))  # Pygame窗口
        pygame.display.set_caption(title)

    # 开始前要执行的
    def startBefore(self):
        pass

    # 画面渲染
    def rending(self):
        pass

    # 画面渲染前执行
    def rendingBefore(self):
        pass

    # 事件监听
    def eventListeners(self, event):
        pass

    # 事件监听前执行
    def eventListenBefore(self):
        pass

    # 开始 执行顺序 事件监听前-->事件监听--->渲染前执行--->渲染
    def start(self):
        self.startBefore()

        while BaseGame.keep_going:
            self.eventListenBefore()
            for event in pygame.event.get():  # 遍历事件
                if event.type == pygame.QUIT:  # 退出事件
                    BaseGame.keep_going = False
                self.eventListeners(event)
            self.rendingBefore()
            self.rending()
            pygame.display.update()  # 刷新屏幕
        # 退出程序
        pygame.quit()