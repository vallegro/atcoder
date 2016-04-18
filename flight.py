import math


def get_next( cur, hist, time):
    hist += 1
    while hist < time.__len__():
        if time[hist] >= cur:
            return hist
        else:
            hist +=1
    return -1


s = input()
N, M = [int(i) for i in s.split()]
s = input()
X, Y = [int(i) for i in s.split()]
s = input()
a = [int(i) for i in s.split()]
s = input()
b = [int(i) for i in s.split()]

times = [a, b]
fnum = 0
cur = 0
loc = 0
last = [a[a.__len__()-1],b[b.__len__()-1]]
hist = [-1, -1]


while True:
    nextf = get_next(cur, hist[loc], times[loc])
    if nextf == -1:
        print(math.floor(fnum/2))
        break
    else:
        cur = times[loc][nextf]
        #print(cur)
        hist[loc] = nextf
        fnum += 1
        if loc == 0:
            loc = 1
            cur += X
        else:
            loc = 0
            cur += Y

