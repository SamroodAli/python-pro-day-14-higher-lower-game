# Todo 1 :import game_data,random, logo and vs
from art import logo,vs
import random
from game_data import data
from replit import clear

# Todo 2 : score, previous_b
score =0
previous_b  = None
def higher_or_lower_game(score,previous_b):
    # Todo 3.1 : clear screen and logo
    clear()
    print(logo)
    # Todo 3 : game function
    def game(score,previous_b):
    # Todo 5 : assign b
        if not previous_b:
            a= random.choice(data)
        else:
            a = previous_b
    # Todo 4 : assign a if not previous_b else from game data
        b= random.choice(data)
        while a == b:
            b = random.choice(data)
    # Todo 6 :function greater(a,b)
        def greater(a,b):
            if a['follower_count'] > b['follower_count']:
                return 'a'
            else:
                return 'b'
        greater = greater(a,b)
    # Todo 7:print a and b
        print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']}, a {b['description']} from {b['country']}")
    # Todo 8 : recieve input
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Todo 9 : check if correct
        # Todo 9.1 : if correct, add score, update previous_b and continue game
        if user_input == greater:
            print("You are correct")
            score += 1
            print(f"score: {score}")
            previous_b = b
            return (score,previous_b)
        # Todo 9.2 : else, clear screen, print a,b and score
        else:
            print("You are wrong")
            print(f"score: {score}")
            score = 0
            previous_b=None
            return (score,previous_b)
        
    score , previous_b = game(score,previous_b)
    # print score
    # Todo 10 : continue ? if yes, call game function again
    continue_playing = input("Do you want to continue playing ? y for yes:  ").lower()
    if continue_playing =='y':
        return higher_or_lower_game(score,previous_b)
# game launch
higher_or_lower_game(score,previous_b)