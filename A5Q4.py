n=int(input("Enter odd Number"))
m=(n+1)/2
for i in range(1,n+1):
    if i<=m:
        for j in range(1,i+1):
            print("* ",end='')
        print()
    else:
        for j in range(1,(n+1-i)+1):
            print("* ",end="")
        print()
