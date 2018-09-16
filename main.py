import pygame
from plane_sprites import *


pygame.init()

screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
bg = pygame.image.load('./images/background.png')
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄图片
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (189, 574))
pygame.display.update()

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")

# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy)


# 设置游戏的时钟以及刷新频率
clock = pygame.time.Clock()
hero_rect = pygame.Rect(189, 574, 102, 124)


while True:
    clock.tick(60)
    # 监听用户事件
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()  # 卸载所有模块
            exit()  # 直接终止当前正在执行的程序

    # 飞机循环上移
    hero_rect.y -= 10
    # if hero_rect.y <= -hero_rect.height:
    #     hero_rect.y = 700
    if hero_rect.bottom <= 0:
        hero_rect.y = 700

    # 重新绘制背景
    screen.blit(bg, (0, 0))

    # 让精灵组调用两个方法

    enemy_group.update()
    enemy_group.draw(screen)


    screen.blit(hero, hero_rect)

    pygame.display.update()


pygame.quit()