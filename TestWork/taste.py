def getMaxTaste(tastes,calories,k):
    n=len(tastes)
    calculatedtastes=[-1]*n
    c=n
    while(c):
        c_i=n-c
        #invidual check
        print("c_i ",c_i)
        for i in range(n-c_i):
            calculatedTaste=-1
            alltastes=0
            allcalories=0
            for j in range(i+1):
                print("checking ",c_i+j)
                #calculatedTaste+=(tastes[c_i+j]/calories[c_i+j])
                alltastes+=tastes[c_i+j]
                allcalories+=calories[c_i+j]
            calculatedTaste=alltastes/allcalories
            print("calculated taste ",calculatedTaste)
            if calculatedTaste==k and alltastes>calculatedtastes[c_i]:
                calculatedtastes[c_i]=alltastes
        c-=1
    #print(calculatedtastes)
    return max(calculatedtastes)
a=[int(i) for i in input().split()]
n=a[0]
k=a[1]
tastes=[int(i) for i in input().split()]
calories=[int(i) for i in input().split()]
print(getMaxTaste(tastes,calories,k))
