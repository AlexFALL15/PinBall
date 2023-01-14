import sys
import os

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Ball:

    def __init__(self, First_X, First_Y, file_name, speed):
        self.x = First_X
        self.y = First_Y
        self.image = load_image(file_name)
        self.vx = speed
        self.vy = speed

    # обновление координат
    def update(self, clock, width, height):
        pos = clock.tick(60) / 1000.0
        self.x += self.vx * pos
        self.y += self.vy * pos
        if self.x > width - self.image.get_width():
            self.vx = -self.vx
            self.x = width - self.image.get_width()
        elif self.x < 0:
            self.vx = -self.vx
            self.x = 0
        if self.y > height - self.image.get_width():
            self.vy = -self.vy
            self.y = height - self.image.get_width()
        elif self.y < 0:
            self.vy = -self.vy
            self.y = 0
    
    # прорисовка на холсте surface
    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Baffle:
    def __init__(self, x, y, file_name, speed):
        self.x = x
        self.y = y
        self.image = load_image(file_name)
        self.vx = speed

    def update(self, clock, width, goingLeft, goingRight):
        if goingLeft:
            self.x -= 10
            goingLeft = False
        elif goingRight:
            self.x += 10
            goingRight = False
        if self.x < 0:
            self.x = 0
        if self.x + self.image.get_width() > width:
            self.x = width - self.image.get_width()

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


def collide():
    pass


def main():
    pygame.init()
    size = width, height = 500, 720
    screen = pygame.display.set_mode(size)

    running = True
    ball = Ball(250, 360, 'Ball.png', 150)
    baffle = Baffle(250, 650, 'Baffle.png', 100)
    fpsclock = pygame.time.Clock()
    going_left, going_right = False, False
    while running:
        ball.render(screen)
        baffle.render(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    going_left = True
                elif event.key == pygame.K_RIGHT:
                    going_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    going_left = False
                elif event.key == pygame.K_RIGHT:
                    going_right = False
        baffle.update(fpsclock, width, going_left, going_right)
        ball.update(fpsclock, size[0], size[1])
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()


if __name__ == '__main__':
    main()