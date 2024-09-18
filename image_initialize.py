from PIL import Image, ImageTk
from tkinter import PhotoImage

PREFIX = './images/'

class Images:
  def __init__(self):
    '''
    Array of all tiles.
    0-5: White pieces on white tiles
    6-11: Black pieces on white tiles
    12: White tile empty
    13-18: White pieces on black tiles
    19-24: Black pieces on black tiles
    25: Black tile empty
    Pieces are in order Rook, Knight, Bishop, Queen, King, Pawn 
    '''
    #Loads the black and white board tiles

    self.tile_arr = [0 for i in range(38)]
    blank = Image.open(PREFIX + 'blank.png')
    for i in range(26):
      piece = Image.open(PREFIX + 'blank.png')
      match i % 13:
        case 0:
          piece = Image.open(PREFIX + 'white_rook.png')
          print(piece.mode)
        case 1:
          piece = Image.open(PREFIX + 'white_knight.png')
        case 2:
          piece = Image.open(PREFIX + 'white_bishop.png')
        case 3:
          piece = Image.open(PREFIX + 'white_queen.png')
        case 4:
          piece = Image.open(PREFIX + 'white_king.png')
        case 5:
          piece = Image.open(PREFIX + 'white_pawn.png')
        case 6:
          piece = Image.open(PREFIX + 'black_rook.png')
        case 7:
          piece = Image.open(PREFIX + 'black_knight.png')
        case 8:
          piece = Image.open(PREFIX + 'black_bishop.png')
        case 9:
          piece = Image.open(PREFIX + 'black_queen.png')
        case 10:
          piece = Image.open(PREFIX + 'black_king.png')
        case 11:
          piece = Image.open(PREFIX + 'black_pawn.png')
      if i // 13 > 0:#Black Tiles
        background = Image.open(PREFIX + 'chess_board_black.png')
        if piece != blank:
          background.paste(piece, (0,0),piece)
        self.tile_arr[i] = ImageTk.PhotoImage(background)
      else:#White Tiles
        background = Image.open(PREFIX + 'chess_board_white.png')
        if piece != blank:
          background.paste(piece, (0,0),piece)
        self.tile_arr[i] = ImageTk.PhotoImage(background)
    self.tile_arr[26] = PhotoImage(file=PREFIX + 'white_rook.png')
    self.tile_arr[27] = PhotoImage(file=PREFIX + 'white_knight.png')
    self.tile_arr[28] = PhotoImage(file=PREFIX + 'white_bishop.png')
    self.tile_arr[29] = PhotoImage(file=PREFIX + 'white_queen.png')
    self.tile_arr[30] = PhotoImage(file=PREFIX + 'white_king.png')
    self.tile_arr[31] = PhotoImage(file=PREFIX + 'white_pawn.png')
    self.tile_arr[32] = PhotoImage(file=PREFIX + 'black_rook.png')
    self.tile_arr[33] = PhotoImage(file=PREFIX + 'black_knight.png')
    self.tile_arr[34] = PhotoImage(file=PREFIX + 'black_bishop.png')
    self.tile_arr[35] = PhotoImage(file=PREFIX + 'black_queen.png')
    self.tile_arr[36] = PhotoImage(file=PREFIX + 'black_king.png')
    self.tile_arr[37] = PhotoImage(file=PREFIX + 'black_pawn.png')

  def get_image(self, number):
    return self.tile_arr[number]

  def get_piece_from_tile(self, piece):
    return 26 + (piece % 13)

  def get_piece_bg(self, piece):
    return 12 + 13*(piece // 13)

  def new_tile(self, piece, background):
    return (piece - 26) + (background - 12)