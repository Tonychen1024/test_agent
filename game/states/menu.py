import pygame


class MenuState:
    """按下 Enter 進入遊戲。"""

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return "playing"
        return None

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((30, 30, 30))
        font = pygame.font.SysFont(None, 64)
        title = font.render("My Game", True, (255, 255, 255))
        hint = pygame.font.SysFont(None, 32).render("Press ENTER to start", True, (180, 180, 180))
        screen.blit(title, title.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 40)))
        screen.blit(hint, hint.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30)))
