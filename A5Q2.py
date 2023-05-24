n=int(input("Enter the number"))
p=int(input("Enter lower limit"))
q=int(input("Enter upper limit"))
for i in range(p,q+1):
    if i%n==0:
        print(i)
