num = int(input())
a = [int(i) for i in input()]
b = [0, 0, 0, 0]
for i in range(0, num):
    b[a[i]-1] += 1
print("{} {}".format(max(b), min(b)))
