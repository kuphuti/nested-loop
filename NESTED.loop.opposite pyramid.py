i=1
while i<=5:
    j=1
    while j<=i:
        print(" ",end=" ")
        j=j+1
    k=2
    while k<=5-i+1:
        print("*",end=" ")    
        k=k+1
    m=5
    while m>=i:
        print("*",end=" ")
        m=m-1    
    print()
    i=i+1