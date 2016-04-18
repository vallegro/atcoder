s = input()
a = s.split()
wr1 = float(a[1])/float(a[0])
wr2 = float(a[3])/float(a[2])

if wr1 > wr2:
    print("TAKAHASHI")
else:
    if wr1 < wr2:
        print("AOKI")
    else:
        print("DRAW")