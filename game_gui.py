import tkinter
from matrix import Matrix

BOARDER_CONST = 1
MAX_RGB_VALUE = 250
RGB_INC = 6
BOARD_SIZE = 7

class Game:
    def __init__(self):
        self.size = BOARD_SIZE
        self.matrix = Matrix(self.size)
        self.matrix.random_squares()
        self.color_one = 0
        self.color_two = 0
        self.color_three = 102
        self.wrong_clicks = 0

        self.root_window = tkinter.Tk()
        
        self.side = 500
        self.block = 500/self.size

        self.root_window.wm_title("Memory Matrix")
        self.root_window.columnconfigure(0, weight = 0)
        self.root_window.rowconfigure(0, weight = 0)
        self.board = tkinter.Canvas(master = self.root_window, width = self.side, height = self.side, background = "white")
        self.root_window.bind("<Return>", self.quit)
        self.play_game()

    def play_game(self):
        self.display_board()
        self._draw_board()
        self.root_window.after(1000, self._start)
        
    def _start(self):
        self.root_window.bind("<Button-1>", self._cord_clicked)
        self._hide_board()

           
    def _reset(self):
        self.board.delete("all")
        self.size += 0.5
        self.matrix = Matrix(int(self.size))
        self.matrix.random_squares()
        self.color_one = 0
        self.color_two = 0
        self.color_three = 102
        self.wrong_clicks = 0
        self.block = 500/int(self.size)
        self.play_game()

    def display_board(self):
        self.board.grid(row = 0, column = 0, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        self._draw_grid()
        self._draw_board()

    def _draw_grid(self):
        for col in range(0, int(self.size) -1):
            self.board.create_line((col + 1) * self.block, 0, (col + 1) * self.block, self.block * self.size)
        for row in range(0, int(self.size) -1):
            self.board.create_line(0, (row + 1) * self.block, self.block * self.size, (row + 1) * self.block, fill = "Black")
        
    def _draw_board(self):
        for x,y in self.matrix.cords_high:
            self.board.create_rectangle(x * self.block + BOARDER_CONST, y * self.block + BOARDER_CONST, (x + 1) * self.block - BOARDER_CONST, (y + 1) * self.block - BOARDER_CONST, fill = '#%02x%02x%02x' % (self.color_one, self.color_two, self.color_three), outline = "white")
    
    def _hide_board(self):
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
        for x,y in self.matrix.cords_high:
            self.board.create_rectangle(x * self.block + BOARDER_CONST, y * self.block + BOARDER_CONST, (x + 1) * self.block - BOARDER_CONST, (y + 1) * self.block - BOARDER_CONST, fill = '#%02x%02x%02x' % (self.color_one, self.color_two, self.color_three), outline = "white")
        if(len(self.matrix.cords_high) != 0 or self.color_one < MAX_RGB_VALUE or self.color_two < MAX_RGB_VALUE or self.color_three < MAX_RGB_VALUE):
            self.root_window.after(1, self._hide_board)
        elif(len(self.matrix.cords_high) == 0):
            self.root_window.unbind("<Button-1>")
            self._reset()
    
    def _cord_clicked(self, event): 
        x,y = self._convert_location(event.x, event.y)  
        if((x,y) in self.matrix.cords_high):
            del self.matrix.cords_high[self.matrix.cords_high.index((x,y))]
            self.board.create_rectangle(x * self.block + BOARDER_CONST, y * self.block + BOARDER_CONST, (x + 1) * self.block - BOARDER_CONST, (y + 1) * self.block - BOARDER_CONST, fill = '#%02x%02x%02x' % (0, 255, 0), outline = "white")
        else:
            self.wrong_clicks += 1
            if(self.wrong_clicks == int(self.size/2)):
                self.root_window.unbind("<Button-1>")
            self.board.create_rectangle(x * self.block + BOARDER_CONST, y * self.block + BOARDER_CONST, (x + 1) * self.block - BOARDER_CONST, (y + 1) * self.block - BOARDER_CONST, fill = '#%02x%02x%02x' % (255,106,106), outline = "white")

    
    def _convert_location(self, x, y):
        return(int(x/self.side * int(self.size)), int(y/self.side * int(self.size)))
        
    def run(self):
        self.root_window.mainloop()
        
    def quit(self, event):
        self.root_window.destroy()
