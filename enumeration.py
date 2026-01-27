n=0
b=0
for i in range(1,2027):
    b=0
    for h in str(i):
        h=int(h)
        b=b+h
        if b%2==0:
            n=n+1

print(n)
