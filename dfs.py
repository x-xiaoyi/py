n=int(input())
step=1
path=[]
used=[False]*(n+1)
def dfs(step):
    if step == n+1:
        print(path)
        return
    for i in range(1,n+1):
        if used[i] ==False:
            used[i] = True
            path.append(i)
            dfs(step+1)
            path.pop()
            used[i] = False
dfs(1)
