i=1
while i<=4:
    j=1
    while j<=4:
        if  i==j or j==4 or i==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1