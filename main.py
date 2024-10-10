import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    frames = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    # pygame groups for all the objects that can be updated and objects that can be drawn
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # create asteroid and field group and add it to groups
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # add the player class to the updatable and drawable groups
    Player.containers = (updatable, drawable)

    # create a player object and spawn it at the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        # iterate over all the objects in the groups
        for obj in updatable:
            obj.update(dt)

        # iterate over all the objects in the asteroid group to check for collisions
        # with the player and if there is a collision, end the game with a message
        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over!")
                return

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # this is simply for 60 frames per second
        dt = frames.tick(60) / 1000
        

if __name__ == "__main__":
    main()