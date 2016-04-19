from math import floor
a, b = [int(i) for i in input().split()]
c = b-a
lookup1 = [0, 1, 2, 3, 2, 1, 2, 3, 4, 5]
lookup2 = [2, 5, 4, 3, 2, 1, 2, 3, 2, 1]

c = abs(c)
r = [0, 0]
r[0] = floor(c/10) + lookup1[c % 10]
r[1] = floor(c/10) + 1 + lookup2[c % 10]
print(min(r))
