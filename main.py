import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def game_loop(screen, player, updatables, drawables):
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return

        screen.fill(pygame.Color('black'))

        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

def main():
    print("Starting Asteroids!")

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    game_loop(screen, player, updatables, drawables)
    pygame.quit()


if __name__ == "__main__":
    main()
