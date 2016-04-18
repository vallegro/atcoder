import math
a = int(input())
dic = ['a', 'b', 'c']
i = 0
limit = pow(3, a)
while i < limit:
    j = 0
    no = i
    s=""
    while j < a:
        s= dic[no % 3]+s
        no = math.floor(no/3)
        j+=1
    print(s)
    i+=1