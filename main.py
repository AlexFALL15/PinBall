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
    def update(self, FPS, width, height):
        pos = FPS.tick(60) / 1000.0
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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 720
    screen = pygame.display.set_mode(size)

    running = True
    ball = Ball(250, 360, 'Ball.png', 150)
    FPSClock = pygame.time.Clock()
    while running:
        ball.render(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        ball.update(FPSClock, size[0], size[1])
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()
