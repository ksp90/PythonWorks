def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

#print(len(primes(int(input("Enter n:: ")))))
prime_table = primes(200000)
t = int(input())
while t:
    n=int(input())
    print(prime_table[n-1])
    t -= 1
