import mysql.connector
import logging
import time
from movement import Grid

STORE_MOVE = ("INSERT INTO stored_moves(side, board_state, depth, move, value) VALUES(%s,%s,%s,%s,%s)")
GET_MOVES = ("SELECT move, depth, value FROM stored_moves WHERE side=%s AND board_state=%s AND depth>=%s")
COUNT_MOVES = ("SELECT COUNT(*) FROM stored_moves WHERE side=%s AND board_state=%s AND depth=%s")
UPDATE_MOVE = ("UPDATE stored_moves SET move=%s, value=%s WHERE side=%s AND board_state=%s AND depth=%s")


def translate_state(state):
  '''
  Translates the board state from an array of grids into a string representation separated by commas
  '''
  boards = ["" for i in range(len(state))]
  for i in range(len(state)):
    boards[i] = str(state[i].value)
  return ",".join(boards)

def untranslate_state(dbval):
  '''
  Translates the comma separated string back into an array of grids
  '''
  if dbval == None:
    return None
  state = dbval.split(",")
  boards = [Grid(0) for i in range(len(state))]
  for i in range(len(state)):
    boards[i] = Grid(int(state[i]))
  return boards

def translate_move(move):
  '''
  Translates the start to dest move tuple to x,y.x,y format
  '''

  return str(move[0][0]) + "," + str(move[0][1])+"."+str(move[1][0]) +","+str(move[1][1])

def untranslate_move(dbval):
  '''
  Translates the x,y.x,y format to the start dest move tuple
  '''
  if dbval == None:
    return None
  move = dbval.split(".")
  move[0] = move[0].split(",")
  move[1] = move[1].split(",")
  return ((int(move[0][0]),int(move[0][1])),(int(move[1][0]),int(move[1][1])))

class DB_Access:
  def __init__(self,username,password):
    '''
    Creates a database connector object to commuicate with the MySQL server 
    '''
    self.logger = logging.getLogger(__name__)
    self.logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    self.logger.addHandler(handler)

    attempt = 1

    config = {
      'user': username,
      'password': password,
      'host': '127.0.0.1',
      'database': 'chess_engine',
      'raise_on_warnings': True
    }

    self.cnx = None

    # Implement a reconnection routine
    while attempt < 4:
      try:
        self.cnx = mysql.connector.connect(**config)
        break
      except (mysql.connector.Error, IOError) as err:
        if (3 == attempt):
          # Attempts to reconnect failed; returning None
          self.logger.info("Failed to connect, exiting without a connection: %s", err)
          break
        self.logger.info(
              "Connection failed: %s. Retrying (%d/%d)...",
              err,
              attempt,
              2,
        )
        # progressive reconnect delay
        time.sleep(2 ** attempt)
        attempt += 1
    if self.cnx != None:
      print("Success: Connected to database")
  
  def check_move(self, side, state, depth):
    '''
    Returns the best move for the board state calculated at the required depth
    '''
    cursor = self.cnx.cursor()
    cursor.execute(GET_MOVES, (side, translate_state(state), depth))
    max_depth = 0
    best_move = None
    best_value = 0
    for (move, depth, value) in cursor:
      if depth > max_depth:
        max_depth = depth
        best_move = move
        best_value = value
    cursor.close()
    if best_move == None:
      return None
    return (float(best_value), untranslate_move(best_move))

  def save_move(self, side, state, depth, move, value):
    '''
    Saves the move at the current board state and depth into the database
    '''
    cursor = self.cnx.cursor()
    cursor.execute(COUNT_MOVES, (side, translate_state(state), depth))
    if cursor.fetchone()[0] > 0:
      cursor.execute(UPDATE_MOVE,(translate_move(move),value,side, translate_state(state),depth))
    else:
      cursor.execute(STORE_MOVE,(side, translate_state(state),depth,translate_move(move),value))
    self.cnx.commit()
    cursor.close()