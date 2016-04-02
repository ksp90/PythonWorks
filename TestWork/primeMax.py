from math import sqrt
def GetPrime(n):
    s=int(n/6)
    mp=int(sqrt(n))
    pl=[2,3,5]
    p=1
    #print(s,",",mp)
    while(s):
        p1=6*p+1
        p2=6*p+5
        #print(p1,"::",p2)
        #check prime
        mpf=int(sqrt(p1))
        #print("mpf",mpf)
        pf=p1
        for i in pl:
            if i>mpf:
                break
            elif p1%i==0:
                pf=i
                break
        #print("pf ",pf)

        if pf==p1:
            pl.append(pf)
        #print(pl)
        if p%5==0 or p2>n:
            p+=1
            #print(p)
            s-=1
            continue
        mpf=int(sqrt(p2))
        pf=p2
        for i in pl:
            if i>mpf:
                break
            elif p2%i==0:
                pf=i
        if pf==p2:
            pl.append(pf)
        #print(pl)
        p+=1
        #print(p)
        s-=1
    return pl
print(GetPrime(300000))
