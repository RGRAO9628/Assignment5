L=[]
for i in range(1,11):
    n=int(input("Enter number "))
    L.append(n)
print("Your List is",L)
L5=[]
for i in L:
    if i not in L5:
        L5.append(i)
p=0
for i in L5:
    for j in L:
        if i==j:
            p=p+1
    print(i,"occurs",p,"times")
    p=0
