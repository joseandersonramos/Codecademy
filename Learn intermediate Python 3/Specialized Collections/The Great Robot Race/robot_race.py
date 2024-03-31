# 🤖 The Great Robot Race Project
# José Anderson Ramos Aquino 03/31/2024

import robot_race_functions as rr
from collections import deque, Counter, namedtuple
from time import time, sleep

maze_file_name = 'maze_data_1.csv'
seconds_between_turns = 0.3
max_turns = 35

# Initialize the robot race
maze_data = rr.read_maze(maze_file_name)
rr.print_maze(maze_data)
walls, goal, bots = rr.process_maze_init(maze_data)

# Populate a deque of all robot commands for the provided maze
robot_moves = deque()
num_of_turns = 0
while not rr.is_race_over(bots) and num_of_turns < max_turns:
  # For every bot in the list of bots, if the bot has not reached the end, add a new move to the robot_moves deque
  # Add your code below!
  for bot in bots:
    if bot.has_finished == False:
      decision = rr.compute_robot_logic(walls, goal, bot)
      robot_moves.append(decision)
  
  num_of_turns += 1

# Count the number of moves based on the robot names
# Add your code below!
moves_counter = Counter(move[0] for move in robot_moves)

# Count the number of collisions by robot name
# Add your code below!
collisions_counter = Counter(move[0] for move in robot_moves if move[2])

# Create a namedtuple to keep track of our robots' points
# Add your code below!
BotScoreData = namedtuple('BotScoreData', 'name num_moves num_collisions score')

# Calculate the scores (moves + collisions) for each robot and append it to bot_scores 
bot_scores = []
# Add your code below!
for bot in bots:
  name = bot.name
  num_moves = moves_counter[name]
  num_collisions = collisions_counter[name]
  score = num_moves + num_collisions

  bot_scores.append(BotScoreData(name, num_moves, num_collisions, score))

# Populate a dict to keep track of the robot movements
bot_data = {}
# Add your code below!
for bot in bots:
  bot_data[bot.name] = bot

# Move the robots and update the map based on the moves deque
while len(robot_moves) > 0:
  # Make sure to pop moves from the front of the deque
  # Add your code below!
  move = robot_moves.popleft() # (name, action, collision)
  bot_name = move[0]
  bot_move = move[1]

  bot_data[bot_name].process_move(bot_move)

  # Update the maze characters based on the robot positions and print it to the console
  rr.update_maze_characters(maze_data, bots)
  rr.print_maze(maze_data)
  sleep(seconds_between_turns - time() % seconds_between_turns)

# Print out the results!
rr.print_results(bot_scores)

"""
The reason for writing sleep(seconds_between_turns - time() % seconds_between_turns)
instead of just sleep(seconds_between_turns) in the provided code snippet is to ensure 
that the program waits for the exact time interval specified by seconds_between_turns
without accumulating any additional delay. By subtracting the remainder of the current
time divided by seconds_between_turns, the code accounts for any time that has already 
passed within the current interval and ensures that the next action occurs precisely 
after the specified time interval.
This approach helps maintain a consistent time interval between actions in the program,
preventing any drift that might occur if the program simply waited for seconds_between_turns
without considering the time already elapsed within the current interval.
"""
