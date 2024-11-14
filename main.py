import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0, 0, 0))
        for s in updatable:
            s.update(dt)
        for s in drawable:
            s.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
