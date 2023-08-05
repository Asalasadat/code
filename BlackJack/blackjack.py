import random
def deal_cards():
    """Returns a random card"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    rand_card=random.choice(cards)
    return rand_card

def calcu_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 


def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw!"
    elif computer_score==0:
        return "Lose, oppenent has BlackJack"
    elif user_score==0:
        return "Win with BlackJack"
    elif user_score>21:
        return "You went over. You lose"
    elif computer_score >21:
        return "Oppenent went over. You wine"
    elif user_score>computer_score:
        return "You win"
    else:
        "You lose"


def play_game():
    user_cards=[]
    copmuter_cards=[]

    game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        copmuter_cards.append(deal_cards())

    while not game_over:
        user_score=calcu_score(user_cards)
        copmuter_score=calcu_score(copmuter_cards)

        print(f" Your cards: {user_cards}, current score: {user_score} ")
        print(f" computer is first card: {copmuter_cards[0]}")

        if user_score==0 or copmuter_score==0 or user_score>21:
            game_over=True
        else:
            flag = input("Type 'Y' to get another card, Type 'X' to pass: ").lower()    
            if flag=='y':
                user_cards.append(deal_cards())
            else:
                game_over=True
                
    while copmuter_score!=0 and copmuter_score<17:
        copmuter_cards.append(deal_cards()) 
        copmuter_score = calcu_score(copmuter_cards)           
        
    print("Your final hand {user_cards}, final score : {user_score}")    
    print("Computer is final hand {copmuter_cards}, final score : {copmuter_score}")    

    print(compare(user_score,copmuter_score))    

while input("Do you want to play a game of BlackJack? Type 'Y' or 'n'").lower()=="y":
    play_game()
    