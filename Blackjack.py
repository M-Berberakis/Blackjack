import random

def pick_card():

    deck = {'Q':10, 'K':10, 'J':10, 'A':11, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    rand_card = random.choice(list(deck.keys()))
    value_card = deck[rand_card]
    print(f"{rand_card} ({value_card})")






    
    
    
    
            









