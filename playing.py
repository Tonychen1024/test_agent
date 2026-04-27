import pygame


class Playing:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 48)
        self.next_state = None

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.next_state = "game_over"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 50, 0))
        text = self.font.render("Playing... Press ESC to end", True, (255, 255, 255))
        rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, rect)
