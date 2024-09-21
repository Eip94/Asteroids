import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    dt = 0
    ticker = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    while True:
        dt = ticker.tick(60)
        dt /= 1000
        pygame.Surface.fill(screen, (0,0,0))
        for object in drawable:
            object.draw(screen)
        for object in updatable:
            object.update(dt)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

if __name__ == "__main__":
    main()