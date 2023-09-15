import pygame

from common.BaseGame import BaseGame


class menuGame(BaseGame):
    width = 600
    height = 400
    title = "古月小游戏"

    def __init__(self):
        super().__init__(self.width, self.height, self.title)

    def eventListeners(self, event):
        if event.type == pygame.KEYDOWN:
            print(event.unicode,event.key)

if __name__ == '__main__':
    game = menuGame()
    game.start()
