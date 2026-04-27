import pygame


class GameOver:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 48)
        self.next_state = None

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.next_state = "menu"
                elif event.key == pygame.K_q:
                    self.next_state = "quit"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((50, 0, 0))
        text = self.font.render("Game Over - Press R to Restart / Q to Quit", True, (255, 255, 255))
        rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, rect)
