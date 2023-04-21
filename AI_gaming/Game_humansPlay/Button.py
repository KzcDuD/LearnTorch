import pygame

SNAKE_COLOR = (0, 255, 0)
WHITE = (255, 255, 255)

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, SNAKE_COLOR)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class startButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y, 100, 50, "Start")

class LeaveButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y, 100, 50, "Leave")

