def GetMaxNumberForPalin(n,m):
    a=[i for i in range(n,int(n/10),-1)]
    t=0
    c=[]
    for i in a:
        b=[j for j in range(i,int(n/10),-1)]
        for j in b:
            p=i*j
            p1=int(str(p)[::-1])
            if p==p1:
                if p>t and p<m:
                    t=p
                    c=[i,j]
    return c[0]*c[1]
i=int(input())
while(i):
    print(GetMaxNumberForPalin(999,int(input())))
    i-=1
