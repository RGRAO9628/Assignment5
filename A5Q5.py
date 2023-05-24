n=int(input("Enter Number of Rows "))
h=65
i=1
while i<=n:
    for i in range(1,i+1):
        if h in range(65,91):
            print(chr(h),end="")
            h=h+1
        else:
            h=65
            print(chr(h),end="")
            h=h+1
    print()
    i=i+1
