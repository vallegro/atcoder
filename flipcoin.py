x, y = [int(i) for i in input().split()]
f = int(input())

if f < y:
    ans = x+f
else:
    ans = x+y-(f-y)

print(ans)
