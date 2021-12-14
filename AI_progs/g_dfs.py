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
    dfs(src,dest,adj,vis,n)

def dfs(cur,dest,adj,vis,n):
    if(cur==dest):
        print(cur)
        print("REACHED!")
        exit()
    vis.append(cur)
    print(cur,end=" ")
    for i in range(n):
        if(adj[cur][i]==1 and (not i in vis)):
            dfs(i,dest,adj,vis,n)


main()