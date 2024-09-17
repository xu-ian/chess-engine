import math
#Upper right diagonal from (7,0)
DIAG_NE = 0x01_02_04_08_10_20_40_80
#Upper left diagonal from (0,0)
DIAG_NW = 0x80_40_20_10_08_04_02_01
#Vertical movement from (7,x)
VERT = 0x01_01_01_01_01_01_01_01
#Horizontal movement from (x,7)
HORI = 0x00_00_00_00_00_00_00_FF

UR = 0xFF_7F_3F_1F_0F_07_03_01
BL = 0x80_C0_E0_F0_F8_FC_FE_FF
BR = 0xFF_FE_FC_F8_F0_E0_C0_80
UL = 0x01_03_07_0F_1F_3F_7F_FF

UPGRADE = 0x00_00_00_00_00_00_00_FF

#Starting Positions of all pieces
OPP_ROOK = 0x81_00_00_00_00_00_00_00
OPP_KNHT = 0x42_00_00_00_00_00_00_00
OPP_BSHP = 0x24_00_00_00_00_00_00_00
OPP_QUEN = 0x10_00_00_00_00_00_00_00
OPP_KING = 0x08_00_00_00_00_00_00_00
OPP_PAWN = 0x00_FF_00_00_00_00_00_00
OPP_BORD = 0xFF_FF_00_00_00_00_00_00

YOU_ROOK = 0x00_00_00_00_00_00_00_81
YOU_KNHT = 0x00_00_00_00_00_00_00_42
YOU_BSHP = 0x00_00_00_00_00_00_00_24
YOU_QUEN = 0x00_00_00_00_00_00_00_10
YOU_KING = 0x00_00_00_00_00_00_00_08
YOU_PAWN = 0x00_00_00_00_00_00_FF_00
YOU_BORD = 0x00_00_00_00_00_00_FF_FF

PAWN_POSVAL = (0,   0,   0,   0,   0,   0,  0,   0,
     98, 134,  61,  95,  68, 126, 34, -11,
     -6,   7,  26,  31,  65,  56, 25, -20,
    -14,  13,   6,  21,  23,  12, 17, -23,
    -27,  -2,  -5,  12,  17,   6, 10, -25,
    -26,  -4,  -4, -10,   3,   3, 33, -12,
    -35,  -1, -20, -23, -15,  24, 38, -22,
      0,   0,   0,   0,   0,   0,  0,   0)
KNIGHT_POSVAL = (-167, -89, -34, -49,  61, -97, -15, -107,
     -73, -41,  72,  36,  23,  62,   7,  -17,
     -47,  60,  37,  65,  84, 129,  73,   44,
      -9,  17,  19,  53,  37,  69,  18,   22,
     -13,   4,  16,  13,  28,  19,  21,   -8,
     -23,  -9,  12,  10,  19,  17,  25,  -16,
     -29, -53, -12,  -3,  -1,  18, -14,  -19,
    -105, -21, -58, -33, -17, -28, -19,  -23)
BISHOP_POSVAL = (-29,   4, -82, -37, -25, -42,   7,  -8,
    -26,  16, -18, -13,  30,  59,  18, -47,
    -16,  37,  43,  40,  35,  50,  37,  -2,
     -4,   5,  19,  50,  37,  37,   7,  -2,
     -6,  13,  13,  26,  34,  12,  10,   4,
      0,  15,  15,  15,  14,  27,  18,  10,
      4,  15,  16,   0,   7,  21,  33,   1,
    -33,  -3, -14, -21, -13, -12, -39, -21)
ROOK_POSVAL = (32,  42,  32,  51, 63,  9,  31,  43,
     27,  32,  58,  62, 80, 67,  26,  44,
     -5,  19,  26,  36, 17, 45,  61,  16,
    -24, -11,   7,  26, 24, 35,  -8, -20,
    -36, -26, -12,  -1,  9, -7,   6, -23,
    -45, -25, -16, -17,  3,  0,  -5, -33,
    -44, -16, -20,  -9, -1, 11,  -6, -71,
    -19, -13,   1,  17, 16,  7, -37, -26)
