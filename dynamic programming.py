def climb_stairs(n):
    if n == 1 : return 1
    if n == 2 : return 2
    if n == 3 : return 4
    a=1,b=2,c=4
    for i in range(4,n+1):
        current=a+b+c
        a=b
        b=c
        c=current
    return c