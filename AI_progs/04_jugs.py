# Actions:
# j4 to j3
# j3 to j3
# fill j4
# fill j3
# empty j4
# empty j3
# Goal: 2L in j4
def main():
    #initial both jugs are empty
    j4=3
    j3=1
    vis=[]
    dfs_jugs(j4,j3,vis)
def get_next_states(j4,j3):
    actions=[]
    if(j4==0):
        actions.append((4,j3))
    if(j3==0):
        actions.append((j4,3))
    if(j4!=4):#move from j3 to j4
        t3=j3-(4-j4)
        if(t3<0):
            t3=0
        t4=j4+(j3-t3)
        if(t4>4):
            t4=4
        actions.append((t4,t3))
    if(j3!=3):#move from j4 to j3
        t4=j4-(3-j3)
        if(t4<0):
            t4=0
        t3=j3+(j4-t4)
        if(t3>3):t3=3
        actions.append((t4,t3))
    if(j4!=0):#empty j4
        actions.append((0,j3))
    if(j3!=0):#empty j3
        actions.append((j4,0))
    return actions


def dfs_jugs(j4,j3,vis):
    if(j4==2):
        print((j4,j3))
        print("GOAL REACHED!")
        exit()
    vis.append((j4,j3))
    print((j4,j3))
    actions=get_next_states(j4,j3)
    for ac in actions:
        if(not (ac[0],ac[1]) in vis):
            dfs_jugs(ac[0],ac[1],vis)
main()


