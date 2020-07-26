from IPython.display import clear_output
import random
def display_board(board):
    clear_output()
   
    print("    |     |   ")
    print(" " + board[7] + "  |  "  + board[8] + "  |  "    +board[9])
    print("    |     |   ")
    print("----------------")
    print("    |     |   ")
    print(" " + board[4] + "  |  "  + board[5] + "  |  "    +board[6]) 
    print("    |     |   ")
    print("----------------")
    print("    |     |   ")
    print(" " + board[1] + "  |  "  + board[2] + "  |  "    +board[3])
    print("    |     |   ")

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
    return ((board[7]== mark and board[8]== mark and board[9]== mark)or # for top row
    (board[6]== mark and board[5]== mark and board[4]== mark)or # for third top
    (board[1]== mark and board[2]== mark and board[3]== mark) or # for bottom row
    (board[7]== mark and board[4]== mark and board[1]== mark)or # for first column
    (board[8]== mark and board[5]== mark and board[2]== mark) or # for 2nd middle column
    (board[9]== mark and board[6]== mark and board[3]== mark)or # for last column
    (board[7]== mark and board[5]== mark and board[3]== mark )or # for diagonal ,5,3 column
    (board[9]== mark and board[5]== mark and board[1]== mark))# for diagonal 8,5,1 column

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1: "
    else:
        return "Player 2: "

def space_availability(board,position):
    return board[position] ==  " "

def full_board_check(board):
    for i in range(1,10):
        if space_availability(board,i):
            return False
    return True

def player_choice(board):
    position = " "
    while position not in "1 2 3 4 5 6 7 8 9".split() or not space_availability(board,int(position)):
        position = input("please Choose your next position (1-9): ")
    return int(position)

def replay():
    return input("DO you want to play again? Enter(Yes or NO): ").lower().startswith("y")

    
print("Welcome to Tic Tac Toe")

while True: 

    TheBoard = [" "]*10
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
