# -*- coding: utf-8 -*-
# 记住上面这行是必须的，而且保存文件的编码要一致！
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((1280, 800), 0, 32)
 
#font = pygame.font.SysFont("仿宋_GB2312", 40)
#上句在Linux可行，在我的Windows 7 64bit上不行，XP不知道行不行
#font = pygame.font.SysFont("simsunnsimsun", 40)
#用get_fonts()查看后看到了这个字体名，在我的机器上可以正常显示了
font = pygame.font.Font("KosugiMaru-Regular.ttf", 40)
#这句话总是可以的，所以还是TTF文件保险啊
text_surface = font.render(u"こんにちは、俺はコの世界の王様だ！", True, (0, 0, 255))

WHITE = [255,255,255]
BLACK = [0,0,0]

def get_surf(font, text, color = WHITE):
    surf = font.render(text, True, color)
    rect = surf.get_rect()
    return surf, rect


class Button:
    def __init__(self, font, text, color = WHITE, back_color = BLACK):
        self.font = font
        self.text_surf, self.text_rect = get_surf(font, text, color)
        self.boarder = 5
        self.center = self.text_rect.center
        self.topleft = [self.text_rect.topleft[0] - self.boarder,
                        self.text_rect.topleft[1] - self.boarder]
        self.width = self.text_rect.width + 2 * self.boarder
        self.height = self.text_rect.height + 2 * self.boarder
        self.size = [self.width, self.height]
        self.rect = self.topleft + self.size
        self.move_on = False
        self.color = color
        self.back_color = back_color

    def set_center(self, pos):
        self.text_rect.center = pos
        self.topleft = [self.text_rect.topleft[0] - self.boarder,
                        self.text_rect.topleft[1] - self.boarder]
        self.rect = self.topleft + self.size

    def Collide(self, pos):
        return (pos[0] >= self.topleft[0] and
                pos[0] <= self.topleft[0] + self.width and
                pos[1] >= self.topleft[1] and
                pos[1] <= self.topleft[1] + self.height)

    def ProcessInput(self, events, pressed_keys):
        pos = pygame.mouse.get_pos()
        if self.Collide(pos):
            self.move_on = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('Button is clicked')
                    return True
        else:
            self.move_on = False
        return False

    def Update(self):
        pass

    def Render(self, screen):
        if self.move_on:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, self.back_color, self.text_rect) 
        else:
            pygame.draw.rect(screen, self.back_color, self.rect) 
        screen.blit(self.text_surf, self.text_rect)
 
x = 0
y = (800 - text_surface.get_height())/2
 
# background = pygame.image.load("1.1.jpg").convert()
 
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
 
    screen.fill(pygame.Color('yellow'))
    b = Button(font, u'はい')
    b.set_center([100, 100])
    b.Update()
    b.ProcessInput(events, None)
    b.Render(screen)
 
 
    screen.blit(text_surface, (0, 0))
 
    pygame.display.update()
