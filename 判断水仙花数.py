def shuixianhua(number):
    while number != 0:
        a=number%10
        s=s+a**3
        number//=10
    if s==number:
        return True
    else:
        return False
