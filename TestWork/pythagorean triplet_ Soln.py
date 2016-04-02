#Pythagorean triplet program
'''
a+b+c=N
r=N//2
if z=n-a
then c = (a**2+z**2)/(2*z)
and b = N-a-c
'''
def getPythagoreanTriplet(N):
    triplet=[]
    r = N//2
    for a in range(1,r+1):
        c = int((a**2+(N-a)**2)/(2*(N-a)))
        b = N-a-c
        if(a**2+b**2==c**2 and a*b>0):
            triplet.append([a,b,c])
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
