'''
Created on Feb 2, 2018

@author: jonathanlin
'''

import random

class Matrix:
    def __init__(self, size = 2):
        self.cords_high = []
        self.size = size
          
    def random_squares(self):
        for x in range(self.size):
            temp_cord = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            while temp_cord in self.cords_high:
                temp_cord = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            self.cords_high.append(temp_cord)
            

        
            