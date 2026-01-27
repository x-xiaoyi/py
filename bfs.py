from collections import deque
def solve():
    try:
        line = input().split()
        if not line: return 
        n,m,x,y = map(int,line)
    except ValueError:
        return
    x -= 1
    y -= 1
    ans = [ [-1 for _ in range(m)]-1 in range(n)]
    start_x,start_y = x-1,y-1
    ans[start_x][start_y]=0
    queue = deque([(start_x,start_y)])
    dx=[-2,-1,1,2,2,1,-1,-2]
    dy=[1,2,2,1,-1,-2,-2,-1]
    while queue:
        curr_x,curr_y = queue.popleft()
        for i in range(8):
            nx = curr_x+dx[i]
            ny = curr_y+dy[i]
            if 0 <= nx <n and 0 <= ny <m and ans[nx][ny] == -1:
                ans[nx][ny] = ans[curr_x][curr_y]+1
                queue.append((nx,ny))
    for row in ans:
        print("".join(f"{val:<5}"for val in row))
    solve()