print("WELCOME TO TIC TAC TOE GAME")


def display_board(board):
    print( board[0], '|', board[1], '|', board[2])
    print('----------')
    print( board[3], '|', board[4], '|', board[5])
    print('----------')
    print( board[6], '|', board[7], '|', board[8])


def check_win():
    if (board[0] == board[1] and board[0] == board[2]):
        return True
    elif (board[3] == board[4] and board[3] == board[5]):
        return True
    elif (board[6] == board[7] and board[6] == board[8]):
        return True
    elif (board[0] == board[3] and board[0] == board[6]):
        return True
    elif (board[1] == board[4] and board[1] == board[7]):
        return True
    elif (board[2] == board[5] and board[2] == board[8]):
        return True
    elif (board[0] == board[4] and board[0] == board[8]):
        return True
    elif (board[6] == board[4] and board[6] == board[2]):
        return True
    else:
        return False

while True:
    choice=eval(input("1) For multiplayer player mode press 1 \n2) For single player mode press 2 \n3) To exit press any other Numeric key \nEnter : "))
    n = "y"
    while n == "y":
        if choice == 1:

            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            print("Welcome to Multi_Player mode")
            display_board(board)
            print("__________________________________")
            player_1 = input("Enter player 1 name : ")
            player_2 = input("Enter player 2 name : ")
            print("__________________________________")
            print("Player 1(", player_1, ") will play as X")
            print("Player 2(", player_2, ") will play as O")
            print("__________________________________")
            player_1 = "X"
            player_2 = "O"
            while True:
                toss = eval(input("Player 1 Enter 0 for head or 1 for tails: "))
                if toss==0 or toss==1:
                    break
                else:
                    print("Please enter appropriate input..")
                    continue
            import random

            tossra = random.randint(0, 1)
            if tossra == toss:
                print("Player 1 wins the toss.")
                current_player = player_1
                second_player = player_2
            else:
                print("player 2 win the toss")
                current_player = player_2
                second_player = player_1

            count = 0
            check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            while True:
                print("____________________________________")
                if current_player == player_1:
                    print("player 1 your turn.")
                else:
                    print("Player 2 your turn.")
                while True:
                    move = int(input("Player enter your move: "))
                    if move<0 or move>9:
                        print("Please enter appropriate input!!")
                        continue
                    else:
                        break

                if move in board:
                    for i in range(9):
                        if board[i] == move:
                            board[i] = current_player
                            display_board(board)
                    a = check_win()
                    if a == True:
                        if current_player == player_1:
                            print("Congratulation Player 1 Wins.")
                        else:
                            print("Congratulation Player 2 Wins.")

                        print("     _______*********_______")
                        again = input("Enter Y to play again or ang other key to exit:")
                        if again == "y":
                            n = "y"
                            break
                        else:
                            n = "t"
                            break
                else:
                    print("Your move is already occupied!!! . Reenter please. ")
                    print("_________________________________")
                    continue
                    display_board(board)
                count += 1
                if count == 9:
                    print("Game is Draw")
                    again = input("Enter Y to play again or ang other key to exit:")
                    if again == "y":
                        n = "y"
                        break
                    else:
                        n = "t"
                        break

                print("____________________________________")
                if current_player == player_1:
                    print("player 2 your turn.")
                else:
                    print("Player 1 your turn.")
                while True:
                    move = int(input("Player enter your move: "))
                    if move<0 or move>9:
                        print("Please enter appropriate input!!")
                        continue
                    else:
                        break

                if move in board:
                    for i in range(9):
                        if board[i] == move:
                            board[i] = second_player
                            display_board(board)
                    a = check_win()
                    if a == True:
                        if current_player == player_1:
                            print("Congratulations player 2 Wins.")
                        else:
                            print("Congratulations Player 1 Wins.")

                        print("     _______*********_______")
                        again = input("Enter Y to play again or ang other key to exit:")
                        if again == "y":
                            n = "y"
                            break
                        else:
                            n = "t"
                            break

                else:
                    print("Your move is already occupied!!! . You waste your chance. ")
                    print("______________________________")
                    continue
                    display_board(board)
                count += 1
                if count == 9:
                    print("Game is Draw")
                    again = input("Enter Y to play again or ang other key to exit:")
                    if again == "y":
                        n = "y"
                        break
                    else:
                        n = "t"
                        break
        elif choice == 2:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            print("Welcome to Single_Player mode")
            display_board(board)
            print("__________________________________")

            player_1 = input("Player 1 enter your name: ")

            while True:
                symbol_1 = input("player 1 choose your symbol,either X or O: ").upper()
                if symbol_1 == "X" or symbol_1 == "O":
                    break
                else:
                    print("Please choose the right symbol!")
            print(player_1, " will play with ", symbol_1)
            player_1 = symbol_1
            print("Player 2 is Computer")
            player_2 = "Computer"
            if symbol_1 == "X":
                symbol_2 = "O"
                print(player_2, "will play with O")
                player_2 = "O"
            else:
                symbol_2 = "X"
                print(player_2, " will play with X")
                player_2 = "X"
            while True:
                toss = eval(input("Player 1 Enter 0 for head or 1 for tails: "))
                if toss==1 or toss==0:
                    break
                else:
                    print("Please enter appropriate input..")
                    continue
            import random

            tossra = random.randint(0, 1)
            if tossra == toss:
                print("Player 1 wins the toss.")
                current_player = player_1
                second_player = player_2
            else:
                print("player 2 win the toss")
                current_player = player_2
                second_player = player_1

            count = 0
            check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            while True:
                print("____________________________________")
                if current_player == player_1:
                    print("player 1 your turn.")
                    while True:
                        move = int(input("Player 1 enter your move: "))
                        if move < 0 or move > 9:
                            print("Please appropriate input!!")
                            continue
                        else:
                            break

                else:
                    print("Computer's turn.")
                    while True:
                        import random

                        move = random.randint(1, 10)
                        if move in board:
                            break
                        else:
                            continue

                if move in board:
                    for i in range(9):
                        if board[i] == move:
                            board[i] = current_player
                            display_board(board)
                    a = check_win()
                    if a == True:
                        if current_player == player_1:
                            print("Congratulation Player 1  Wins.")
                        else:
                            print("Computer Wins!!!!")

                        print("     _______*********_______")
                        again = input("Enter Y to play again or ang other key to exit:")
                        if again == "y":
                            n = "y"
                            break
                        else:
                            n = "t"
                            break
                else:
                    print("Your move is already occupied!!! . Reenter please. ")
                    print("_________________________________")
                    continue
                    display_board(board)
                count += 1
                if count == 9:
                    print("Game is Draw")
                    again = input("Enter Y to play again or ang other key to exit:")
                    if again == "y":
                        n = "y"
                        break
                    else:
                        n = "t"
                        break

                print("____________________________________")
                if current_player == player_1:
                    print("Computer's turn.")
                    while True:
                        import random

                        move = random.randint(1, 10)
                        if move in board:
                            break
                        else:
                            continue

                else:
                    print("player 1 your turn.")
                    while True:
                        move = int(input("Player enter your move: "))
                        if move<0 or move>9:
                            print("PLease enter appropriate input!!!")
                            continue
                        else:
                            break
                if move in board:
                    for i in range(9):
                        if board[i] == move:
                            board[i] = second_player
                            display_board(board)
                    a = check_win()
                    if a == True:
                        if current_player == player_1:
                            print("Congratulations Computer Wins.")
                        else:
                            print("Congratulations Player 1 Wins.")

                        print("     _______*********_______")
                        again = input("Enter Y to play again or ang other key to exit:")
                        if again == "y":
                            n = "y"
                            break
                        else:
                            n = "t"
                            break

                else:
                    print("Your move is already occupied!!! . You waste your chance. ")
                    print("______________________________")
                    continue
                    display_board(board)
                count += 1
                if count == 9:
                    print("Game is Draw")
                    again = input("Enter Y to play again or ang other key to exit:")
                    if again == "y":
                        n = "y"
                        break
                    else:
                        n = "t"
                        break