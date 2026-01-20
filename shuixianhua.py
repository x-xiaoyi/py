def shuixianhua(number):
    s=0
    temp=number
    while number != 0:
        a=number%10
        s=s+a**3
        number//=10
    if s==temp:
        return True
    else:
        return False
