import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    P1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()
        #following loop looks for the exit press on pygame window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        #supposed to update player rotation and movement
        updatable.update(dt)
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
