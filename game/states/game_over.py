import pygame


class GameOverState:
    """按下 R 回到選單，按下 Q 離開。"""

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "menu"
                if event.key == pygame.K_q:
                    return "quit"
        return None

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((40, 10, 10))
        font = pygame.font.SysFont(None, 64)
        title = font.render("Game Over", True, (220, 50, 50))
        hint = pygame.font.SysFont(None, 32).render("R: Restart   Q: Quit", True, (180, 180, 180))
        screen.blit(title, title.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 40)))
        screen.blit(hint, hint.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30)))
