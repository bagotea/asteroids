import sys
import pygame
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    SPACE = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    P1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()
        #following loop looks for the exit press on pygame window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        #supposed to update entity rotation and movement
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(P1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
        #renders the screen
        screen.fill("black")
        #renders the player sprite
        for sprite in drawable:
            sprite.draw(screen)
        #refreshes the screen
        pygame.display.flip()
        #ensures the refresh rate is locked to 60 because we don't need a bajillion fps of Asteroids
        dt = Clock.tick(60.0) / 1000
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
