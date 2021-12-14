def main():
    goal=[1,2,3,4,5,6,7,8,-1]
    start=[1,-1,3,4,2,6,7,5,8]
    vis=[]
    a_star(start,goal,vis,1)


def a_star(cur,goal,vis,g):
    #if(len(vis)==10):exit()
    if(cur==goal):
        display(cur)
        print("GOAL REACHED")
        exit()
    display(cur)
    vis.append(cur)
    next_states=gen_state(cur)
    min_ind=find_index(next_states,goal,g,vis)
    a_star(next_states[min_ind],goal,vis,g)

def h(cur,goal):
    count=0
    for i in range(9):
        if(cur[i]!=goal[i] and cur[i]!=-1):
            count=count+1
    return count

def find_index(next_states,goal,g,vis):
    fvals=[]
    for i in range(len(next_states)):
        fvals.append(100)

    for i in range(len(next_states)):
        fvals[i]=g+h(next_states[i],goal)

    
    min=10000
    min_ind=-1
    for i in range(len(next_states)):
        if(fvals[i]<min and (not next_states[i] in vis)):
            min=fvals[i]
            min_ind=i
    return min_ind

        

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