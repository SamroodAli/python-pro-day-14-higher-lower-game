# Todo 1 :import game_data,random, logo and vs
from art import logo,vs
import random
from game_data import data
from replit import clear

# Todo 2 : score, previous_a
score =0
previous_a  = None

# Todo 3 : game function
def game():
    # Todo 3.1 : clear screen and logo
    clear()
    print(logo)
# Todo 4 : assign a if not previous_A else from game data
if not previous_a:
    a= random.choice(data)
else:
    a = previous_a
print(a)
# Todo 5 : assign b
b= random.choice(data)

# Todo 6 :function greater(a,b)

# Todo 7 : recieve input

# Todo 8 : check if correct
    # Todo 8.1 : if correct, add score, update previous_a and continue game

    # Todo 8.2 : else, clear screen, print a,b and score

# Todo 9 : continue ? if yes, call game function again

game()