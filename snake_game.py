import os
import pygame
import colors
from snake_body import SnakeBody
from food import Food
from random import randint
import math


clear = lambda: os.system('clear')

class SnakeGame:
 
    def __init__(self):
        self.game_over = False
        self.snake_body = SnakeBody(100, 100, 0 , 0)
        self.screen_height = 300
        self.screen_width = 200
        self.block_size = 10
        self.game_speed = 10        
        self.food = self.__random_food(self.screen_height, self.screen_width, self.block_size)

    def start(self):

        pygame.init()        
        screen = pygame.display.set_mode((self.screen_height, self.screen_width))
        pygame.display.set_caption('Snake Game')

        clock = pygame.time.Clock() 

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake_body.set_xy_direction(-10, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake_body.set_xy_direction(10, 0)
                    elif event.key == pygame.K_UP:
                        self.snake_body.set_xy_direction(0, -10)
                    elif event.key == pygame.K_DOWN:
                        self.snake_body.set_xy_direction(0, 10)
        
            self.snake_body.x += self.snake_body.x_direction
            self.snake_body.y += self.snake_body.y_direction 
                      
            print(self.snake_body.snake_list)                

            screen.fill(colors.WHITE)

            if (self.snake_body.x > self.screen_height) or (self.snake_body.x < 0) or (self.snake_body.y > self.screen_width) or (self.snake_body.y < 0):                                
                self.game_over = True

            if (self.snake_body.x == self.food.x) and (self.snake_body.y == self.food.y) : 
                self.__grow_snake() 
                self.food = self.__random_food(self.screen_height, self.screen_width, self.block_size)                


            self.__update_snake()
            self.__draw_snake(screen, self.block_size)
            self.__draw_food(screen, self.food, self.block_size)

            clock.tick(self.game_speed)

        pygame.quit()

    def __grow_snake(self):        
        (tempx, tempy) = self.snake_body.snake_list[0]
        if self.snake_body.x_direction == 10:
            print("self.snake_body.x_direction == 10")
            tempx -= 10
        elif self.snake_body.x_direction == -10:
            print("self.snake_body.x_direction == -10")
            tempx += 10
        elif self.snake_body.y_direction == 10:
            print("self.snake_body.y_direction == 10")
            tempy -= 10
        elif self.snake_body.y_direction == -10:
            print("self.snake_body.y_direction == -10")
            tempy += 10

        new_snake_list = []
        new_snake_list.append((tempx, tempy))
        for i in range(0, len(self.snake_body.snake_list) , 1): 
            new_snake_list.append(self.snake_body.snake_list[i])

        print("nova lista")
        print(new_snake_list)    

        self.snake_body.snake_list = new_snake_list

  
    def __update_snake(self):        
        if len(self.snake_body.snake_list) > 0 :
            del self.snake_body.snake_list[0]
        self.snake_body.snake_list.append((self.snake_body.x, self.snake_body.y))

    def __draw_snake(self, screen, block_size):         
        for i in range(len(self.snake_body.snake_list), 0, -1):            
            (x,y) = self.snake_body.snake_list[i - 1]
            pygame.draw.rect(screen, colors.BLACK, [x, y, block_size, block_size])
            pygame.display.update() 
    
    def __draw_food(self, screen, food, block_size):
        pygame.draw.rect(screen, colors.RED, [food.x, food.y, block_size, block_size])
        pygame.display.update() 

    def __random_food(self, height, width, block_size):
        random_x = math.floor(randint(0, height) / block_size) * block_size
        random_y = math.floor(randint(0, width) / block_size) * block_size   
        food = Food(random_x, random_y)
        print(" FOOD : [X : " + str(food.x) + ", Y : " + str(food.y)+ "]" )     
        return food