
class SnakeBody:   

    def __init__(self, x, y, x_direction, y_direction):
        self.x = x 
        self.y = y
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.snake_list = []
        self.snake_list.append((x,y))

    def set_xy_direction(self, x_direction, y_direction ):
        self.x_direction = x_direction
        self.y_direction = y_direction 