limit=1001
odd = [i for i in range(3,limit+1,2)]
last=1
s=1
for i in odd:
    start = last + (i-1)
    s += ((start * 4) + (i-1)*6)
    last= start + (i-1)*3

print(s)
