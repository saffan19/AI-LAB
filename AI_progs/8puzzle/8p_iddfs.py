def main():
    goal=[1,2,3,4,5,6,7,8,-1]
    start=[1,2,3,4,-1,6,7,5,8]
    vis=[]
    print("Enter the limit:")
    lim=int(input())
    iddfs(start,goal,vis,lim)
    print("GOAL NOT REACHABLE within limit")

def iddfs(start,goal,vis,lim):
    for i in range(1,lim):
        vis=[]
        dfs(start,goal,vis,i)
def dfs(cur,goal,vis,i):
    
    if(i==0):
        return
    if(cur==goal):
        display(cur)
        print("\nGOAL REACHED within limit!!")
        exit()
    vis.append(cur)
    display(cur)
    next_states=gen_state(cur)
    #print(next_states)
    for state in next_states:
        if(not state in vis):
            dfs(state,goal,vis,i-1)
def display(cur):
    print("\n------------------")
    for i in range (9):
        if(i%3==0):
            print("")
        print(cur[i],end=" ")

def gen_state(cur):
    ind=find_space(cur)
    
    moves=[]
    if ind < 6:
        moves.append('d')
    if(ind % 3!=2):
        moves.append('r')
    if ind > 2:
        moves.append('u')
    if ind % 3 !=0:
        moves.append('l')


    next_states=[]
    for move in moves:
        temp=create_state(cur,move,ind)
        next_states.append(temp)
    return next_states


def create_state(cur,move,ind):
    c=cur[:]
    if(move=='u'):
        c[ind],c[ind-3]=c[ind-3],c[ind]
    if(move=='d'):
        c[ind],c[ind+3]=c[ind+3],c[ind]
    if(move=='r'):
        c[ind],c[ind+1]=c[ind+1],c[ind]
    if(move=='l'):
        c[ind],c[ind-1]=c[ind-1],c[ind]
    return c


def find_space(cur):
    for i in range(9):
        if(cur[i]==-1):return i
    return -1
main()