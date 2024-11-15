import pygame
import circleshape
import random
from constants import ASTEROID_MIN_RADIUS


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, pygame.Color(255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split1 = Asteroid(
            self.position.x,
            self.position.y,
            new_radius
        )
        split1.velocity = vec1

        split2 = Asteroid(
            self.position.x,
            self.position.y,
            new_radius
        )
        split2.velocity = vec2
