import random
def display(board):
    print("\n   1  2  3  4\n")
    print("1  ",board[0][0],"  ",board[0][1],"  ",board[0][2])
    print("2  ",board[1][0],"  ",board[1][1],"  ",board[1][2])
    print("3  ",board[2][0],"  ",board[2][1],"  ",board[2][2])
    
def check_if_full(board):
    for i in board:
        for k in i:
            if(k==''):
                return False
    return True

def check_if_won(board):
    #Rows
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][2]!=''):
            return True
    return False

    #Col
    for i in range(3):
        if(board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[2][i]!=''):
            return True
    return False
    #Diag
    if(board[0][0]==board[1][1]and board[1][1]==board[2][2]and board[2][2]!=''):
        return True
    if(board[0][3]==board[2][2]and board[2][2]==board[3][1] and board[3][1]!=''):
        return True
    

def main():
    board=[
        ['','',''],
        ['','',''],
        ['','',''],
    ]
    print("You are X and computer is O")
    p=['X','O']
    for i in range(9):
        display(board)
        if(check_if_full(board)):
            print("Tie")
        if(i%2==0):
            print("Your turn:")
            print("Enter row and columns:")
            row=int(input())
            column=int(input())
            if(board[row-1][column-1]==''):
                board[row-1][column-1]='X'
            else:
                print("Wrong input!")
            if check_if_won(board):
                display(board)
                print("You won!!")
                break
        else:
            row=random.randint(0,2)
            column=random.randint(0,2)
            while(board[row][column]!=''):
                row=random.randint(0,2)
                column=random.randint(0,2)
            board[row][column]='O'
            if check_if_won(board):
                display(board)
                print("Computer won!!")
                break
main()

