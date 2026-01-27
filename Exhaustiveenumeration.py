from datetime import datetime,timedelta
str_daytime="20200202"
i=5000
current=datetime.strptime(str_daytime, '%Y%m%d')
while i!=0:
    current+=timedelta(days=1)
    a=current.strftime('%Y%m%d')
    s=a[::-1]
    i=i-1
    if s==a:
        print(a)
        break
    else:
        continue


