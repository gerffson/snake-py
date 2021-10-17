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
        self.snake_body = SnakeBody(300, 300, 0 , 0)
        self.screen_height = 800
        self.screen_width = 600
        self.block_size = 20
        self.game_speed = 10        
        self.food = self.random_food(self.screen_height, self.screen_width, self.block_size)        

    def start(self):

        pygame.init()        
        screen = pygame.display.set_mode((self.screen_height, self.screen_width))
        pygame.display.set_caption('Snake Game')
        background_image = pygame.image.load("grass2.jpg").convert()    
        background_image = pygame.transform.scale(background_image, (800, 600))    
        screen.blit(background_image, [0, 0])
        
        pygame.display.flip()
        clock = pygame.time.Clock() 

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake_body.set_xy_direction(-20, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake_body.set_xy_direction(20, 0)
                    elif event.key == pygame.K_UP:
                        self.snake_body.set_xy_direction(0, -20)
                    elif event.key == pygame.K_DOWN:
                        self.snake_body.set_xy_direction(0, 20)
        
            self.snake_body.x += self.snake_body.x_direction
            self.snake_body.y += self.snake_body.y_direction 
                      
            #print(self.snake_body.snake_list)                
            
            if (self.snake_body.x > self.screen_height) or (self.snake_body.x < 0) or (self.snake_body.y > self.screen_width) or (self.snake_body.y < 0):                                
                print("Game Over")
                self.game_over = True

            if (self.snake_body.x == self.food.x) and (self.snake_body.y == self.food.y) : 
                self.grow_snake() 
                self.game_speed += 1 
                self.food = self.random_food(self.screen_height, self.screen_width, self.block_size)                

            rect = background_image.get_rect()            
            screen.blit(background_image, rect)
            pygame.display.flip()

            self.update_snake()
            self.draw_snake(screen, self.block_size)
            self.draw_food(screen, self.food, self.block_size)

            #pygame.display.update()


            clock.tick(self.game_speed)

        pygame.quit()


    def grow_snake(self):        
        (tempx, tempy) = self.snake_body.snake_list[0]
        if self.snake_body.x_direction == 20:            
            tempx -= 20
        elif self.snake_body.x_direction == -20:
            tempx += 20
        elif self.snake_body.y_direction == 20:
            tempy -= 20
        elif self.snake_body.y_direction == -20:
            tempy += 20

        new_snake_list = []
        new_snake_list.append((tempx, tempy))
        for i in range(0, len(self.snake_body.snake_list) , 1): 
            new_snake_list.append(self.snake_body.snake_list[i])

        self.snake_body.snake_list = new_snake_list

  
    def update_snake(self):        
        if len(self.snake_body.snake_list) > 0 :
            del self.snake_body.snake_list[0]
        self.snake_body.snake_list.append((self.snake_body.x, self.snake_body.y))


    def draw_snake(self, screen, block_size):         
        for i in range(len(self.snake_body.snake_list), 0, -1):            
            (x,y) = self.snake_body.snake_list[i - 1]
            img_body = pygame.image.load("body.png")            
            screen.blit(img_body, (x, y))
            #pygame.display.flip()
            #pygame.draw.rect(screen, colors.BLACK, [x, y, block_size, block_size])
            #pygame.display.update() 
    

    def draw_food(self, screen, food, block_size): 
        img_pig = pygame.image.load("apple.png")            
        screen.blit(img_pig, (food.x, food.y))
        pygame.display.flip()
        #pygame.draw.rect(screen, colors.RED, [food.x, food.y, block_size, block_size])
        #pygame.display.update() 


    def random_food(self, height, width, block_size):
        random_x = math.floor(randint(0, height) / block_size) * block_size
        random_y = math.floor(randint(0, width) / block_size) * block_size   
        food = Food(random_x, random_y)
        #print(" FOOD : [X : " + str(food.x) + ", Y : " + str(food.y)+ "]" )     
        return food