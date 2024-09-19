# Python Chess Engine
Chess engine written in python. 

# Prerequisites
- Python 3.0+ must be installed on your system
- If you wish to use the transposition table, you must have the mysql connector for python installed

# Features
- Alpha-Beta algorithm to search for the best move 
- Evaluates the result of a move using material, positioning, and PeSTO's piece square tables. 
- Looks up past moves in a transposition table from a MySQL database to save time 

# Setting up the transposition table
- Open and run the `database_setup.sql` file in your MySQL environment to set up the transposition table

# Running the engine
- Run `python game.py` to run without the transposition table
- Run `python game.py [database username] [database password]` to run with the transposition table