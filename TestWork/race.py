n=int(input())
n_tournaments=2**n-1
winners=[]
loosers=[]
while(n_tournaments):
    try:
        a=1/0
    except ZeroDivisionError:
        print("Hello")
    n_tournaments-=1
