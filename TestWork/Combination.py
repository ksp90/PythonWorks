import math
def GetCombination(a,n):
    t=a
    s=""
    while(len(t) >0):
        #t = a[1::]
        l = math.factorial(len(t)-1)
        #print(" l ",l)
        i = (n-1)//l
        n -= i*l
        #print(" t ",t,". i=",i)
        e = t.pop(i)
        s+=str(e)
        #t.remove(e)
    print(s)
i=int(input("enter step : "))
GetCombination([0,1,2,3,4,5,6,7,8,9],i)
