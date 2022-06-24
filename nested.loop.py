i=1
while i<=9:
    j=1
    while j<=9-i+1:
        print(" ",end="")
        j=j+1
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+1
    print()
    i=i+2      