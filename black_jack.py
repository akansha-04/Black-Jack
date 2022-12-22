import random
import artblackjack
print(artblackjack.logo)
game_play=True
while game_play==True:
    play=input('Do you want to play the game type y for yes and n for no: ')
    if play=='y':
        game_play=True
    else:
        break
    cards = [10,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    usercard_1=random.choice(cards)
    usercard_2=random.choice(cards)
    user_card=[usercard_1,usercard_2]
    user_score = usercard_1+usercard_2
    print(f'Your cards are: {user_card}')
    print(f'Your score is {user_score}')
    computercard_1=random.choice(cards)
    computercard_2=random.choice(cards)
    computer_card=[computercard_1,computercard_2]
    computer_score = computercard_1+computercard_2
    print(f'Computer\'s first card: {computercard_1}')
    continue_choose=True
    while continue_choose==True:
        choice=input('Type "y" to get another card, type "n" to pass: ')
        if choice=='y':
            another_card=random.choice(cards)
            if another_card==11:
                user_score=user_score+11
                if user_score>21:
                    user_card.append(1)
                    user_score=user_score-10
                    print(f'Your cards are: {user_card}')
                    print(f'Your score is {user_score}')
                else:
                    user_card.append(11)
                    user_score=user_score
                    print(f'Your cards are: {user_card}')
                    print(f'Your score is {user_score}')
            else:
                user_card.append(another_card)
                user_score=user_score+another_card
                print(f'Your cards are: {user_card}')
                print(f'Your score is {user_score}')
        else:
            print(f'Your final hand is {user_card} ')
            continue_choose=False
    computer_continue=True
    while computer_continue==True:
        if computer_score<=16:
            another_computer_card=random.choice(cards)
            if another_computer_card==11:
                 computer_score=computer_score+11
                 if computer_score>21:
                      computer_card.append(1)
                      computer_score=computer_score-10
                 else:
                     computer_card.append(11)
                     computer_score=computer_score
            else:
                computer_card.append(another_computer_card)
                computer_score=computer_score+another_computer_card
        else:
            computer_continue=False
    print(f'Computers\'s final hand {computer_card}')
    print(f'Computer\'s final score is {computer_score}')
    if user_score>21 and computer_score<=21:
        print('You are Busted.You lose')
    elif user_score<computer_score<=21:
        print('You lose.The computer scored more')
    elif user_score==computer_score<21:
        print('Pass.Since both scored same')
    elif user_score==computer_score>21:
        print('Both lost since both are busted')
    elif user_score==21 and computer_score==21:
        print('You lose since computer got a blackjack')
    elif user_score==21 and computer_score!=21:
        print('You win since you got a blackjack')
    elif user_score<=21 and computer_score>21:
        print('You win since computer is busted')
    else:
        print('You win')

    
    