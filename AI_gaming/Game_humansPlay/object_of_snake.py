import pygame
import random

# 定義常量
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 定義貪吃蛇類別
class Snake:
    def __init__(self):
        self.body = [(240, 240), (220, 240), (200, 240)]
        self.direction = 'right'
        self.score =0
        
    def move(self):
        # 取得貪吃蛇頭部的座標
        x, y = self.body[0]
        
        # 根據移動方向更新座標
        if self.direction == 'up':
            y -= BLOCK_SIZE
        elif self.direction == 'down':
            y += BLOCK_SIZE
        elif self.direction == 'left':
            x -= BLOCK_SIZE
        elif self.direction == 'right':
            x += BLOCK_SIZE
    
        # 將新的頭部座標加入貪吃蛇身體的開始位置
        self.body.insert(0, (x, y))
        
        # 刪除身體最後一個方塊
        self.body.pop()
    
    def draw(self):
        # Draw checkerboard pattern on play field
        for i in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            for j in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
                rect = pygame.Rect(i, j, BLOCK_SIZE, BLOCK_SIZE)
                if (i // BLOCK_SIZE + j // BLOCK_SIZE) % 2 == 0:
                    pygame.draw.rect(screen, (50, 50, 50), rect)
                else:
                    pygame.draw.rect(screen, (75, 75, 75), rect)
        for block in self.body:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
    
    def reset(self):
        # Set initial state of the snake
        self.body = [(240, 240), (220, 240), (200, 240)]
        self.direction = 'right'
        self.score =0
    
# 定義食物類別
class Food:
    def __init__(self):
        self.position = self.generate_position()
    
    def generate_position(self):
        # 產生一個隨機座標
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        
        return (x, y)

    def draw(self):
        pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))
