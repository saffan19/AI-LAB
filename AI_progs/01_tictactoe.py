import random
from typing import Coroutine

def main():
    board=[['','',''],['','',''],['','','']]
    print("You are X and computer is O")
    i=0
    while True:
        display(board)
        if(check_full(board)):
            print("DRAW")
            exit()
        if(i%2==0):
            print("Enter row and col:")
            row=int(input())
            col=int(input())
            if(board[row][col]!=''):
                print("Invalid input..try again")
                continue
            board[row][col]='X'
            if(check_won(board)):
                print("YOU WON")
                display(board)
                exit()
        else:
            row=random.randint(0,2)
            col=random.randint(0,2)
            if(board[row][col]!=''):
                continue
            board[row][col]='O'
            if(check_won(board)):
                print("YOU LOST!")
                display(board)
                exit()
        i=i+1

def display(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" | ")
        print("\n----------")


def check_full(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]==''):
                return False
    return True

def check_won(board):
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][2]!=''):
            return True
        if(board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[2][i]!=''):
            return True
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]!=''):
        return True
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]!=''):
        return True
    return False


main()
