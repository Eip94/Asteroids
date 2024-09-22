import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    dt = 0
    ticker = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    score = 0

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)

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
        for asteroid in asteroids:
            if player.Check_Collision(asteroid):
                print("Game over!")
                print(f"Your final score was {score}!")
                return
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.Check_Collision(asteroid):
                    asteroid.split()
                    bullet.kill()
                    score += 10

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()