n=int(input('請輸入一個整數值,並算出可以除以2多少次?'))
k=0
while(n%2==0):
    k+=1
    n=n/2
    print(n,'是除',format(k),'次')