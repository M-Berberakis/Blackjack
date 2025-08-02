import random

def pick_card():
    deck = {'Q':10, 'K':10, 'J':10, 'A':11, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    rand_card = random.choice(list(deck.keys()))
    value_card = deck[rand_card]
    return rand_card, value_card

def player():
    total = 0
    while True:
        p_input=input("Would you like to play? (Y)/(N): ")

        if p_input == 'Y':
            card, c_value = pick_card()
            print(f"{card} ({c_value})")
            total += c_value
            

        elif p_input == 'N':
            print("Ok, cya!")
            return total
        else:
            print("Please pick y or n")

def check_bust():
    #Uses total value to check whether the player has
    #gone bust or not
            

play = player()







    
    
    
    
            









