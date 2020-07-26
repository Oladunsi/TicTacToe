from IPython.display import clear_output
import random
# this is printing of the tic-tac board
theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ' ,
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def display_board(theboard):
    clear_output()
    print(  "" +  theboard['top-L'] + " |" + " " +  theboard['top-M'] + " "  + "|" + theboard['top-R'] )
    print("--+---+--")
    print( "" +  theboard['mid-L'] + " |" + " " + theboard['mid-M'] + " " + "|" + theboard['mid-R'] )
    print("--+---+--")
    print( "" + theboard['low-L'] + " |" + " " +  theboard['low-M'] + " " +  "|" + theboard['low-R'] )
print(display_board)   
    

# here we intend to get the input of the gamer as to who would play first and as game proceeds which when either "X" or "O" is entered it returns a tuple of both "X" and "O"
def player_input():
    marker = " "
    while not (marker == "X" or marker == "O"):
        marker = input("Enter your choice of either X or O: ").upper()
        if marker == "X":
            return ("X","O") 
        elif marker == "O":
            return ("O","X")
        else:
            print("invalid Entry")

# here we are using which player is to play first where player 1 == 0  and player 1 == 1
def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1: "
    else:
        return "Player 2: "

# here the place_maker just assign the input entered into position on the board in the display_board function vis. board[num] = "X" or "O"
def place_marker(theboard,marker,position):
    theboard[position] = marker
    #print(theboard[position])
    return theboard[position]

# here we are checking for the winner when an input is entered
def win_check(theboard,mark):
    return ((theboard['top-L']== mark and theboard['top-M']== mark and theboard['top-R']== mark)or # for top row
    (theboard['mid-L']== mark and theboard['mid-M']== mark and theboard['mid-R']== mark)or # for mid row
    (theboard['low-L']== mark and theboard['low-M']== mark and theboard['low-R']== mark) or # for bottom row
    (theboard['top-L']== mark and theboard['mid-L']== mark and theboard['low-L']== mark)or # for first column 
    (theboard['top-M']== mark and theboard['mid-M']== mark and theboard['low-M']== mark) or # for 2nd column 
    (theboard['top-R']== mark and theboard['mid-R']== mark and theboard['low-R']== mark)or # for 3rd column
    (theboard['top-L']== mark and theboard['mid-M']== mark and theboard['low-R']== mark)or # for diagonal top-l,mid-M, buttom-R
    (theboard['low-L']== mark and theboard['mid-M']== mark and theboard['top-R']== mark)) # for diagonal top-R,mid-M, buttom-l
   


# this function is used to check the board for empty position vis. board[position] == " "
def space_availability(theboard,position):
    return theboard[position] ==  " "

# here we will loop through the baord to chech for empty board[position] or occupied
def full_board_check(theboard):
    for i in theboard.keys():
        if theboard[i] == " " and not space_availability(theboard,position):
            return False
    return True

# here first we check if variable position is not part of the list 1-16 or is not on the space_availablity(where position is converted to int)
# then the position where the game want to place the marker would ask and it returns a int value of position
def player_choice(theboard):
    #position = " "
    position = input("please Choose your next position from (top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R): ")
    while position not in "top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R".split() or not space_availability(theboard,position):
        position = input("please Choose your next position from (top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R): ")
        if position in "top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R".split() and not space_availability(theboard,position):
            return position
    else:
        return position
        #newposition = input("please Choose your next position from (top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R): ")
        #if newposition in "top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R".split() or not space_availability(theboard,newposition):
            #return newposition
        #else:
            #continue

# here this function is meant to ask if the players still want to play again and if the answers start with y if convert it to a lower case
def replay():
    return input("DO you want to play again? Enter(Yes or NO): ").lower().startswith("y")

    
print("Welcome to Tic Tac Toe")
# here the program runs forever by initializing while to be true and it should carry out the following lines of code

while True: 
    theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ' ,
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# this first instructions prints out the empty positions of the board
# then calls the player_input function that assigns "X" or "O" to either player1_marker or player2_marker as tuple
# then choose_first function is initialize that returns who is play first then print who's is to go first


    start = True
    while start:
        turn = choose_first()
        Player1_marker, Player2_marker = player_input()
        choice = (Player1_marker,Player2_marker)
        if choice not in (("X","O"), ("O","X")):
            print(player_input())
        
        else:
            if (choice == ("X","O") and turn == "Player 1: " ):
                display_board(theboard)
                choice = choice #("X","O")
                print(f"{Player1_marker} will go first as")
                start = False
                break
            elif (choice == ("O","X") and turn == "Player 2: "):
                display_board(theboard)
                choice = Player1_marker,Player2_marker #("O","X")
                print(f"{Player1_marker} will go first:")
                start = False
                break
            elif (choice == ("O","X") and turn == "Player 1: "):
                display_board(theboard)
                choice = Player1_marker,Player2_marker  #("O","X")
                print(f"{Player1_marker} will go first :")
                start = False
                break
            elif (choice == ("X","O") and turn == "Player 2: "):
                display_board(theboard)
                choice = Player1_marker,Player2_marker #("X","O")
                print(f"{Player1_marker} will go first : ")
                #print("issues been dey here before!!!!!!")
                start = False
                break
            else:
                start = True
        start = False
        display_board(theboard)
        break


    # here a variable is assign a boolean value "True"    
    game_on = True
    # then a while loop is initialize on the variable assigned "True"
    while game_on:
        # here if statement is called on function choose_first which is now variable "turn" to check if "turn" is equals to "player 1"
        if choice == ("X","O"):
            # then player 1 will have access to a printed board 
            display_board(theboard)
            print(f"{Player1_marker} is now playing")
            # and can enter where to place the marker on the board using the function player_choice 
            position = player_choice(theboard)
            if position in "top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R".split():
                # function place_marker is initialize to convert the position to either "X" and "O"
                place_marker(theboard,Player1_marker,position)
                 
                # then the win_check is initialize to check if there is a winner 
                if win_check(theboard,Player1_marker):
                    # then display the board again and a message sayin "player 1" is the winner then gameon is assign "False"
                    display_board(theboard)
                    print(f"Congratulations, {Player1_marker} has won the game")
                    game_on = False
                    break

                else: 
                    # here if the board is full and there is no winner the full_board_check is initialize to check if there is still space on the board 
                    # and print the board then afteR (a message saing it is a "draW")
                    if full_board_check(theboard) == True:
                        display_board (theboard)
                        print("The Game is a Draw!")
                        game_on = False
                        break    
                    else:
                        # else player 2 turn is initalized and then entire process from game_on is started on "player 2"
                        choice = ("O","X")
        else:       
            # player 2 turn
            display_board(theboard)
            print(f"{Player2_marker} is now playing")
            position = player_choice(theboard)
            if position in "top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R".split():
                place_marker(theboard,Player2_marker,position)

                if win_check(theboard,Player2_marker):
                    display_board(theboard)
                    print(f"Congratulations, {Player2_marker} has won the game")
                    game_on = False
                    break
                
                else: 
                    if full_board_check(theboard) == True:
                        display_board (theboard)
                        print("The Game is a Draw!")
                        game_on = False
                        break    
                    else:
                        choice = ("X","O")

    if not replay():
        break 
