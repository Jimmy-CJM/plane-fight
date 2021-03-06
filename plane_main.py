import pygame
from plane_sprites import *
from settings import *


class PlaneGame(object):

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        bg3 = Background()
        bg4 = Background(True)

        bg3.rect.x = bg3.rect.width
        bg4.rect.x = bg4.rect.width
        self.bg_group = pygame.sprite.Group(bg1, bg2, bg3, bg4)

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] == 1:
            self.hero.speed = 2
        elif key_pressed[pygame.K_LEFT] == 1:
            self.hero.speed = -2
        # y轴的移动
        elif key_pressed[pygame.K_UP] == 1:
            self.hero.speed_y = -2
        elif key_pressed[pygame.K_DOWN] == 1:
            self.hero.speed_y = 2
        else:
            self.hero.speed = 0
            self.hero.speed_y = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullets, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if enemies:
            self.hero.kill()
            self.__game_over()

    def __update_sprites(self):
        self.bg_group.update()
        self.enemy_group.update()
        self.hero_group.update()
        self.hero.bullets.update()

        self.bg_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.hero_group.draw(self.screen)
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

    def start_game(self):
        while True:
            self.clock.tick(FRAME_PRE_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()

            pygame.display.update()




if __name__ == '__main__':

    game = PlaneGame()
    game.start_game()