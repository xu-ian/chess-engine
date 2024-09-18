from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from movement import *
import movement
from image_initialize import Images
import time
import random



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
    self.root.geometry("544x544")

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
    self.mainframe = ttk.Frame(self.root,padding=(0,0,0,0))
    self.mainframe.grid(column=0, row=0,sticky=(N, W, E, S))
    
    #Sets up interactions with every square on the board
    for x in range(8):
      for y in range(8):
        self.arr[x][y] = ttk.Label(self.mainframe, text="Tile")
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
    self.dpiece = Label(self.mainframe, text = "Held Piece")

  def bind_press(self,x,y):
    if x == 0:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,0))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,0,0))
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,1))  
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,0,1))
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,2))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,0,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,3))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,0,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,4))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,0,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,5))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,0,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,6))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,0,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,0,7))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,0,7))
    elif x == 1:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,0))  
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,1,0))
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,1))  
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,1,1))
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,2))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,1,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,3))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,1,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,4))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,1,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,5))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,1,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,6))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,1,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,1,7))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,1,7))
    elif x == 2:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,0))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,2,0))
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,1))  
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,2,1))
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,2))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,2,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,3))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,2,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,4))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,2,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,5))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,2,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,6))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,2,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,2,7))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,2,7))
    elif x == 3:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,0))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,3,0)) 
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,1))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,3,1))
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,2))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,3,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,3))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,3,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,4))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,3,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,5))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,3,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,6))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,3,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,3,7))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,3,7))
    elif x == 4:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,0))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,4,0))
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,1))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,4,1))
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,2))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,4,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,3))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,4,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,4))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,4,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,5))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,4,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,6))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,4,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,4,7))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,4,7))
    elif x == 5:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,0)) 
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,5,0)) 
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,1))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,5,1))
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,2))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,5,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,3))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,5,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,4))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,5,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,5))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,5,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,6))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,5,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,5,7))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,5,7))
    elif x == 6:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,0))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,6,0))
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,1))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,6,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,2))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,6,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,3))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,6,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,4))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,6,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,5))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,6,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,6))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,6,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,6,7))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,6,7))
    elif x == 7:
      if y == 0:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,0))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,7,0))
      elif y == 1:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,1))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,7,1))  
      elif y == 2:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,2))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,7,2))
      elif y == 3:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,3))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,7,3))
      elif y == 4:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,4))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,7,4))
      elif y == 5:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,5))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,7,5))
      elif y == 6:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,6))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,7,6))
      elif y == 7:
        self.arr[x][y].bind('<Button-1>', lambda e: self.set_grid(e,7,7))
        self.arr[x][y].bind('<B1-Motion>', lambda e: self.move_piece(e,7,7))

  def conclude_game(self):
    if self.bitboard[4].value == 0:
      print("You Lose")
      self.root.destroy()
      return True
    if self.bitboard[10].value == 0:
      print("You Win")
      self.root.destroy()
      return True
    return False

  def start_game(self):
    self.root.mainloop()

  def evaluate_material(self):
    material = 0
    positioning = 0
    for i in range(8):
      for j in range(8):
        pnt = (i,j)
        if self.joinboard[0].test_bit(pnt):
          if self.bitboard[0].test_bit(pnt):
            material += 5
            positioning += movement.ROOK_POSVAL[i*8+j]
          elif self.bitboard[1].test_bit(pnt):
            material += 3
            positioning += movement.KNIGHT_POSVAL[i*8+j]
          elif self.bitboard[2].test_bit(pnt):
            material += 3
            positioning += movement.BISHOP_POSVAL[i*8+j]
          elif self.bitboard[3].test_bit(pnt):
            positioning += movement.QUEEN_POSVAL[i*8+j]
            material += 9
          elif self.bitboard[4].test_bit(pnt):
            positioning += movement.KING_POSVAL[i*8+j]
            material += 200
          elif self.bitboard[5].test_bit(pnt):
            positioning += movement.PAWN_POSVAL[i*8+j]
            material += 1
        elif self.joinboard[1].test_bit(pnt):
          if self.bitboard[6].test_bit(pnt):
            material -= 5
            positioning -= movement.ROOK_POSVAL[(7-i)*8+(7-j)]
          elif self.bitboard[7].test_bit(pnt):
            material -= 3
            positioning -= movement.KNIGHT_POSVAL[(7-i)*8+(7-j)]
          elif self.bitboard[8].test_bit(pnt):
            material -= 3
            positioning -= movement.BISHOP_POSVAL[(7-i)*8+(7-j)]
          elif self.bitboard[9].test_bit(pnt):
            material -= 9
            positioning -= movement.QUEEN_POSVAL[(7-i)*8+(7-j)]
          elif self.bitboard[10].test_bit(pnt):
            material -= 200
            positioning -= movement.KING_POSVAL[(7-i)*8+(7-j)]
          elif self.bitboard[11].test_bit(pnt):
            material -= 1
            positioning -= movement.PAWN_POSVAL[(7-i)*8+(7-j)]
    return material + 0.01*positioning

  def evaluate_mobility(self):
    mob = [0,0]
    for i in range(8):
      for j in range(8):
        pos = (i,j)
        if self.joinboard[0].test_bit(pos):
          if self.bitboard[0].test_bit(pos):
            mob[0] += 3*(i < 6) + 3*((movement.VERT << j) & self.bitboard[5].value == 0)
          elif self.bitboard[1].test_bit(pos):
            mob[0] += 1 + 2*(i > 1 and i < 6 and j > 1 and j < 7)
          elif self.bitboard[2].test_bit(pos):
            mob[0] += 2*(i < 6)
          elif self.bitboard[3].test_bit(pos):
            mob[0] += 1 + 7*(i < 6)
          elif self.bitboard[4].test_bit(pos):
            mob[0] += 1
          elif self.bitboard[5].test_bit(pos):
            mob[0] += (i == 6 or i == 5 or i == 4)
        elif self.joinboard[1].test_bit(pos):
          if self.bitboard[6].test_bit(pos):
            mob[1] += 3*(i > 1) + 3*((movement.VERT << j) & self.bitboard[11].value == 0)
          if self.bitboard[7].test_bit(pos):
            mob[1] += 1 + 2*(i > 1 and i < 6 and j > 1 and j < 7)
          elif self.bitboard[8].test_bit(pos):
            mob[1] += 2*(i > 1)
          elif self.bitboard[9].test_bit(pos):
            mob[1] += 1 + 7*(i > 1)
          elif self.bitboard[10].test_bit(pos):
            mob[1] += 1
          elif self.bitboard[11].test_bit(pos):
            mob[1] += (i == 1 or i == 2 or i == 3)
    return (mob[0]-mob[1])

  def evaluate(self, multiplier):
    self.count += 1
    if self.count % 1000 == 0:
      print("Number: ", self.count, ", F1 Elapsed Time: ", self.elapsed, ", F2 Elapsed Time: ", self.elapsed2)
    start_time = time.perf_counter()
    val = self.evaluate_material() 
    end_time = time.perf_counter()
    val2 = 0.1*self.evaluate_mobility()
    end_time_2 = time.perf_counter()
    self.elapsed += (end_time - start_time)
    self.elapsed2 += (end_time_2 - end_time)
    return multiplier*(val + val2 + random.uniform(0,0.3))

  def alphaBetaMax(self, alpha, beta, depth):
    if depth == 0:
      return (self.evaluate(-1),((0,0),(0,0)))
    best_value = (-9999999,((0,0),(0,0)))
    #Iterates through the whole grid and if it lands on a 
    #valid piece saves the valid moves in dgrid
    for i in range(8):
      for j in range(8):
        bgn = (i,j)
        dgrid = 0
        gridnum = -1
        for k in range(6):
          if self.bitboard[6+k].test_bit(bgn):
            if k == 0:
              dgrid = movement.get_cardinal_movement(bgn, self.joinboard[1], self.joinboard[0])
              gridnum = 6+k
            elif k == 1:
              dgrid = movement.get_knight_movement(bgn, self.joinboard[1])
              gridnum = 6+k
            elif k == 2:
              dgrid = movement.get_ordinal_movement(bgn, self.joinboard[1], self.joinboard[0])
              gridnum = 6+k          
            elif k == 3:
              dgrid = (movement.get_cardinal_movement(bgn, self.joinboard[1], self.joinboard[0]) + 
                movement.get_ordinal_movement(bgn, self.joinboard[1], self.joinboard[0]))
              gridnum = 6+k              
            elif k == 4:
              dgrid = movement.get_king_movement(bgn, self.joinboard[1])
              gridnum = 6+k
            else:
              dgrid = movement.get_pawn_movement(bgn, self.joinboard[0], self.joinboard[1])
              gridnum = 6+k            

        #If a valid move exists for this piece check the score for all possible moves
        if dgrid != 0:
          dgrid = Grid(dgrid)
          
          for i2 in range(8):
            for j2 in range(8):
              dst = (i2,j2)
              if dgrid.test_bit(dst):
                #Moves the piece
                temp_board = self.bitboard[gridnum].copy()
                temp_board2 = Grid(0)
                self.bitboard[gridnum].move_bit(bgn,dst)
                tmp = -1
                for k2 in range(12):
                  if k2 != gridnum and self.bitboard[k2].test_bit(dst):
                    tmp = k2
                    temp_board2 = self.bitboard[k2].copy()
                    self.bitboard[k2].reset_bit(dst)
                    break
                self.update_joinboards()
                #Checks the score
                score = self.alphaBetaMin(alpha, beta, depth-1)
                score = (score[0],(bgn,dst))

                #print(score)
                #Unmoves the piece
                if tmp != -1:
                  self.bitboard[tmp] = temp_board2
                self.bitboard[gridnum] = temp_board
                self.update_joinboards()
                #print("Score: ", score[0], ", best value: ", best_value, ", alpha: ", alpha, ", beta: ", beta)
                if score[0] > best_value[0]:
                  if score[0] > alpha:
                    alpha = score[0]
                  best_value = (alpha, (bgn,dst))
                if score[0] >= beta:
                  return score
    #print("Best value: ", best_value)
    #print(" ")
    return best_value

  def alphaBetaMin(self, alpha, beta, depth):
    if depth == 0:
      return (self.evaluate(1),((0,0),(0,0)))
    best_value = (9999999, ((0,0),(0,0)))
    for i in range(8):
      for j in range(8):
        bgn = (i,j)
        dgrid = 0
        gridnum = -1
        for k in range(6):
          if self.bitboard[k].test_bit(bgn):
            if k == 0:
              dgrid = movement.get_cardinal_movement(bgn, self.joinboard[0], self.joinboard[1])
              gridnum = k
            elif k == 1:
              dgrid = movement.get_knight_movement(bgn, self.joinboard[0])
              gridnum = k
            elif k == 2:
              dgrid = movement.get_ordinal_movement(bgn, self.joinboard[0],self.joinboard[1])
              gridnum = k          
            elif k == 3:
              dgrid = (movement.get_cardinal_movement(bgn, self.joinboard[0], self.joinboard[1]) + 
                movement.get_ordinal_movement(bgn, self.joinboard[0], self.joinboard[1]))
              gridnum = k              
            elif k == 4:
              dgrid = movement.get_king_movement(bgn, self.joinboard[0])
              gridnum = k            
            else:
              dgrid = movement.get_pawn_movement(bgn, self.joinboard[0], self.joinboard[1])
              gridnum = k            

        #If a valid move exists for this piece check the score for all possible moves
        if dgrid != 0:
          dgrid = Grid(dgrid)
          for i2 in range(8):
            for j2 in range(8):
              dst = (i2,j2)
              if dgrid.test_bit(dst):
                #Moves the piece
                temp_board = self.bitboard[gridnum].copy()
                temp_board2 = Grid(0)
                self.bitboard[gridnum].move_bit(bgn,dst)
                tmp = -1
                for k2 in range(12):
                  if k2 != gridnum and self.bitboard[k2].test_bit(dst):
                    tmp = k2
                    temp_board2 = self.bitboard[k2].copy()
                    self.bitboard[k2].reset_bit(dst)
                    break
                self.update_joinboards()
                #Checks the score
                score = self.alphaBetaMax(alpha, beta, depth-1)
                score = (score[0],(bgn,dst))
                #print("Score: ", score, ", Best: ",best_value, ", Alpha: ", alpha, ", Beta: ", beta)
                #Unmoves the piece
                if tmp != -1:
                  self.bitboard[tmp] = temp_board2
                self.bitboard[gridnum] = temp_board
                self.update_joinboards()
                #Alpha Beta Pruning
                if score[0] < best_value[0]:
                  if score[0] < beta:
                    beta = score[0]
                  best_value = (beta,(bgn,dst))
                if score[0] <= alpha:
                  return score
    #print("Returning: ", best_value)
    #print(" ")
    return best_value

  def set_grid(self,e,x,y):
    self.posx = x
    self.posy = y
    self.holding = self.images.get_piece_from_tile(self.pngarr[x][y])
    img = self.images.get_piece_bg(self.pngarr[x][y])
    if self.holding < 38:
      self.dpiece = Label(self.mainframe, text = "Held Piece")
      self.dpiece['image'] = self.images.get_image(self.holding)

    self.set_tile(x,y, img)

  def move_piece(self, e, x, y):
    self.dpiece.place(x = e.x+(y*67), y = e.y+(x*67), anchor = CENTER)
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
    self.dpiece.destroy()
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
            self.refresh_grid()
            print("This occurs")
            if self.conclude_game():
              return
            #time.sleep(0.5)
            stt = time.perf_counter()
            #score = self.alphaBetaMax(-99999999, 99999999, 4)
            elp = time.perf_counter() - stt
            print("Total Elapsed Time: ", elp)
            #bgn = score[1][0]
            #dst = score[1][1]
            dstbrd = -1
            #for i in range(12):
            #  if self.bitboard[i].test_bit(bgn):
            #    dstbrd = i
            #    self.bitboard[i].move_bit(bgn,dst)
            #  if dstbrd != i and self.bitboard[i].test_bit(dst):
            #    self.bitboard[i].reset_bit(dst)
            #self.update_joinboards()
            #self.refresh_grid()
            #print(score)
            if self.conclude_game():
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
