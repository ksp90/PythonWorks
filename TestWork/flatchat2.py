def Sweetness(a):
    a.sort()
    b=[]
    while(len(a)):
        b.insert(0,a.pop())
        if len(a)>0:
            b.insert(0,a.pop(0))
    taste=0
    print(b)
    #calculate taste. data is stored in 0 based array
    for i in range(1,len(b),1):
        taste += ((i+1)* abs(b[i]-b[i-1]))
    return taste
t=int(input())
while t:
    n=int(input())
    a=[int(i) for i in input().split()]
    print(Sweetness(a))
    t-=1
