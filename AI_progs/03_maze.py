import math
maze=[['0','0','1','1','1'],['0','1','1','1','1'],['1','1','1','1','0'],['1','1','0','0','1'],['1','0','D','1','1']]

def main():   
    start=(0,0)
    dest=(4,2)
    vis=[]
    a_star(start,dest,vis,0)
def display(cur):
    x=cur[0]
    y=cur[1]
    for i in range(5):
        for j in range(5):
            if(i==x and y==j):
                print("  X ",end="")
            else:
                print(" ",maze[i][j]," ",end="")
        print("")
    print("________________")

def h(cur,dest):
    cx=cur[0]
    cy=cur[1]
    dx=dest[0]
    dy=dest[1]
    hval=math.sqrt((cx-dx)**2+(cy-dy)**2)
    return hval
def get_next(cur,dest,vis,g):
    moves=[]
    x=cur[0]
    y=cur[1]
    if(x>1 and maze[x-1][y]!='0'):
        moves.append((x-1,y))
    if(y>1 and maze[x][y-1]!='0'):
        moves.append((x,y-1))
    if(x<4 and maze[x+1][y]!='0'):
        moves.append((x+1,y))
    if(y<4 and maze[x][y+1]!='0'):
        moves.append((x,y+1))
    if(x>1 and y>1 and maze[x-1][y-1]!='0'):
        moves.append((x-1,y-1))
    if(x<4 and y<4 and maze[x+1][y+1]!='0'):
        moves.append((x+1,y+1))  
    l=len(moves)
    fval=[]
    mini=1000
    minind=-1
    for i in range(l):  
        fval.append(100)
    for i in range(l):
        fval[i]=g+h(moves[i],dest)
        if(fval[i]<mini and (not moves[i] in vis)):
            mini=fval[i]
            minind=i
    return moves[minind]
    
    
def a_star(cur,dest,vis,g):
    if(cur==dest):
        print("Reached!")
        #print(cur)
        display(cur)
        exit()
    display(cur)
    vis.append(cur)
    next_pos=get_next(cur,dest,vis,g)
    a_star(next_pos,dest,vis,g+1)
main()