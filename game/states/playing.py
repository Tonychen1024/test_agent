import pygame


class PlayingState:
    """按下 ESC 進入 Game Over。"""

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "game_over"
        return None

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((10, 20, 40))
        font = pygame.font.SysFont(None, 48)
        text = font.render("Playing... (ESC to end)", True, (100, 220, 100))
        screen.blit(text, text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)))
