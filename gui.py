'''
Created on Feb 3, 2018

@author: jonathanlin
'''
BOARDER_CONST = 1
MAX_RGB_VALUE = 250
RGB_INC = 6
BOARD_SIZE = 4

COLOR_ONE = 0
COLOR_TWO = 0
COLOR_THREE = 102

import tkinter
import random

class Game:
    def __init__(self):
        self.size = BOARD_SIZE
        self.color_one = COLOR_ONE
        self.color_two = COLOR_TWO
        self.color_three = COLOR_THREE
        self.wrong_clicks = 0
        self.select_squares = []
        
        self.root_window = tkinter.Tk()
        self.side_length = 500
        self.block = self.side_length/self.size
        
        self.root_window.wm_title("Memory Matrix")
        self.root_window.columnconfigure(0, weight = 0)
        self.root_window.rowconfigure(0, weight = 0)
        self.board = tkinter.Canvas(master = self.root_window, width = self.side_length, height = self.side_length, background = "white")
        self.root_window.bind("<Return>", self.quit)
        self.play_game()
        
    def play_game(self):
        self.randomize_squares()
        self.display_board()
        self.root_window.after(1000, self.start)
        
    def start(self):
        self.root_window.bind("<Button-1>", self.cord_clicked)
        self.hide_board()
        
    def randomize_squares(self):
        for x in range(self.size):
            temp_cord = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            while temp_cord in self.select_squares:
                temp_cord = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            self.select_squares.append(temp_cord)
            
    def cord_clicked(self, event):
        x,y = self.convert_location(event.x, event.y)        
        if (x,y) in self.select_squares:
            del self.select_squares[self.select_squares.index((x,y))]
            self.board.create_rectangle(x * self.block + BOARDER_CONST, y * self.block + BOARDER_CONST, (x + 1) * self.block - BOARDER_CONST, (y + 1) * self.block - BOARDER_CONST, fill = '#%02x%02x%02x' % (0, 255, 0), outline = "white")
        else:
            self.board.create_rectangle(x * self.block + BOARDER_CONST, y * self.block + BOARDER_CONST, (x + 1) * self.block - BOARDER_CONST, (y + 1) * self.block - BOARDER_CONST, fill = '#%02x%02x%02x' % (255,106,106), outline = "white")
            self.wrong_clicks += 1
            if(self.wrong_clicks == int(self.size/2)):
                self.root_window.unbind("<Button-1>")
                
    def convert_location(self, x, y):
        return(int(x/self.side_length * self.size), int(y/self.side_length * self.size))
    
    def display_board(self):
        self.board.grid(row = 0, column = 0, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        self.draw_grid()
        self.draw_selected()
        
    def draw_selected(self):
        for x,y in self.select_squares:
            self.board.create_rectangle(x * self.block + BOARDER_CONST, y * self.block + BOARDER_CONST, (x + 1) * self.block - BOARDER_CONST, (y + 1) * self.block - BOARDER_CONST, fill = '#%02x%02x%02x' % (self.color_one, self.color_two, self.color_three), outline = "white")
    
    def draw_grid(self):
        for col in range(1, self.size):
            self.board.create_line(col * self.block, 0, col * self.block, self.block * self.size)
        for row in range(1, self.size):
            self.board.create_line(0, row * self.block, self.block * self.size, row * self.block)
    
    def hide_board(self):
        if(self.color_one < MAX_RGB_VALUE):
            self.color_one += RGB_INC   
        else:
            self.color_one = MAX_RGB_VALUE        
        if(self.color_two < MAX_RGB_VALUE):
            self.color_two += RGB_INC 
        else:
            self.color_two = MAX_RGB_VALUE 
        if(self.color_three < MAX_RGB_VALUE):
            self.color_three += RGB_INC 
        else:
            self.color_three = MAX_RGB_VALUE 
        for x,y in self.select_squares:
            self.board.create_rectangle(x * self.block + BOARDER_CONST, y * self.block + BOARDER_CONST, (x + 1) * self.block - BOARDER_CONST, (y + 1) * self.block - BOARDER_CONST, fill = '#%02x%02x%02x' % (self.color_one, self.color_two, self.color_three), outline = "white")
        if(len(self.select_squares) != 0 or self.color_one < MAX_RGB_VALUE or self.color_two < MAX_RGB_VALUE or self.color_three < MAX_RGB_VALUE):
            self.root_window.after(1, self.hide_board)
        elif(len(self.select_squares) == 0):
            self.root_window.unbind("<Button-1>")
            self.reset()
    
    def reset(self):
        self.board.delete("all")
        self.size += 1
        self.color_one = COLOR_ONE
        self.color_two = COLOR_TWO
        self.color_three = COLOR_THREE
        self.wrong_clicks = 0
        self.block = self.side_length/self.size
        self.play_game()
    
    def quit(self, event):
        self.root_window.destroy()

    def run(self):
        self.root_window.mainloop()
        
            
        