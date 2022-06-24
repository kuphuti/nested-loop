a=int(input("enter"))
i=0
while i<=a:
    j=1
    while j<=5:
        if i==4 or j==5 or i+j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1            