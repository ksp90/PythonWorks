def GetPrime(n):
    prime = [2,3]
    allOdd = [i for i in range(5,n+1,2)]
    for i in allOdd:
        isPrime=True
        for j in prime:
            if i%j==0:
                isPrime=False
                break
            if j>i/2:
                break
        if isPrime:
            prime.append(i)
    return len(prime)

if __name__ == "__main__":
    n = int(input("Enter max range "))
    print(GetPrime(n))
