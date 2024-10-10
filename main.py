import pygame
from constants import *
from player import *

def main():
    pygame.init()
    frames = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    # create a player object and spawn it at the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        # this is simply for 60 frames per second
        dt = frames.tick(60) / 1000
        

if __name__ == "__main__":
    main()