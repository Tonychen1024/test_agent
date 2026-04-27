import pygame
import sys

from menu import Menu
from playing import Playing
from game_over import GameOver

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

STATE_MAP = {
    "menu": Menu,
    "playing": Playing,
    "game_over": GameOver,
}


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()

    current_state = Menu()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_state.handle_events(events)
        current_state.update()
        current_state.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

        if current_state.next_state == "quit":
            pygame.quit()
            sys.exit()
        elif current_state.next_state in STATE_MAP:
            current_state = STATE_MAP[current_state.next_state]()


if __name__ == "__main__":
    main()
