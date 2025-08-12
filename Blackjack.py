import random

def pick_card():
    deck = {'Q':10, 'K':10, 'J':10, 'A':11, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    rand_card = random.choice(list(deck.keys()))
    value_card = deck[rand_card]
    return (rand_card, value_card)

def player():
    hand = []
    total = 0
    blackjack = check_blackjack(hand)
    num = 3
    while num == 3:
        p_input=input("Would you like to play? (Y)/(N): ")

        if p_input == 'Y':
            cards = pick_card()
            hand.append(cards)
            for card, c_value in hand:
                print(f"({c_value})")

            total += c_value
            print(total)

            if check_blackjack(hand) == True:
                print("You've got Blackjack!")
            

            if check_bust(total): #We check whether the player has gone bust, while they're still playing
                print(f"(({total})) You've gone bust!")
                break

        elif p_input == 'N':
            print(f"Your total is: {total}")
            total += c_value
            break
        else:
            print("Please pick y or n")



def check_bust(total):
    return total >= 22

def check_blackjack(hand):

    ten_cards = {'10', 'K', 'Q', 'J'}

    if len(hand) == 2 and ((hand[0][0] == 'A' and hand [1][0] in ten_cards) or (hand[1][0] == 'A' and hand[0][0] in ten_cards)):

        return True
    else:
        return False


    
            

play = player()

