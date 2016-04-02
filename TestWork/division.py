def fracnum(N,D,R):
    n=N*(10**R)
    r = int(str(n//D)[-1])
    return r

t = int(input())
while t:
    data = [int(i) for i in input().split()]
    print(fracnum(data[0],data[1],data[2]))
    t-=1
