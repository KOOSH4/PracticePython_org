i = 1

def new_game_function():
    new_game = input("Do you want to start a new game? (Y)es (N)o ")
    if new_game.lower() == "n":
        return 1
    else:
        return 0

while i < 2:
    player1 = input("Player1: (R)ock, (P)aper or (S)cissors? ")
    player2 = input("Player2: (R)ock, (P)aper or (S)cissors? ")
    player1 = player1.lower()
    player2 = player2.lower()
    if player1 == "r" and player2 == "s":
        print("Player 1 beats player 2!")
        if new_game_function():
            break
    elif player1 == "s" and player2 == "p":
        print("Player 1 beats player 2!")
        if new_game_function():
            break
    elif player1 == "p" and player2 == "r":
        print("Player 1 beats player 2!")
        if new_game_function():
            break
    else:
        print("Player 2 beats player 1!")
        if new_game_function():
            break
