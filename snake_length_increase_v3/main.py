import random
import pygame
import time
from pygame.locals import *
SIZE_OF_BLOCK = 50

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("Media/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE_OF_BLOCK*3
        self.y = SIZE_OF_BLOCK*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def run_apple(self):
        self.x = random.randint(0,20)*SIZE_OF_BLOCK #screensize: 1000by500 & apple size=50,so,(1000/50=20),(500/50=10)
        self.y = random.randint(0,10)*SIZE_OF_BLOCK #horizontally 20, vertically 10


class build_Snake:
    def __init__(self,parent_screen ,length_snake):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("Media/flags.png").convert_alpha()
        self.block = pygame.transform.scale(self.block, (45, 45))
        self.length_snake = length_snake
        self.x = [SIZE_OF_BLOCK]*length_snake #x/y= left top coordinate of a block or rectangular/round shape that we are using
        self.y = [SIZE_OF_BLOCK]*length_snake
        self.direction = 'down'

    def big_fat_snake(self):
        self.length_snake += 1
        self.x.append(-1)
        self.y.append(-1)

    def up(self):
        self.direction = 'up'
    def down(self):
        self.direction = 'down'
    def left(self):
        self.direction = 'left'
    def right(self):
        self.direction = 'right'


    def draw(self):
        self.parent_screen.fill((255, 204, 255))

        for i in range(self.length_snake):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i])) # x/y are in arrays now
        pygame.display.flip()

    def move(self):
        #put other blocks to their previous blocks to take place and keep the snake moving
        for i in range (self.length_snake-1,0,-1):
            self.x[i] = self.x[i-1] #current x position will be previous x block's position
            self.y[i] = self.y[i-1]

        if self.direction == 'up':
            self.y[0] -= SIZE_OF_BLOCK
        if self.direction == 'down':
            self.y[0] += SIZE_OF_BLOCK
        if self.direction == 'left':
            self.x[0] -= SIZE_OF_BLOCK
        if self.direction == 'right':
            self.x[0] += SIZE_OF_BLOCK

        self.draw()


class run_Snake:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.snake = build_Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def eat(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE_OF_BLOCK:
            if y1 >= y2 and y1 <= y2 + SIZE_OF_BLOCK:
                return True
        return False

    def game(self):
        self.snake.move()
        self.apple.draw()
        self.scoreboard()
        pygame.display.flip()

        if self.eat(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.big_fat_snake()
            self.apple.run_apple()

    def scoreboard(self):
        font =pygame.font.SysFont("times new roman",20)
        score = font.render(f"You smashed it {self.snake.length_snake} times!", True, (205,30, 152)) #storing the score with render function for colors
        self.surface.blit(score,(800,10)) #blit function is always required for 'surface'


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.up()
                    if event.key == K_DOWN:
                        self.snake.down()
                    if event.key == K_LEFT:
                        self.snake.left()
                    if event.key == K_RIGHT:
                        self.snake.right()


                elif event.type == QUIT:
                    running = False

            self.game()
            time.sleep(0.3)

if __name__ == '__main__':
    run_snake = run_Snake()
    run_snake.run()

