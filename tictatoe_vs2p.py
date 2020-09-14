#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
import random

def display_board(board):
    
    clear_output()
    
    print('_____________')
    print('|   '+'|   '+'|   '+'|')
    print('| '+board[1]+' | '+board[2]+' | '+board[3]+' |')
    print('|   '+'|   '+'|   '+'|')
    print('-------------')
    print('|   '+'|   '+'|   '+'|')
    print('| '+board[4]+' | '+board[5]+' | '+board[6]+' |')
    print('|   '+'|   '+'|   '+'|')
    print('-------------')
    print('|   '+'|   '+'|   '+'|')
    print('| '+board[7]+' | '+board[8]+' | '+board[9]+' |')
    print('|   '+'|   '+'|   '+'|')
    print('-------------')
    
    


# In[2]:


def player_input():
    marker = ''
    #Keep asking player 1 to choose X or 0    
    while marker.upper() not in ['X','0']:
        marker = input(f'{first_player},Do you want to be X or 0? ')
        
        if marker.upper() not in ['X','0']:
            print('Wrong choice, please choose between X or 0')
        else:
            pass
    #ASSING player 2 , the oposite marker
    player1 = marker.upper()
    
    if player1  == 'X':
        player2 = '0'
    else:
        player2 = 'X'
        
    return (player1,player2)


# In[3]:


def place_marker(board,maker,position):
        
    board[position] = maker


# In[4]:


def win_check(board, mark):

    row1 = board[1] == board[2] == board[3] == mark
    row2 = board[4] == board[5] == board[6] == mark
    row3 = board[7] == board[8] == board[9] == mark
    colum1 = board[1] == board[4] == board[7] == mark
    colum2 = board[2] == board[5] == board[8] == mark
    colum3 = board[3] == board[6] == board[9] == mark
    diagonal1 = board[1] == board[5] == board[9] == mark
    diagonal2 = board[3] == board[5] == board[7] == mark
    
    
    return row1 or row2 or row3 or colum1 or colum2 or colum3 or diagonal1 or diagonal2


# In[5]:


import random

def choose_first():
    if random.choice(['player1','player2']) == 'player1':
        return 'player1'
    else:
        return 'player2'


# In[6]:


def space_check(board, position):
    
    return board[position] == ' '


# In[7]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[8]:


def player_choice(board,name):
    position = input(f"{name}, please choose your position from 1 to 9 : ")
    #case of invalid input
    while position not in [str(person) for person in range(1, 10)]:
        position = input("invalid choice. Please choose a number from 1 to 9 : ")
   
    position = int(position)

    while board[position] != ' ':
        position = input("you can't go there, please try again : ") 
        while position not in [str(person) for person in range(1, 10)]:
            position = input("invalid choice. Please choose a number from 1 to 9 : ")
        position = int(position)
    
    return position

# In[10]:


def replay():
    
    answer = ''
    while answer.lower() not in ['yes', 'y', 'no','n']:
        answer = input("Would you guys like to play again(yes/y or no/n) :")
        
        if answer.lower() not in ['yes', 'y', 'no','n']:
            print("Please, choose 'yes'/'y' or 'no'/'n' :")
        elif answer.lower() in ['yes', 'y']:
            return True
        elif answer.lower() in ['no','n']:
            return False
        else:
            pass
            
        


# In[11]:


def play_game():
    
    willing = ''
    while willing.lower() not in ['yes', 'y', 'no','n']:
        willing = input("Ready to play ?(yes/y or no/n) :")
        
        if willing.lower() not in ['yes', 'y', 'no','n']:
            print("Please, choose 'yes'/'y' or 'no'/'n' :")
        elif willing.lower() in ['yes', 'y']:
            return True
        elif willing.lower() in ['no','n']:
            return False
        else:
            pass


# In[ ]:


# WHILE LOOP TO KEEP RUNNINF THE GAME


print('Welcome to Tic Tac Toe by EMERIC F. T.')

first_player = input("Player one, writes your name please: ")
second_player = input("player two, writes your name plaese: ")


while True:
    
    # PLAY THE GAME
    
    ## SET UP THE GAME(BOARD, WHO'S FIRST' CHOOSE MARKERS X,O )
    the_board = [' ']*10
    player1, player2 =  player_input()
    
    turn = choose_first()
    print (turn +' will go first')
    
    so_on = play_game()
    
    ## GAME PLAY
    while so_on:
        
        if turn == 'player1':
            
            #show the board
            display_board(the_board)
            
            print(f"this is {first_player}'s turn")
            
            #choose a position
            position = player_choice(the_board,first_player)
            
            # place the maker on the marker on the position
            place_marker(the_board,player1,position)
            
            #check if they won
            if win_check(the_board, player1):
                display_board(the_board)
                print(f'{first_player} won')
                so_on = False
            
            #or check if there is a tie 
            elif full_board_check(the_board):
                display_board(the_board)
                print("It's a tie")
                so_on = False
                
            #no tie and no win = next player's turn
            else:
                turn = 'player2'
            
    ### PLAYER ONE TURN
    
        else:
            #show the board
            display_board(the_board)
            
            print(f"this is {second_player}'s turn")
            
            #choose a position
            position = player_choice(the_board,second_player)
            
            # place the maker on the marker on the position
            place_marker(the_board,player2,position)
            
            #check if they won
            if win_check(the_board, player2):
                display_board(the_board)
                print(f'{second_player} won')
                so_on = False
            
            #or check if there is a tie 
            elif full_board_check(the_board):
                display_board(the_board)
                print("It's a tie")
                so_on = False
                
            #no tie and no win = next player's turn
            else:
                turn = 'player1'
    ### PLAYER TWO TURN
    
    
    
    if not replay():
        break
    #BREAK out of the WHILE LOOP ON replay() 
