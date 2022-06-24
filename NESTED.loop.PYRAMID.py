a=1
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<=a:
        print("*",end=" ")
        k=k+1
    print()
    i=i+1
    a=a+2