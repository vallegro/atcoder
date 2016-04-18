s = [int(i) for i in input().split()]
a = s[0]+s[3]+s[4]
b = s[1]+s[2]+s[4]
if a > b:
    print(a)
else:
    print(b)
