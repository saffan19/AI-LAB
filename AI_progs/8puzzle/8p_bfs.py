def main():
    goal=[1,2,3,4,5,6,7,8,-1]
    start=[1,2,3,4,-1,6,7,5,8]
    vis=[]
    bfs(start,goal,vis)


def bfs(cur,goal,vis):
    if(cur==goal):
        display(cur)
        print("GOAL REACHED!")
        exit()
    queue=[]
    queue.append(cur)
    while(len(queue)!=0):
        t=queue.pop(0)
        if(t==goal):
            print("GOAL REACHED")
            display(t)
            exit()
        display(t)
        vis.append(t)
        next_states=gen_state(t)
        for state in next_states:
            if(not state in vis):
                queue.append(state)
def find_space(cur):
    for i in range(9):
        if(cur[i]==-1):return i
    return -1
def gen_state(cur):
    ind=find_space(cur)
    moves=[]
    if(ind>2):
        moves.append('u')
    if(ind<6):
        moves.append('d')
    if(ind%3 !=0):
        moves.append('l')
    if(ind%3 !=2):
        moves.append('r')
    next_state=[]
    for move in moves:
        t=create_move(cur,move,ind)
        next_state.append(t)
    return next_state
def create_move(cur,move,ind):
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

def display(cur):
    for i in range(9):
        if(i%3==0):print('')
        print(cur[i],end=" ")
    print("\n--------------------")
main()
        