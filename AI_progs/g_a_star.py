def main():
    print("Enter number of nodes:")
    n=int(input())
    print("Enter adjacency matrix:")
    adj=[]
    for i in range (n):
        t=list(map(int,input().split(" ")))
        adj.append(t)
    src=0
    print("Enter dest:")
    dest=int(input())
    vis=[]
    dfs(src,dest,adj,vis,n,0)

def h(i):
    if(i==0):
        return 5
    if(i==1):
        return 4
    if(i==2):
        return 2
    return 0

def get_next(cur,dest,adj,vis,n,g):
    fval=[]
    min=1000
    minInd=-1
    for i in range(n):
        fval.append(1000)
    for i in range(n):
        if(adj[cur][i]!=0 and (adj[cur][i]!=1000) and (not i in vis)):
            fval[i]=(g+h(i))
            if(fval[i]<min):
                min=fval[i]
                minInd=i
    return minInd
                


def dfs(cur,dest,adj,vis,n,g):
    if(cur==dest):
        print(cur,end="==>>")
        print("REACHED!")
        exit()
    vis.append(cur)
    print(cur,end="->")
    for i in range(n):
        mov=get_next(cur,dest,adj,vis,n,g)
        dfs(mov,dest,adj,vis,n,g+1)


main()