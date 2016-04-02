def GetFirstNDigitSum(n):
    s=0
    with open("C:/tmp/Data.txt") as f:
        content = f.read().splitlines()
        for c in content:
            s += int(c[:n+len(str(len(content)*9)):])
    print(int(str(s)[:n:]))
GetFirstNDigitSum(10)
