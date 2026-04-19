import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state
from shot import Shot

def game_loop(screen, player, updatables, drawables, asteroids, shots):
    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return

        screen.fill(pygame.Color('black'))

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.hasCollidedWith(player):
                print("Game over!")
                return
            for shot in shots:
                if shot.hasCollidedWith(asteroid):
                    shot.kill()
                    asteroid.split()
                    continue

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT) 

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    game_loop(screen, player, updatables, drawables, asteroids, shots)
    pygame.quit()


if __name__ == "__main__":
    main()
