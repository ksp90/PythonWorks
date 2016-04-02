def GetMaxColor(m,x,y,d):
    row = len(m)
    col=0
    if row>0:
        col=len(m[0])
    color=[[0 for i in range(col)]]*row
    color[x][y]=1
    while(x<row):
        while(y<col):
            #chedck left
            n_x = x
            n_y=y-1
            if n_y>=0 and abs(m[x][y]-m[n_x][n_y])<=d:
                color[n_x][n_y]=1

            #right
            n_x = x
            n_y=y+1
            if n_y<col and abs(m[x][y]-m[n_x][n_y])<=d:
                color[n_x][n_y]=1
            #top
            n_x = x-1
            n_y=y
            if n_x>=0 and abs(m[x][y]-m[n_x][n_y])<=d:
                color[n_x][n_y]=1
            #down
            n_x = x+1
            n_y=y
            if n_x<row and abs(m[x][y]-m[n_x][n_y])<=d:
                color[n_x][n_y]=1
            y+=1
        x+=1
    c=0;
    for i in range(row):
        for j in range(col):
            if color[i][j]==1:
                c+=1
    return c

m=[]
row,col,q=0,0,0
a=[int(i) for i in input().split()]
row=a[0]
col=a[1]
q=a[2]
while(row):
    m.append([int(i) for i in input().split()])
    row-=1
while(q):
    a=[int(i) for i in input().split()]
    x=a[0]
    y=a[1]
    d=a[2]
    print(GetMaxColor(m,x-1,y-1,d))
    q-=1
