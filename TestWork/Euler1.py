t=int(input())
while(t):
    n = int(input())
    n-=1
    a3=n//3
    a5=n//5
    a15=n//15
    s= ((a3*(a3+1)//2 * 3)+(a5*(a5+1)//2*5) -(a15*(a15+1)//2*15))
    print(s)
    t-=1
