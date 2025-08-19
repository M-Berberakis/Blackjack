import random
import time

def pick_card():
    deck = {'Q':10, 'K':10, 'J':10, 'A':11, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    rand_card = random.choice(list(deck.keys()))
    value_card = deck[rand_card]
    return (rand_card, value_card)

def player():
    hand = []
    total = 0
    num = 3
    while num == 3:
        p_input=input("Would you like to play? (Y)/(N): ")

        if p_input == 'Y':
            cards = pick_card()
            hand.append(cards)
            
            total += cards[1]

            print(f"Player drew: {cards[0]}")
            print(f"Player total is: {total}")
            

        if p_input == 'N':
            if total == 0:
                break
            else:
                print(f"Player total is: {total}")
                break

        
        if check_bust(total):
            break

    return hand, total



def check_bust(total):

    if total >= 22:
        return True
    else:
        return False


def check_blackjack(hand):

    ten_cards = {'10', 'K', 'Q', 'J'}

    if len(hand) == 2 and ((hand[0][0] == 'A' and hand [1][0] in ten_cards) or (hand[1][0] == 'A' and hand[0][0] in ten_cards)):

        return True
    else:
        return False
    
def check_push(dealer_total, player_total):

    if not check_bust(dealer_total) and not check_bust(player_total):
        return dealer_total == player_total
    else:
        return False
    

def check_winner(dealer_total, player_total, dealer_hand, player_hand):

    if dealer_total == 21 and check_blackjack(dealer_hand) == True: #This works because the dealer_turn function can see the dealer hand. ADD THESE AS THE MAIN IF STATEMENT
        print("The Dealer has Blackjack!")

    elif not check_bust(dealer_total) == True and dealer_total > player_total:
        print(f"The Player has lost with {player_total}, the Dealer wins with: {dealer_total}")

    if player_total == 21 and check_blackjack(player_hand) == True: #This does not work because the dealer_turn function cannot see the player's hand. NEED TO FIX
        print("The Player has Blackjack!")

    elif not check_bust(player_total) == True and player_total > dealer_total:
        print(f"The Dealer has lost with {dealer_total} The Player wins with: {player_total} ")

    if player_total == 21 and check_blackjack(player_hand) == True and dealer_total == 21 and check_blackjack(dealer_hand) == True:
        print("Both the Player and the Dealer have Blackjack, the bet is pushed!")

    if check_push(dealer_total, player_total) == True:
        print(f"The Dealer has: ({dealer_total}) and the Player has: ({player_total}), the bet is pushed!")

    if check_bust(dealer_total) == True and check_bust(player_total) == False:
        print("The Dealer has gone bust, the Player wins ")

    elif check_bust(player_total) == True and check_bust(dealer_total) == False:
        print("The Player has gone bust, the Dealer wins")

    

    
    


def dealerTurn(player_total, player_hand):
    dealer_hand=[]
    dealer_total = 0

    print("DEALER'S TURN")
    

    while dealer_total < 17:
        Dcards = pick_card()
        dealer_hand.append(Dcards)

        dealer_total += Dcards[1]

        print("Dealer is drawing: ")
        time.sleep(1)

        print(f"The Dealer drew: {Dcards[0]})")
        print(f"Dealer total: (({dealer_total}))")
        

    # if check_push(dealer_total, player_total):
    #     print("The bet is pushed")


    winner = check_winner(dealer_total, player_total, dealer_hand, player_hand)
    print(winner)

 

player_hand,player_total = player() 
dealer = dealerTurn(player_total, player_hand)
          



