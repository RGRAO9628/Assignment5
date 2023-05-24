p=input("Enter sides of triangle")
a,b,c=p.split(",")
a=int(a)
b=int(b)
c=int(c)
if a+b>c and b+c>a and c+a>b:
    s=(a+b+c)/2
    z=(s*(s-a)*(s-b)*(s-c))**(1/2)
    print("Triangle is Possible and\n it's area is ",z)
else:
    print("Triangle is not Possible")
