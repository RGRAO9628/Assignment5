a=int(input("Enter lower limit "))
b=int(input("Enter Upper limit "))
for i in range(a,b+1):
    if i==2:
        print(i)
    if i>2:
        f=0
        for j in range(1,int((i+1)/2)+1):
            #print(i,"%",j)
            if i%j==0:
                f=f+1
        if f<2:
            print(i)
            f=0