QUEEN_POSVAL = (-28,   0,  29,  12,  59,  44,  43,  45,
    -24, -39,  -5,   1, -16,  57,  28,  54,
    -13, -17,   7,   8,  29,  56,  47,  57,
    -27, -27, -16, -16,  -1,  17,  -2,   1,
     -9, -26,  -9, -10,  -2,  -4,   3,  -3,
    -14,   2, -11,  -2,  -5,   2,  14,   5,
    -35,  -8,  11,   2,   8,  15,  -3,   1,
     -1, -18,  -9,  10, -15, -25, -31, -50)
KING_POSVAL = (-65,  23,  16, -15, -56, -34,   2,  13,
     29,  -1, -20,  -7,  -8,  -4, -38, -29,
     -9,  24,   2, -16, -20,   6,  22, -22,
    -17, -20, -12, -27, -30, -25, -14, -36,
    -49,  -1, -27, -39, -46, -44, -33, -51,
    -14, -14, -22, -46, -44, -30, -15, -27,
      1,   7,  -8, -64, -43, -16,   9,   8,
    -15,  36,  12, -54,   8, -28,  24,  14)

def at(x,y=None):
  '''
  Returns a grid with a piece at coord.
  coord is an (x,y) tuple
  '''
  if y == None:
    return 0b1 << x[0]*8+x[1]
  return 0b1 << x*8+y

