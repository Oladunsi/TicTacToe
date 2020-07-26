from IPython.display import clear_output
import random
# this is printing of the tic-tac board
def display_board(board):
    clear_output()
    print("    |     |     |  ")
    print(" " + board[13] + "  |  "  + board[14] + "  |  "    +board[15] +  "  |  " +board[16])
    print("----------------------------")
    print("    |     |     |  ")
    print(" " + board[9] + "  |  "  + board[10] + "  |  "    +board[11] +  "  |  " +board[12])
    print("    |     |     |  ")
    print("----------------------------")
    print("    |     |     |  ")
    print(" " + board[5] + "  |  "  + board[6] + "  |  "    +board[7] + "  |  " +board[8])
    print("    |     |     |  ")
    print("----------------------------")
    print("    |     |     |  ")
    print(" " + board[1] + "  |  "  + board[2] + "  |  "    +board[3] + "  |  "  +board[4])
    print("    |     |     |  ")
# here we intend to get the input of the gamer as to who would play first and as game proceeds which when either "X" or "O" is entered it returns a tuple of both "X" and "O"
def player_input():
    marker = " "
    while not (marker == "X" or marker == "O"):
        marker = input("Enter your choice of either X or O: ").upper()
        if marker == "X":
            return ("X","O") 
        else:
            return ("O","X")
# here the place_maker just assign the input entered into position on the board in the display_board function vis. board[num] = "X" or "O"
def place_marker(board,marker,position):
    board[position] = marker
# here we are checking for the winner when an input is entered
def win_check(board,mark):
    return ((board[13]== mark and board[14]== mark and board[15]== mark and board[16]==mark)or # for top row
    (board[9]== mark and board[10]== mark and board[11]== mark and board[12]== mark)or # for 2nd top row
    (board[5]== mark and board[6]== mark and board[7]== mark and board[8]== mark) or # for 2nd bottom row
    (board[1]== mark and board[2]== mark and board[3]== mark and board[4]== mark)or # for bottom row
    (board[13]== mark and board[9]== mark and board[5]== mark and board[1]== mark) or # for first column
    (board[14]== mark and board[10]== mark and board[6]== mark and board[2]== mark)or # for 2nd column
    (board[15]== mark and board[11]== mark and board[7]== mark and board[3]== mark)or # for 3rd column
    (board[16]== mark and board[12]== mark and board[8]== mark and board[2]== mark) or # for 4th column
    (board[16]== mark and board[11]== mark and board[6]== mark and board[1]== mark)or # for diagonal 16, 11, 6, 1
    (board[13]== mark and board[10]== mark and board[7]== mark and board[4]== mark))# for diagonal 13, 10, 7, 4 

# here we are using which player is to play first where player 1 == 0  and player 1 == 1
def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1: "
    else:
        return "Player 2: "
# this function is used to check the board for empty position vis. board[position] == " "
def space_availability(board,position):
    return board[position] ==  " "
# here we will loop through the baord to chech for empty board[position] or occupied
def full_board_check(board):
    for i in range(1,17):
        if space_availability(board,i):
            return False
    return True
# here first we check if variable position is not part of the list 1-16 or is not on the space_availablity(where position is converted to int)
# then the position where the game want to place the marker would ask and it returns a int value of position
def player_choice(board):
    position = " "
    while position not in "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16".split() or not space_availability(board,int(position)):
        position = input("please Choose your next position (1-16): ")
    return int(position)
# here this function is meant to ask if the players still want to play again and if the answers start with y if convert it to a lower case
def replay():
    return input("DO you want to play again? Enter(Yes or NO): ").lower().startswith("y")

    
print("Welcome to Tic Tac Toe")
# here the program runs forever by initializing while to be true and it should carry out the following lines of code
while True: 
# this first instructions prints out the empty positions of the board
# then calls the player_input function that assigns "X" or "O" to either player1_marker or player2_marker as tuple
# then choose_first function is initialize that returns who is play first then print who's is to go first

    TheBoard = [" "]*17
    Player1_marker, Player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    # here a variable is assign a boolean value "True"    
    game_on = True
    # then a while loop is initialize on the variable assigned "True"
    while game_on:
        # here if statement is called on function choose_first which is now variable "turn" to check if "turn" is equals to "player 1"
        if turn == "Player 1: ":
            # then player 1 will have access to a printed board 
            display_board(TheBoard)
            # and can enter a number into the printed using the function player_choice 
            position = player_choice(TheBoard)
             # function place_marker is initialize to convert the position to either "X" and "O"
            place_marker(TheBoard,Player1_marker,position) 
            
            # then the win_check is initialize to check if there is a winner 
            if win_check(TheBoard,Player1_marker):
                # then display the board again and a message sayin "player 1" is the winner then gameon is assign "False"
                display_board(TheBoard)
                print("Congratulations, Player 1 has won the game")
                game_on = False
                
            else: 
                # here if the board is full and there is no winner the full_board_check is initialize to check if there is still space on the board 
                # and print the board then after print a message saing it is a "draW"
                if full_board_check(TheBoard):
                    display_board (TheBoard)
                    print("The Game is a Draw!")
                    break    
                else:
                    # else player 2 turn is initalized and then entire process from game_on is started on "player 2"
                    turn = "Player 2: "
        else:       
            # player 2 turn
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
