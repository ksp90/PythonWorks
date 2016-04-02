#m matrix, n--> how many numbers to multiply
def GetMaxMulNum(m, n):
    row_max = len(m)
    col_max = len(m[0])
    num=0
    for r in range(0,row_max):
        for c in range(0,col_max):
            cntr=0
            left = 1
            right=1
            upper=1
            lower=1
            upper_left=1
            upper_right=1
            lower_right=1
            lower_left=1
            #left
            if r>=n-1:
                cntr=0
                while(cntr<n):
                    left *= m[r-cntr][c]
                    cntr+=1
            else:
                left=0
            #right
            if r<=row_max-n:
                cntr=0
                while(cntr<n):
                    right *= m[r+cntr][c]
                    cntr+=1
            else:
                right=0
            #upper
            if c>=n-1:
                cntr=0
                while(cntr<n):
                    upper *= m[r][c-cntr]
                    cntr+=1
            else:
                upper=0
            #lower
            if c<=col_max-n:
                cntr=0
                while(cntr<n):
                    lower *= m[r][c+cntr]
                    cntr+=1
            else:
                lower=0
            #upper left
            if c>=n-1 and r>=n-1:
                cntr=0
                while(cntr<n):
                    upper_left *= m[r-cntr][c-cntr]
                    cntr+=1
            else:
                upper_left=0
            #upper right
            if c>=n-1 and r<=row_max-n:
                cntr=0
                while(cntr<n):
                    upper_right *= m[r+cntr][c-cntr]
                    cntr+=1
            else:
                upper_right=0
            #lower right
            if c<=col_max-n and r<=row_max-n:
                cntr=0
                while(cntr<n):
                    lower_right *= m[r+cntr][c+cntr]
                    cntr+=1
            else:
                lower_right=0

            #lower left
            if c<=col_max-n and r>=n-1:
                cntr=0
                while(cntr<n):
                    lower_left *= m[r-cntr][c+cntr]
                    cntr+=1
            else:
                lower_left=0
            nn = max([left,right,upper,lower,upper_left,upper_right,lower_right,lower_left])
            if nn>num:
                num=nn
    print("max : ",num)

with open("C:/tmp/Data.txt") as f:
    content = f.read().splitlines()
    m=[]
    for c in content:
        m.append([int(i) for i in c.split()])
    GetMaxMulNum(m,4)