def coord(val):
  '''
  Returns a coordinate from a grid with a single point
  '''
  val = math.log(val,2)
  return (val// 8, val % 8)

def merge_grids(grids):
  '''
  Merges an array of grids and returns it.
  '''
  temp_grid = 0
  for grid in grids:
    temp_grid |= grid.value
  return Grid(temp_grid)

class Grid:
  def __init__(self, bitboard):
    self.value = bitboard
  
  def __str__(self):
    return self.value

  def __iand__(self,other):
    return self.value & other.value

  def set_bit(self, x, y=None):
    if y == None:
      self.value |= at(x)
    else:
      self.value |= at(x,y)

  def reset_bit(self,x,y=None):
    '''
    Removes a piece at coord from grid.
    coord is an (x,y) tuple
    '''
    if y == None:
      self.value &= ~at(x)
    else:
      self.value &= ~at(x,y)

  def toggle_bit(self, x, y=None):
    '''
    Toggles a possible piece at coord from grid.
    '''
    if y == None:
      self.value ^= at(x)
    else:
      self.value ^= at(x,y)

  def test_bit(self, x, y=None):
    '''
    Retrieves the existance of a piece at coord from grid.
    coord is an (x,y) tuple
    '''
    if y == None:
      return self.value & at(x)
    return self.value & at(x,y)

  def move_bit(self, bgn, dst):
    '''
    Moves a piece on grid from bgn to dst.
    bgn and dst are (x,y) tuples
    '''
    self.set_bit(dst)
    self.reset_bit(bgn)
  
  def copy(self):
    return Grid(self.value | 0)

  def count(self):
    acc = 0
    for i in range(8):
      for j in range(8):
        acc += self.test_bit((i,j)) > 0
    return acc

  def print_grid(self):
    for i in range(8):
      for j in range(8):
        if self.test_bit((i,j)):
          print('1 ',end='')
        else:
          print('0 ',end='')
      print('')
    print('')

  def rotate_180(self):
    for i in range(4):
      for j in range(8):
        if self.test_bit((i,j)) != self.test_bit((7-i,7-j)):
          self.toggle_bit((i,j))
          self.toggle_bit((7-i,7-j))

  def is_cardinal_clear(board, pnt1, pnt2):
    '''
    Check if the cardinal movement between pnt1 and pnt2 is clear.
    pnt1 should have less or equal coordinate numbers than pnt2
    '''
    board.reset_bit(pnt1)
    board.reset_bit(pnt2)
    tmp_pnt = pnt2
    tmp_pnt2 = pnt1
    if pnt1[0] < pnt2[0] or pnt1[1] < pnt2[1]:
      print("Switching")
      tmp_pnt = pnt1
      tmp_pnt2 = pnt2
    while tmp_pnt[0] != tmp_pnt2[0]:
      if board.test_bit(tmp_pnt):
        return False
      tmp_pnt = (tmp_pnt[0]+1,tmp_pnt[1])
    while tmp_pnt[1] != tmp_pnt2[1]:
      if board.test_bit(tmp_pnt):
        return False
      tmp_pnt = (tmp_pnt[0],tmp_pnt[1]+1)
    return True

  def is_ordinal_clear(board, pnt1, pnt2):
    '''
    Check if ordinal movement between pnt1 and pnt2 is clear.
    pnt1 should be below pnt2
    '''
    board.reset_bit(pnt1)
    board.reset_bit(pnt2)

    tmp_pnt = pnt1
    tmp_pnt2 = pnt2
    if pnt1[1] > pnt2[1]:
      tmp_pnt = pnt2
      tmp_pnt2 =pnt1

    if tmp_pnt[0] < tmp_pnt2[0]:
      while tmp_pnt[1] != tmp_pnt2[1]:
        if board.test_bit(tmp_pnt):
          return False
        tmp_pnt = (tmp_pnt[0] + 1, tmp_pnt[1]+1)
    else:
      while tmp_pnt[1] != tmp_pnt2[1]:
        if board.test_bit(tmp_pnt):
          return False
        tmp_pnt = (tmp_pnt[0]-1, tmp_pnt[1]+1)
    return True

def get_cardinal_movement(coord, youboard, oppboard):
  grid = 0
  left = 1
  right = 1
  up = 1
  down = 1
  while coord[0] - left >= 0 and not(youboard.test_bit(coord[0] - left, coord[1])):
    grid |= at(coord[0] - left, coord[1])
    if oppboard.test_bit(coord[0] - left, coord[1]):
      break
    left += 1

  while coord[0] + right < 8 and not(youboard.test_bit(coord[0] + right, coord[1])):
    grid |= at(coord[0]+ right, coord[1])
    if oppboard.test_bit(coord[0] + right, coord[1]):
      break
    right += 1

  while coord[1] - up >= 0 and not(youboard.test_bit(coord[0], coord[1] - up)):
    grid |= at(coord[0],coord[1]-up)
    if oppboard.test_bit((coord[0], coord[1] - up)):
      break
    up += 1

  while coord[1] + down < 8 and not(youboard.test_bit(coord[0], coord[1] + down)):
    grid |= at(coord[0],coord[1]+down)
    if oppboard.test_bit(coord[0], coord[1] + down):
      break
    down += 1
    
  return grid

def count_cardinal_movement(coord, youboard, oppboard):
  left = 1
  right = 1
  up = 1
  down = 1
  while coord[0] - left >= 0 and not(youboard.test_bit(coord[0] - left, coord[1])):
    if oppboard.test_bit(coord[0] - left, coord[1]):
      left += 1
      break
    left += 1

  while coord[0] + right < 8 and not(youboard.test_bit(coord[0] + right, coord[1])):
    if oppboard.test_bit(coord[0] + right, coord[1]):
      right += 1
      break
    right += 1

  while coord[1] - up >= 0 and not(youboard.test_bit(coord[0], coord[1] - up)):
    if oppboard.test_bit((coord[0], coord[1] - up)):
      up += 1
      break
    up += 1

  while coord[1] + down < 8 and not(youboard.test_bit(coord[0], coord[1] + down)):
    if oppboard.test_bit(coord[0], coord[1] + down):
      down += 1
      break
    down += 1
    
  return left + right + up + down - 4

def get_ordinal_movement(coord, youboard, oppboard):
  grid = 0
  ul = 1
  ur = 1
  bl = 1
  br = 1
  count = 0
  while coord[0] - ul >= 0 and coord[1] - ul >= 0 and not(youboard.test_bit(coord[0]-ul,coord[1]-ul)):
    grid |= at(coord[0]-ul,coord[1]-ul)
    if oppboard.test_bit(coord[0]-ul,coord[1]-ul):
      break
    ul += 1
  while coord[0] + ur < 8 and coord[1] - ur >= 0 and not(youboard.test_bit(coord[0]+ur,coord[1]-ur)):
    grid |= at(coord[0]+ur,coord[1]-ur)
    if oppboard.test_bit(coord[0]+ur,coord[1]-ur):
      break
    ur += 1
  while coord[0] - bl >= 0 and coord[1] + bl < 8 and not(youboard.test_bit(coord[0]-bl,coord[1]+bl)):
    grid |= at(coord[0]-bl,coord[1]+bl)
    if oppboard.test_bit(coord[0]-bl,coord[1]+bl):
      break
    bl += 1
  while coord[0] + br < 8 and coord[1] + br < 8 and not(youboard.test_bit(coord[0]+br,coord[1]+br)):
    grid |= at(coord[0]+br,coord[1]+br)
    if oppboard.test_bit(coord[0]+br,coord[1]+br):
      break
    br += 1
  return grid

def count_ordinal_movement(coord, youboard, oppboard):
  ul = 1
  ur = 1
  bl = 1
  br = 1
  while coord[0] - ul >= 0 and coord[1] - ul >= 0 and not(youboard.test_bit(coord[0]-ul,coord[1]-ul)):
    if oppboard.test_bit(coord[0]-ul,coord[1]-ul):
      ul += 1
      break
    ul += 1
  while coord[0] + ur < 8 and coord[1] - ur >= 0 and not(youboard.test_bit(coord[0]+ur,coord[1]-ur)):
    if oppboard.test_bit(coord[0]+ur,coord[1]-ur):
      ur += 1
      break
    ur += 1
  while coord[0] - bl >= 0 and coord[1] + bl < 8 and not(youboard.test_bit(coord[0]-bl,coord[1]+bl)):
    if oppboard.test_bit(coord[0]-bl,coord[1]+bl):
      bl += 1
      break
    bl += 1
  while coord[0] + br < 8 and coord[1] + br < 8 and not(youboard.test_bit(coord[0]+br,coord[1]+br)):
    if oppboard.test_bit(coord[0]+br,coord[1]+br):
      br += 1
      break
    br += 1
  return ul + ur + bl + br - 4

def get_knight_movement(coord, youboard):
  arr = [(coord[0]-1,coord[1]-2),(coord[0]-2,coord[1]-1),(coord[0]+1,coord[1]-2),(coord[0]+2,coord[1]-1),
    (coord[0]-1,coord[1]+2),(coord[0]-2,coord[1]+1),(coord[0]+1,coord[1]+2),(coord[0]+2,coord[1]+1)]
  pos = [Grid(0) for i in range(8)]
  for i in range(8):
    if arr[i][0] >= 0 and arr[i][0] < 8 and arr[i][1] >= 0 and arr[i][1] < 8:
      pos[i].value = ~(youboard.value) & at(arr[i])
  return merge_grids(pos).value

def count_knight_movement(coord, youboard):
  arr = [(coord[0]-1,coord[1]-2),(coord[0]-2,coord[1]-1),(coord[0]+1,coord[1]-2),(coord[0]+2,coord[1]-1),
    (coord[0]-1,coord[1]+2),(coord[0]-2,coord[1]+1),(coord[0]+1,coord[1]+2),(coord[0]+2,coord[1]+1)]
  pos = 0
  for i in range(8):
    if arr[i][0] >= 0 and arr[i][0] < 8 and arr[i][1] >= 0 and arr[i][1] < 8:
      pos += youboard.test_bit(arr[i]) == 0
  return pos

def get_king_movement(coord, youboard):
  arr = [(coord[0]-1,coord[1]-1),(coord[0],coord[1]-1),(coord[0]+1,coord[1]-1),(coord[0]-1,coord[1]),
    (coord[0]+1,coord[1]),(coord[0]-1,coord[1]+1),(coord[0],coord[1]+1),(coord[0]+1,coord[1]+1)]
  pos = [Grid(0) for i in range(8)]
  for i in range(8):
    if arr[i][0] >= 0 and arr[i][0] < 8 and arr[i][1] >= 0 and arr[i][1] < 8:
      pos[i].value = ~(youboard.value) & at(arr[i])
  return merge_grids(pos).value

def count_king_movement(coord, youboard):
  arr = [(coord[0]-1,coord[1]-1),(coord[0],coord[1]-1),(coord[0]+1,coord[1]-1),(coord[0]-1,coord[1]),
    (coord[0]+1,coord[1]),(coord[0]-1,coord[1]+1),(coord[0],coord[1]+1),(coord[0]+1,coord[1]+1)]
  pos = 0
  for i in range(8):
    if arr[i][0] >= 0 and arr[i][0] < 8 and arr[i][1] >= 0 and arr[i][1] < 8:
      pos += (~(youboard.value) & at(arr[i])) > 0
  return pos

def get_pawn_movement(coord, youboard, oppboard):
  shmovement = 0
  dir = 1 
  if youboard.test_bit(coord):
    dir = -1

  joing = merge_grids([youboard,oppboard])
  if not(joing.test_bit(coord[0]+dir,coord[1])):
    shmovement |= at(coord[0]+dir,coord[1])
  if dir == -1:
    if coord[1]-1 >= 0 and oppboard.test_bit(coord[0]+dir,coord[1]-1):
      shmovement |= at(coord[0]+dir,coord[1]-1)
    if coord[1] + 1 < 8 and oppboard.test_bit(coord[0]+dir,coord[1]+1):
      shmovement |= at(coord[0]+dir,coord[1]+1)
    if (Grid(OPP_PAWN).test_bit(coord) and not(joing.test_bit(coord[0]+dir,coord[1])) and 
      not(joing.test_bit(coord[0]+(dir*2),coord[1]))):
      shmovement |= at(coord[0]+(dir*2),coord[1])
  else:
    if coord[1] -1 >= 0 and youboard.test_bit(coord[0]+dir,coord[1]-1):
      shmovement |= at(coord[0]+dir,coord[1]-1)
    if coord[1] + 1 < 8 and youboard.test_bit(coord[0]+dir,coord[1]+1):
      shmovement |= at(coord[0]+dir,coord[1]+1)
    if (Grid(YOU_PAWN).test_bit(coord) and not(joing.test_bit(coord[0]+dir,coord[1])) and 
      not(joing.test_bit(coord[0]+(dir*2),coord[1]))):
      shmovement |= at(coord[0]+(dir*2),coord[1])
  return shmovement

def count_pawn_movement(coord, youboard, oppboard):
  dir = 1 
  count = 0
  if youboard.test_bit(coord):
    dir = -1

  joing = merge_grids([youboard,oppboard])
  if joing.test_bit(coord[0]+dir,coord[1]) == 0:
    count += 1 
  if dir == -1:
    if coord[1]-1 >= 0 and oppboard.test_bit(coord[0]-1,coord[1]-1):
      count += 1
    if coord[1] + 1 < 8 and oppboard.test_bit(coord[0]-1,coord[1]+1):
      count += 1
    if (Grid(OPP_PAWN).test_bit(coord) and joing.test_bit(coord[0]-1,coord[1]) == 0 and 
      joing.test_bit(coord[0]-2,coord[1]) == 0):
      count += 1
  else:
    if coord[1] -1 >= 0 and youboard.test_bit(coord[0]+1,coord[1]-1):
      count += 1
    if coord[1] + 1 < 8 and youboard.test_bit(coord[0]+1,coord[1]+1):
      count += 1
    if (Grid(YOU_PAWN).test_bit(coord) and not(joing.test_bit(coord[0]+1,coord[1])) and 
      not(joing.test_bit(coord[0]+2,coord[1]))):
      count += 1
  return count

def upgrade_pawns(pawns, queens):
  queens.value |= pawns.value & UPGRADE
  pawns.value &= ~(pawns.value & UPGRADE)