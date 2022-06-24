i=5
while i>=1:
    j=5
    while j>=1:
        if j==5 or i==5 or j==1 or i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j-1
    print()
    i=i-1