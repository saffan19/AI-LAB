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
    bfs(src,dest,adj,vis,n)

def bfs(cur,dest,adj,vis,n):
    if(cur==dest):
        print(cur)
        print("REACHED!")
        exit()
    queue=[]
    queue.append(cur)
    while(len(queue)!=0):
        t=queue.pop(0)
        vis.append(t)
        if(t==dest):
            print(t," => REACHED!")
            exit()
        print(t,end="->")
        for i in range(n):
            if (adj[t][i]==1 and (not i in vis)):
                queue.append(i)
                
            




main()