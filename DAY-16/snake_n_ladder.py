import random

def dice():
    return random.randint(1,6)

player_1 = input("Enter the player-1: ")
player_2 = input("Enter the player-2: ")

player1_score, player2_score = 0, 0

winning_point = 100

ladders = {6:25,12:31,35:90,46:60,51:74,78:99,82:96}
snakes = {24:5,45:18,66:33,74:37,88:77,93:57,98:21}

while player1_score < winning_point and player2_score < winning_point:

    # -------- Player 1 --------
    status1 = input(f"{player_1} : [P]lay or [Q]uit: ").lower()

    if status1 == 'p':
        dice_1 = dice()
        print(f'Dice Score: {dice_1}')

        player1_score += dice_1

        if player1_score > winning_point:
            player1_score -= dice_1
        elif player1_score in ladders:
            player1_score = ladders[player1_score]
            print(f'+++++ Ladder - Board Score: {player1_score}')
        elif player1_score in snakes:
            player1_score = snakes[player1_score]
            print(f'----- Snake Bite - Board Score: {player1_score}')
        else:
            print(f'Board Score: {player1_score}')

    elif status1 == 'q':
        print(f'********* {player_2} won the game')
        break
    else:
        print("Enter valid input")

    # -------- Player 2 --------
    status2 = input(f"{player_2} : [P]lay or [Q]uit: ").lower()

    if status2 == 'p':
        dice_2 = dice()
        print(f'Dice Score: {dice_2}')

        player2_score += dice_2

        if player2_score > winning_point:
            player2_score -= dice_2
        elif player2_score in ladders:
            player2_score = ladders[player2_score]
            print(f'+++++ Ladder - Board Score: {player2_score}')
        elif player2_score in snakes:
            player2_score = snakes[player2_score]
            print(f'----- Snake Bite - Board Score: {player2_score}')
        else:
            print(f'Board Score: {player2_score}')

    elif status2 == 'q':
        print(f'********* {player_1} won the game')
        break
    else:
        print("Enter valid input")

# -------- Winner --------
if player1_score == winning_point:
    print(f'{player_1} won the game')
elif player2_score == winning_point:
    print(f'{player_2} won the game')

'''
another logic-


if(player1_score+dice_1)<winning_point:
    elif (player1_score+dice_1) = winning_point:
        break

'''
import random

player1 = input("Enter Player 1: ")
player2 = input("Enter Player 2: ")

player1_score = 0
player2_score = 0

winning_point = 100

# simple snakes & ladders
ladders = {4:14, 8:30}
snakes = {17:7, 28:12}

while player1_score < winning_point and player2_score < winning_point:

    # -------- Player 1 --------
    input(player1 + " press Enter to roll dice")
    dice_1 = random.randint(1,6)
    print("Dice:", dice_1)

    if (player1_score + dice_1) < winning_point:
        player1_score += dice_1

    elif (player1_score + dice_1) == winning_point:
        player1_score += dice_1
        print(player1, "reached 100 and wins!")
        break

    else:
        print("Need exact number to win")

    # check ladder
    if player1_score in ladders:
        print("Ladder!")
        player1_score = ladders[player1_score]

    # check snake
    elif player1_score in snakes:
        print("Snake!")
        player1_score = snakes[player1_score]

    print(player1, "Score:", player1_score)

    # -------- Player 2 --------
    input(player2 + " press Enter to roll dice")
    dice_2 = random.randint(1,6)
    print("Dice:", dice_2)

    if (player2_score + dice_2) < winning_point:
        player2_score += dice_2

    elif (player2_score + dice_2) == winning_point:
        player2_score += dice_2
        print(player2, "reached 100 and wins!")
        break

    else:
        print("Need exact number to win")

    # check ladder
    if player2_score in ladders:
        print("Ladder!")
        player2_score = ladders[player2_score]

    # check snake
    elif player2_score in snakes:
        print("Snake!")
        player2_score = snakes[player2_score]

    print(player2, "Score:", player2_score)
