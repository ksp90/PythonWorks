def GetSum():
    a=[]
    with open("C:/tmp/p022_names.txt") as f:
        for c in f.readlines():
            a=[i.replace('"','') for i in c.split(',')]
    a.sort()
    p=1
    s=0
    for c in a:
        s += (sum([ord(i)-64 for i in c])*p)
        p+=1
    print(s)
from timeit import Timer
print (Timer('GetSum()', 'from __main__ import GetSum').timeit(1))
