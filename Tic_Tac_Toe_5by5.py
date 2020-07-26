from IPython.display import clear_output
import random
def display_board(board):
    clear_output()
    print("    |     |     |    |   ")
    print(" " + board[21] + "  |  "  + board[22] + "  |  "    +board[23] +  "  |  " +board[24] + "  |  "  +board[25])
    print("----------------------------")
    print("    |     |     |    |   ")
    print(" " + board[16] + "  |  "  + board[17] + "  |  "    +board[18] +  "  |  " +board[19] + "  |  "  +board[20])
    print("----------------------------")
    print("    |     |     |    |   ")
    print(" " + board[11] + "  |  "  + board[12] + "  |  "    +board[13] +  "  |  " +board[14] + "  |  "  +board[15])
    print("    |     |     |    |   ")
    print("----------------------------")
    print("    |     |     |    |   ")
    print(" " + board[6] + "  |  "  + board[7] + "  |  "    +board[8] + "  |  " +board[9] + "  |  "  +board[10])
    print("    |     |     |    |   ")
    print("----------------------------")
    print("    |     |     |    |   ")
    print(" " + board[1] + "  |  "  + board[2] + "  |  "    +board[3] + "  |  "  +board[4] + "  |  "  +board[5])
    print("    |     |     |    |   ")

def player_input():
    marker = " "
    while not (marker == "X" or marker == "O"):
        marker = input("Enter your choice of either X or O: ").upper()
        if marker == "X":
            return ("X","O") 
        else:
            return ("O","X")

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return ((board[21]== mark and board[22]== mark and board[23]== mark and board[24]== mark and board[25]== mark)or # for top row
    (board[16]== mark and board[17]== mark and board[18]== mark and board[19]== mark and board[20]== mark)or # for 2nd top row
    (board[11]== mark and board[12]== mark and board[13]== mark and board[14]== mark and board[15]== mark)or # for third top
    (board[6]== mark and board[7]== mark and board[8]== mark and board[9]== mark and board[10]== mark) or # for 2nd bottom row
    (board[1]== mark and board[2]== mark and board[3]== mark and board[4]== mark and board[5]== mark)or # for bottom row
    (board[21]== mark and board[16]== mark and board[11]== mark and board[6]== mark and board[1]== mark) or # for first column
    (board[22]== mark and board[17]== mark and board[2]== mark and board[7]== mark and board[2]== mark)or # for 2nd column
    (board[23]== mark and board[18]== mark and board[13]== mark and board[9]== mark and board[4]== mark)or # for 3rd column
    (board[25]== mark and board[20]== mark and board[15]== mark and board[10]== mark and board[5]== mark) or # for 4th column
    (board[25]== mark and board[19]== mark and board[13]== mark and board[7]== mark and board[1]== mark)or # for diagonal 25, 19, 13, 7, 1
    (board[21]== mark and board[17]== mark and board[13]== mark and board[9]== mark and board[5]== mark))# for diagonal 21, 17, 13, 9, 5 

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1: "
    else:
        return "Player 2: "

def space_availability(board,position):
    return board[position] ==  " "

def full_board_check(board):
    for i in range(1,26):
        if space_availability(board,i):
            return False
    return True

def player_choice(board):
    position = " "
    while position not in "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25".split() or not space_availability(board,int(position)):
        position = input("please Choose your next position (1-25): ")
    return int(position)

def replay():
    return input("DO you want to play again? Enter(Yes or NO): ").lower().startswith("y")

    
print("Welcome to Tic Tac Toe")

while True: 

    TheBoard = [" "]*26
    Player1_marker, Player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    
    game_on = True
    
    while game_on:
        
        if turn == "Player 1: ":
            #player 1 turn
            display_board(TheBoard)
            position = player_choice(TheBoard)
            place_marker(TheBoard,Player1_marker,position) 
            
            
            if win_check(TheBoard,Player1_marker):
                display_board(TheBoard)
                print("Congratulations, Player 1 has won the game")
                game_on = False
                
            else: 
                if full_board_check(TheBoard):
                    display_board (TheBoard)
                    print("The Game is a Draw!")
                    break    
                else:
                    turn = "Player 2: "
        else:       
            #player 2 turn
            display_board(TheBoard)
            position = player_choice(TheBoard)
            place_marker(TheBoard,Player2_marker,position)
            
            if win_check(TheBoard,Player2_marker):
                display_board(TheBoard)
                print("Congratulations, Player 2 has won the game")
                game_on = False
                
            else: 
                if full_board_check(TheBoard):
                    display_board (TheBoard)
                    print("The Game is a Draw!")
                    break    
                else:
                    turn = "Player 1: "
    
    if not replay():
        break 
