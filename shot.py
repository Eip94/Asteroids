from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
    velocity = pygame.Vector2(0,1)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)