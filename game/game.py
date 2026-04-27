import sys
import pygame

from game.states.menu import MenuState
from game.states.playing import PlayingState
from game.states.game_over import GameOverState

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.states = {
            "menu": MenuState(),
            "playing": PlayingState(),
            "game_over": GameOverState(),
        }
        self.current_state = "menu"

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            state = self.states[self.current_state]
            next_state = state.handle_events(events)
            if next_state == "quit":
                pygame.quit()
                sys.exit()
            elif next_state is not None:
                self.current_state = next_state

            state.update()
            state.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
