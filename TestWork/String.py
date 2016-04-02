def GetCommonString(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    short_len=0
    res=[]
    if len1<len2:
        short_len=len1
    else:
        short_len=len2
    for i in range(1,short_len +1):
        subString1 = s1[:i]
        subString2 = s2[-i:]
        if subString1 == subString2:
            res.append(subString1)
        subString1 = s2[:i]
        subString2 = s1[-i:]
        if subString1 == subString2:
            res.append(subString1)
    return res

print(GetCommonString(input('string1 : '),input('string1 : ')))

def Calculate(array):
    a=[[]*len(array)]*len(array)
    
