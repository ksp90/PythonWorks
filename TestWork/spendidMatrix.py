def getIJ(order,value):
    x,y=0,0
    startValue=1
    blockUnit=2
    n=order
    while(n>1):
        position=value-startValue+1
        smallerBlockOrder=2**(n-1)
        totalElementInSmallBlock=smallerBlockOrder**2
        region=(position-1)//totalElementInSmallBlock
        #print("n = ",n," region ",region," position ",position)
        startValue+=totalElementInSmallBlock*region
        if region==1:
            y+=smallerBlockOrder
        elif region==2:
            x+=smallerBlockOrder
        elif region==3:
            x+=smallerBlockOrder
            y+=smallerBlockOrder
        n-=1
    #print("start value ",startValue," x ",x," y ",y)
    if n==1:
        position=value-startValue+1
        region=(position-1)
        #print("n = ",n," region ",region," position ",position)
        if region==1:
            y+=1
        elif region==2:
            x+=1
        elif region==3:
            x+=1
            y+=1
    return [x,y]

def getNumofIJ(order,x,y):
    #x,y=0,0
    startValue=1
    blockUnit=2
    n=order
    while(n>1):
        #position=value-startValue+1
        smallerBlockOrder=2**(n-1)
        totalElementInSmallBlock=smallerBlockOrder**2
        regionX=x//smallerBlockOrder
        regionY=y//smallerBlockOrder
        #region=(position-1)//totalElementInSmallBlock
        region=2*regionX+regionY
        #print("n = ",n," region ",region," position ",position)
        startValue+=totalElementInSmallBlock*region
        if region==1:
            y-=smallerBlockOrder
        elif region==2:
            x-=smallerBlockOrder
        elif region==3:
            x-=smallerBlockOrder
            y-=smallerBlockOrder
        n-=1
    #print("start value ",startValue," x ",x," y ",y)
    if n==1:
        #position=value-startValue+1
        region=2*x+y
        #print("n = ",n," region ",region," position ",position)
        startValue+=region
    return startValue

print(getNumofIJ(int(input("order ")),int(input("x ")),int(input("y "))))
