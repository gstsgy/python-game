# import pygame
# pygame.font.init()
# print("获取系统中所有可用字体",pygame.font.get_fonts())
# my_font = pygame.font.SysFont(['notosanstelugu','microsoftsansserif'],50)
# ---> 最下面的位置为第一个
# havingScore = 0
# tmp = [4, 2, 4, 0]
# zeroCounts = 0
# for n in tmp:
#     if n == 0:
#         zeroCounts += 1
#         tmp.remove(n)
#     if n != 0 and zeroCounts > 0:
#         havingScore = 1
# for _ in range(zeroCounts):
#     tmp.append(0)
# print(tmp)
# l = tmp
# for i in range(3):
#     if l[i] == l[i + 1] and l[i] != 0:
#         l[i] *= 2
#         l[i + 1] = 0
#         havingScore = 1
# zeroCounts = 0
# for n in l:
#     if n == 0:
#         zeroCounts += 1
#         l.remove(n)
# for _ in range(zeroCounts):
#     l.append(0)
# print(l)
# print(havingScore)
import pygame

# l = [2,3]
# z = [0,0]
# #l.extend(z)
# print(l[-1])
# l=[[False] * 20 for _ in range(10)]
# print(l)
pygame.font.init()
f = pygame.font.Font('/home/guyue/pro/python/game/resouces/ChillKai.ttf',16)
print("获取系统中所有可用字体", f)