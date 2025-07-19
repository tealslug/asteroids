import pygame
from constants import *
from player import Player

def game_loop(screen, player):
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return

        screen.fill(pygame.Color('black'))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

def main():
    print("Starting Asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    game_loop(screen, player)
    pygame.quit()


if __name__ == "__main__":
    main()
