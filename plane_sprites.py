import random
from settings import *


class GameSprite(pygame.sprite.Sprite):
    """飞机大战初始方法"""
    def __init__(self, image_name, speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        super().__init__("./images/enemy1.png", random.randint(1, 10))
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("敌机挂了 %d" % self.rect.y)
        pass


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        super().__init__("./images/me1.png")
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.speed = 0
        self.speed_y = 0
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y

        # 限制飞机在屏幕内部移动
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.x = SCREEN_RECT.right
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        for i in range(3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y -20*i
            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被销毁了")
        pass
