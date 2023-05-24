L=[]
for i in range(1,11):
    n=int(input("Enter number "))
    L.append(n)
print("Your List is",L)
L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
for i in L:
    if i>=0:
        L1.append(i)
    else:
        L2.append(i)
for i in L:
    if i%2==0:
        L3.append(i)
    else:
        L4.append(i)
for i in L:
    if i not in L5:
        L5.append(i)
print("Positive Nos are ",L1)
print("Negative Nos are ",L2)
print("Even Nos are ",L3)
print("Odd Nos are ",L4)
#print(L5)
p=0
for i in L5:
    for j in L:
        if i==j:
            p=p+1
    print(i,"occurs",p,"times")
    p=0
