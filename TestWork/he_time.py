testCases = int(input())
while(testCases):
    nk=input().split()
    n=int(nk[0])
    k=int(nk[1])
    values=input().split()
    allValues = [int(i) for i in values]
    lastReleased=-1
    lastSelected=0
    allSelections=[0]*n
    allSelections[0]=1
    numberHopping=0
    for i in range(n):
        #i is current index
        if(allValues[i]<0):
            numberHopping=0
            continue
        if(i>(lastSelected+k)):
            #mark this element as selected
            allSelections[i]=1
            lastSelected=i
            continue
        if(allValues[i]>allValues[lastSelected] and numberHopping<k):
            allSelections[lastSelected]=0
            allSelections[i]=1
            lastSelected=i
            lastReleased=lastSelected
            numberHopping+=1
    s=0
    for i in range(n):
        s += (allValues[i]*allSelections[i])
    print(s)
    testCases-=1
