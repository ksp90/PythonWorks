from math import sqrt
from itertools import count, islice

def GetFactor(n):
    f=[]
    for number in islice(count(1), int(n/2)):
        if n%number==0:
            f.append(number)
    f.append(n)
    return f

def GetFactor1(n):
    f=[1,n]
    pf=isPrime(n)
    if pf==n:
        return f
    t=n
    while(t>1):
        pf=isPrime(t)
        if pf != 1:
            f.append(pf)
            t=int(t/pf)
    return f

def getNum(m):
    a=[]
    n=0
    s=0
    while(len(a)<m):
        n+=1
        s+=n
        #print("n ",n,"s ",s)
        a=GetFactor(s)
        #print("a ",a)
    print("n :: ",n," . a[] :: ",a)


getNum(50)
#print(GetFactor(int(input("Enter number to check :: "))))
