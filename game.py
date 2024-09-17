from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from movement import *
import movement
from image_initialize import Images
import time



class Game:
  
  def __init__(self):
    #Drag and drop variables
    self.posx = 0
    self.posy = 0
    self.holding = 0
    self.turn = 0

    #Diagnostic Variables
    self.count = 0
    self.elapsed = 0
    self.elapsed2 = 0    

    #Sets up the root 
    self.root = Tk()
    self.root.title("Chess")

    #Initializes the board tile images
    self.images = Images()
    #Initializes an 8 by 8 array for the background images
    self.arr = [[0 for i in range(8)] for j in range(8)]
    self.pngarr = [[0 for i in range(8)] for j in range(8)]
    #Initializes an 8 by 8 array for the pieces
    self.pieces = [[0 for i in range(8)] for j in range(8)]
    #initializes an array of twelve 64-bit numbers for the 12 bitboards
    self.bitboard = [Grid(movement.OPP_ROOK),Grid(movement.OPP_KNHT),Grid(movement.OPP_BSHP),Grid(movement.OPP_QUEN),
      Grid(movement.OPP_KING),Grid(movement.OPP_PAWN),Grid(movement.YOU_ROOK),Grid(movement.YOU_KNHT),
      Grid(movement.YOU_BSHP),Grid(movement.YOU_QUEN),Grid(movement.YOU_KING),Grid(movement.YOU_PAWN)]
    self.joinboard = [Grid(movement.OPP_BORD),Grid(movement.YOU_BORD)]

    #Creates the board frame
    mainframe = ttk.Frame(self.root,padding=(0,0,0,0))
    mainframe.grid(column=0, row=0,sticky=(N, W, E, S))
    #Sets up interactions with every square on the board
    for x in range(8):
      for y in range(8):
        self.arr[x][y] = ttk.Label(mainframe, text="Tile")
        self.arr[x][y].grid(row=x,column=y)
        image_number = 0
        if y % 2 == x % 2:
          image_number += 13
        i = 0
        while i < 12 and not(self.bitboard[i].test_bit(x,y)):
          i+=1
        image_number +=i
        self.bind_press(x,y)
        self.set_tile(x,y,image_number)
        self.arr[x][y].bind('<ButtonRelease-1>', self.move_to_dest)

  def bind_press(self,x,y):
    if x == 0:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,0))  
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,7))
    elif x == 1:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,0))  
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,7))
    elif x == 2:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,0))  
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,7))
    elif x == 3:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,0))  
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,7))
    elif x == 4:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,0))  
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,7))
    elif x == 5:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,0))  
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,7))
    elif x == 6:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,0))  
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,7))
    elif x == 7:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,0))  
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,7))

  def conclude_game(self):
    if self.bitboard[4].value == 0:
      print("You Lose")
      self.root.destroy()
    if self.bitboard[10].value == 0:
      print("You Win")
      self.root.destroy()

  def start_game(self):
    self.root.mainloop()

  def set_grid(self,e,x,y):
    self.posx = x
    self.posy = y
    self.holding = self.images.get_piece_from_tile(self.pngarr[x][y])
    img = self.images.get_piece_bg(self.pngarr[x][y])
    self.set_tile(x,y, img)

  def set_tile(self, x,y,img):
    self.arr[x][y]['image']=self.images.get_image(img)
    self.pngarr[x][y] = img

  def update_image(self,x,y):
    img = self.images.new_tile(self.holding, self.images.get_piece_bg(self.pngarr[x][y]))
    self.set_tile(x,y,img)

  def print_board(self):
    for i in range(8):
      for j in range(8):
        pnt = (i,j)
        if self.bitboard[0].test_bit(pnt):
          print("R ", end = "")
        elif self.bitboard[1].test_bit(pnt):
          print("N ", end = "")
        elif self.bitboard[2].test_bit(pnt):
          print("B ", end = "")
        elif self.bitboard[3].test_bit(pnt):
          print("Q ", end = "")
        elif self.bitboard[4].test_bit(pnt):
          print("K ", end = "")
        elif self.bitboard[5].test_bit(pnt):
          print("P ", end = "")
        elif self.bitboard[6].test_bit(pnt):
          print("r ", end = "")
        elif self.bitboard[7].test_bit(pnt):
          print("n ", end = "")
        elif self.bitboard[8].test_bit(pnt):
          print("b ", end = "")
        elif self.bitboard[9].test_bit(pnt):
          print("q ", end = "")
        elif self.bitboard[10].test_bit(pnt):
          print("k ", end = "")
        elif self.bitboard[11].test_bit(pnt):
          print("p ", end = "")
        else:
          print("0 ", end="")
      print(" ")
    print(" ")

  def move_to_dest(self,event):
    dest = (self.posx+(event.y// 67),self.posy+(event.x//67))

    if not(self.joinboard[0].test_bit(dest)):
      for i in range(6):
        if self.bitboard[i].test_bit(self.posx,self.posy):
        
          if (((i % 6 == 0 or i % 6 == 3) and 
            movement.get_cardinal_movement((self.posx,self.posy),self.joinboard[0],self.joinboard[1]) & movement.at(dest)) or
            ((i % 6 == 2 or i % 6 == 3) and 
            movement.get_ordinal_movement((self.posx,self.posy),self.joinboard[0],self.joinboard[1]) & movement.at(dest)) or 
            (i % 6 == 1 and movement.get_knight_movement((self.posx,self.posy),self.joinboard[0]) & movement.at(dest)) or 
            (i % 6 == 4 and movement.get_king_movement((self.posx,self.posy),self.joinboard[0]) & movement.at(dest)) or 
            (i % 6 == 5 and movement.get_pawn_movement((self.posx,self.posy),self.joinboard[0],self.joinboard[1]) & movement.at(dest))):
            self.bitboard[i].move_bit((self.posx, self.posy), dest)
            for j in range(6):
              if self.bitboard[6+j].test_bit(dest):
                self.bitboard[6+j].reset_bit(dest)
            movement.upgrade_pawns(self.bitboard[5],self.bitboard[3])
            self.update_joinboards()
              
            self.conclude_game()
            return
    self.refresh_grid()

  def update_joinboards(self):
    self.joinboard[0] = movement.merge_grids(self.bitboard[0:6])
    self.joinboard[1] = movement.merge_grids(self.bitboard[6:12])

  def refresh_grid(self):
    for i in range(8):
      for j in range(8):
        k = 0
        while k < 12 and not(self.bitboard[k].test_bit((i,j))):
          k+=1
        img = self.images.new_tile(k+26, self.images.get_piece_bg(self.pngarr[i][j]))
        self.set_tile(i,j,img)
 


if __name__ == "__main__":
  game = Game()
  game.start_game()
