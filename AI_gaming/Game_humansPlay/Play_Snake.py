import pygame
import sys
import Button
import object_of_snake

# 定義常量
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
WHITE = (255, 255, 255)

# 初始化 pygame
pygame.init()

# 建立遊戲視窗
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('貪吃蛇')

# 建立貪吃蛇和食物物件
snake = object_of_snake.Snake()
food = object_of_snake.Food()

# 繪製遊戲畫面
screen.fill((0, 0, 0))
snake.draw()
food.draw()

restart_button = Button.startButton(10, 10)
leave_button = Button.LeaveButton(10, 70)

# 遊戲迴圈
def gmae_loop():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    snake.direction = 'down'
                elif event.key == pygame.K_LEFT:
                    snake.direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    snake.direction = 'right'

        # 更新貪吃蛇位置
        snake.move()

        # 檢查是否吃到食物，如果是則在貪吃蛇尾部增加一個方塊，並重新生成食物
        if snake.body[0] == food.position:
            snake.body.append(snake.body[-1])
            food.position = food.generate_position()
            snake.score+=10
            
        # 檢查是否碰到邊界或自己的身體，如果是則結束遊戲
        x, y = snake.body[0]
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            game_over = True
        for block in snake.body[1:]:
            if snake.body[0] == block:
                game_over = True
        
        # 畫線
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))
        
        # 繪製遊戲畫面
        screen.fill((0, 0, 0))
        snake.draw()
        food.draw()
        
        # 更新分數
        font = pygame.font.SysFont("arial", 20)
        score_text = font.render("Score: " + str(snake.score), True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        
        # 控制遊戲速度
        pygame.time.Clock().tick(10+snake.score/10)
        
while True:
    pygame.display.update()
    
    restart_button.draw(screen)
    leave_button.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            if restart_button.is_clicked(pos):
                # Restart the game
                snake.reset()
                gmae_loop()
            
            elif leave_button.is_clicked(pos):
                # Exit the game
                pygame.quit()
                sys.exit()

