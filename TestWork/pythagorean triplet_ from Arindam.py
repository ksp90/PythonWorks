#Pythagorean triplet program
'''
from Arindam
'''
def getPythagoreanTriplet(n):
    triplet=[]
    for i in range(1,n//3+1):
        for j in range(i+1,n//2+1):
            c = n-i-j
            if(i**2+j**2==c**2):
                triplet.append([i,j,c])
    return triplet
def getMaxMul(tripletSets):
    mul=-1
    for triplet in tripletSets:
        res = triplet[0]*triplet[1]*triplet[2]
        if res>mul:
            mul=res
    return mul
t=int(input())
while t:
    print(getMaxMul(getPythagoreanTriplet(int(input()))))
    t-=1
