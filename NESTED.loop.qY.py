i=0
while i<=5:
    j=5
    while j>=i:
        print(" ",end=" ")
        j=j-1
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+1
    l=i-1
    while l>0:
        print("*",end=" ")
        l=l-1
    print()
    i=i+1    