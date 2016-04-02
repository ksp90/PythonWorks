def GetMaxNumberForPalin(n,m):
    step=10
    a=[i for i in range(n,int(n/10),-1)]
    t=n*n
    while(t>=m):
        a=[i for i in range(n,n-step, -1)]
        c=[]
        for i in a:
            b=[j for j in range(i,n-step,-1)]
            for j in b:
                p=i*j
                p1=int(str(p)[::-1])
                if p==p1:
                    t=p
                    c=[i,j]
        n-=1
    print(c)
    return c[0]*c[1]
i=int(input())
while(i):
    print(GetMaxNumberForPalin(999,int(input())))
    i-=1
