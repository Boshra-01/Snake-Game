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


class build_Snake:
    def __init__(self,parent_screen ,length_snake):
        self.length_snake = length_snake
        self.parent_screen = parent_screen
        self.block = pygame.image.load("Media/flags.png").convert_alpha()
        self.block = pygame.transform.scale(self.block, (45, 45))
        self.x = [SIZE_OF_BLOCK]*length_snake #x/y= left top coordinate of a block or rectangular/round shape that we are using
        self.y = [SIZE_OF_BLOCK]*length_snake
        self.direction = 'down'

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
        self.snake = build_Snake(self.surface, 5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def game(self):
        self.snake.move()
        self.apple.draw()

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

