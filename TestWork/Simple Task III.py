
def MaxCount(a):
    a.sort(key=None,reverse=True)
    c=a[1]*2
    if a[0]>a[1]:
        c+=1
    return c

t=int(input())
while t:
    a=[int(i) for i in input().split()]
    print(MaxCount(a))
    t-=1
