mod=10**9+7
def my_fib(x):
  if x < 2:
    return [x,x-1]
  else:
    return my_fib_helper(x)

def my_fib_helper(x):
  if x == 1:
    return (1, 0)
  if x % 2 == 1:
    (p,q) = my_fib_helper(x-1)
    return ((p+q)%mod,p%mod)
  else:
    (p,q) = my_fib_helper(x/2)
    return ((p*p+2*p*q)%mod,(p*p+q*q)%mod)

t=int(input())
while(t):
  t_i=[int(i) for i in input().split()]
  f_0=t_i[0]
  f_1=t_i[1]
  step=t_i[2]
  coef=my_fib(step)
  print(((coef[0]%mod)*(f_1%mod)+(coef[1]%mod)*(f_0%mod))%mod)
  t-=1
