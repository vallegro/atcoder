s = input()
h, m = s.split()
h = float(h)%12
h = float(h)*30+float(m)/2
m = float(m)*6
diff = abs(h-m)
if diff > 180:
    diff = 360-diff
print(str(diff))
