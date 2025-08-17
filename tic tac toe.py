import random
from colorama import Fore, init, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell=='x':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell=='O':
            return Fore.BLUE +cell +Style.RESET_ALL
        else:
            return Fore.BLUE +cell +Style.RESET_ALL
    print("  "+colored(board[0])+ ' | '+colored(board[1])+ ' | '+colored(board[2]))    
    print(Fore.CYAN +' ---------- '+ Style.RESET_ALL)
    print("  "+colored(board[3])+ ' | '+colored(board[4])+ ' | '+colored(board[5]))    
    print(Fore.CYAN +' ---------- '+ Style.RESET_ALL)
    print("  "+colored(board[6])+ ' | '+colored(board[7])+ ' | '+colored(board[8]))    
    print()
def player_choice():
    symbol=''
    while symbol not in ['X','O']    : 
        symbol=input(Fore.GREEN+"Do you want to be X or O?" +Style.RESET_ALL).upper()
    if symbol=='X':
        return('X','O') 
    else:
        return('O','X')  
def player_move(board,symbol):
    move=-1
    while move not in range(1,10) or not board[move -1].isdigit():
        try:
            move=int(input("enter your  move (1-9):"))
            if move not in range (1,10) or not board[move -1].isdigit():
                print("invalid move ... try again!")
        except ValueError:
            print("pls enter no. bw 0-9")    
    board[move -1]=symbol
def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy=board.copy()
            board_copy[i]=ai_symbol
            if check_win(board_copy,ai_symbol):
                board[i]=ai_symbol
                return
    for i in range(9):
        if board[i].isdigit() :
            board_copy=board.copy()
            board_copy[i]=player_symbol
            if check_win(board_copy,player_symbol)     :
                board[i]=ai_symbol
    possible_moves= [i for i in range(0,9) if board[i].isdigit()]        
    move=random.choice(possible_moves)    
    board[move]=ai_symbol
def check_win(board,symbol):
    win_conditions=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for cond in win_conditions:
        if board[cond[0]]==board[cond[1]]==board[cond[2]]==symbol:
            return True
    return False
def check_full(board):
    return all(not spot.isdigit() for spot in board)   
def tictactoe():
    print("welcome!")
    player_name=input(Fore.GREEN+"Enter name"+Style.RESET_ALL) 
    while True:
        board=['1','2','3','4','5','6','7','8','9']
        player_symbol,ai_symbol=player_choice()
        turn="Player"
        game_on=True
        while game_on:
            display_board(board)
            if turn=='Player':
                player_move(board,player_symbol)
                if check_win(board,player_symbol):
                    display_board(board)
                    print("congoo! "+player_name+" has won the game")
                    game_on=False
                else:
                    if check_full(board):
                        display_board(board)
                        print("its a tie")
                        break
                    else:
                        turn='AI' 
            else:
                ai_move(board, ai_symbol, player_symbol)  
                if check_win(board, ai_symbol):
                    display_board(board)
                    print("ai won")
                    game_on=False 
                else:
                    if check_full(board):
                        display_board(board)
                        print("its a tie")
                        break  
                    else:
                        turn="Player"
        play_again=input("do you wanna play again").lower()
        if play_again !="yes":
            print("bye")
            break
if __name__=="__main__":
    tictactoe()
        

                
