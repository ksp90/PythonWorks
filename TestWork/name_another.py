'''
def p22():
    f = open("C:/tmp/p022_names.txt")
    names = sorted([n.strip('"') for n in f.read().split(',')])

    total = 0
    a = ord('A')
    for i in range(len(names)):
        total += sum([ord(c)-a+1  for c in names[i]]) * (i+1)
    print (total)

def main():
    from timeit import Timer
    print (Timer('p22()', 'from __main__ import p22').timeit(100))

if __name__ == '__main__': main()
'''
def p22():
    import string
    from time import *
    valuehash = dict(zip([x for x in string.letters[26:]],range(1,27)))
    names = [x[1:-1] for x in string.split(open('C:/tmp/p022_names.txt','r').read()[:-1],',')]
    names.sort()
    namescores = [sum([valuehash[x] for x in names[i]])*(i+1) for i in range(len(names))]
    print ("Sum = %d" % sum(namescores))

p22()
