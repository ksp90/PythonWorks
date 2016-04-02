def CalMinPrimeDivisorSum(n):
    prime = [2,3]
    total=5
    allOdd = [i for i in range(5,n+1,2)]
    allEvenCount=0
    allOddCount=len(allOdd)
    if n%2==0:
        allEvenCount=allOddCount+1
    else:
        allEvenCount=allOddCount
    for i in allOdd:
        isPrime=True
        for j in prime:
            if i%j==0:
                total += j
                isPrime=False
                break
        if isPrime:
            prime.append(i)
            total+=i
    total += (allEvenCount *2)
    print(total)



if __name__ == "__main__":
    n = int(input("Enter the max range "))
    CalMinPrimeDivisorSum(n)
