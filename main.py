import pygame
import random

#WINDOW
WIDTH,HEIGTH = 400,400
WIN = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("Py SNAKE!")


END_GAME_EVENT = pygame.USEREVENT + 1
SNAKE_EATE_BERRY = pygame.USEREVENT + 2
SNAKE_EATE_HIMSELF = pygame.USEREVENT + 3

GREEN = (0, 150, 75)
BLUE = (0, 0, 200)
RED = (255, 0, 0)

FPS = 4

MAX_LENGTH_SNAKE = 1

def game():
    pygame.init()
    #snake = pygame.Rect(WIDTH // 2, HEIGTH // 2, 10, 10)
    snake = [pygame.Rect(WIDTH // 2, HEIGTH // 2, 10, 10),pygame.Rect(WIDTH // 2 - 10, HEIGTH // 2, 10, 10),pygame.Rect(WIDTH // 2 - 20, HEIGTH // 2, 10, 10)]
    berry = pygame.Rect(random.randint(0, WIDTH // 10 - 1) * 10, random.randint(0, HEIGTH // 10 - 1) * 10, 10, 10)
    run = True
    zivot = True
    smer_x = 0
    smer_y = 0
    clock = pygame.time.Clock()
    while run:
        if zivot:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                    run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:  #Nahoru
                    smer_x = 0
                    smer_y = -10
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:  #Dolu
                    smer_x = 0
                    smer_y = 10
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:  #Doleva
                    smer_x = -10
                    smer_y = 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:  #Doprava
                    smer_x = 10
                    smer_y = 0
            print(f"Smer:{smer_x},{smer_y}")
            last_part_of_snake = return_last_part_of_snake(snake)
            snake_movement_hanle(smer_x, smer_y, snake)
            snake_eate_berry(snake, berry)
            snake_eate_himeself(snake)
            for event in pygame.event.get():
                if event.type == END_GAME_EVENT:
                    zivot = False
                elif event.type == SNAKE_EATE_HIMSELF:
                    zivot = False
                elif event.type == SNAKE_EATE_BERRY:
                    spawn_berry(berry)
                    print("Snake eate berry")
                    snake.append(pygame.Rect(last_part_of_snake))
            print(f"Delka hada: {len(snake)}")
            draw(snake, berry)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                    run = False
    pygame.quit()

def draw(snake, berry):
    WIN.fill(GREEN)
    for partOfBody in snake:
        pygame.draw.rect(WIN, BLUE, partOfBody)
    pygame.draw.rect(WIN, RED, berry)
    pygame.display.update()

def snake_movement_hanle(smer_x, smer_y, snake):
    if smer_x != 0:
        if smer_x == 10:
            if snake[0].x + smer_x >= WIDTH:
                pygame.event.post(pygame.event.Event(END_GAME_EVENT))
            else:
                #snake[0].x += smer_x
                copy_of_snake = snake[:-1]
                copy_of_snake.insert(0,snake[0].x + smer_x)
                snake = copy_of_snake[:]
        elif smer_x == -10:
            if snake[0].x + smer_x < 0:
                pygame.event.post(pygame.event.Event(END_GAME_EVENT))
            else:
                #snake[0].x += smer_x
                copy_of_snake = snake[:-1]
                copy_of_snake.insert(0, snake[0].x + smer_x)
                snake = copy_of_snake[:]
    elif smer_y != 0:
        if smer_y == 10:
            if snake[0].y + smer_y >= HEIGTH:
                pygame.event.post(pygame.event.Event(END_GAME_EVENT))
            else:
                #snake[0].y += smer_y
                copy_of_snake = snake[:-1]
                copy_of_snake.insert(0, snake[0].y + smer_y)
                snake = copy_of_snake[:]
        elif smer_y == -10:
            if snake[0].y + smer_y < 0:
                pygame.event.post(pygame.event.Event(END_GAME_EVENT))
            else:
                #snake[0].y += smer_y
                copy_of_snake = snake[:-1]
                copy_of_snake.insert(0, snake[0].y + smer_y)
                snake = copy_of_snake[:]

def spawn_berry(berry):
    berry.x = (random.randint(0, 39) * 10)
    berry.y = (random.randint(0, 39) * 10)

def snake_eate_berry(snake, berry):
    if snake[0].colliderect(berry):
        pygame.event.post(pygame.event.Event(SNAKE_EATE_BERRY))

def snake_eate_himeself(snake):
    for partOfSnake in snake:
        if snake[0].colliderect(partOfSnake) and not snake[0] == partOfSnake:
            pygame.event.post(pygame.event.Event(SNAKE_EATE_HIMSELF))

def return_last_part_of_snake(snake):
    length = len(snake) - 1
    return snake[length]

if __name__ == '__main__':
    game()