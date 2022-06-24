i=0
while i<=3:
    j=3-i
    while j>=0:
        print(" ",end=" ")
        j=j-1
    n=i+1
    while n>0:
        print("*",end=" ") 
        n=n-1
    k=2
    while k<=i+1:
        print("*",end=" ")     
        k=k+1
    print()
    i=i+1      