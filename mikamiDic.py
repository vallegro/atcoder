N, a = [int(i) for i in input().split()]
k = int(input())
b = [int(i) for i in input().split()]

count = 0
cur = a
d = {}

while True:
    count += 1
    s = str(b[cur-1])

    if count == k:
        print(s)
        exit(0)

    if s in d:
        loop = count-d[s]+1
        before = count - loop
        entry = b[cur-1]
        break

    else:
        d[str(cur)] = count
        cur = b[cur-1]


pos = (k-before) % loop

cur = entry
i = 0
while i < pos:
    cur = b[cur-1]
    i += 1

print(str(cur))
