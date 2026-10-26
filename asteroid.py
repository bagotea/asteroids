import random
from logger import log_event
from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "White", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle1 = random.uniform(20, 50)
        new_velo1 = self.velocity.rotate(new_angle1)
        new_velo2 = self.velocity.rotate(-new_angle1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_aster1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_aster1.velocity = new_velo1 * 1.2
        new_aster2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_aster2.velocity = new_velo2 * 1.2
