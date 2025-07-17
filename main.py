import pygame
from constants import *

def game_loop(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return

        screen.fill(pygame.Color('black'))
        pygame.display.flip()

def main():
    print("Starting Asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen)
    pygame.quit()


if __name__ == "__main__":
    main()
