def ispalendrom(x):
    if x<0:
        return False
    rev_num=0
    temp=x
    while temp!=0:
        digit=temp%10
        rev_num=rev_num*10+digit
        temp//=10
    return rev_num==x
print(ispalendrom(121))