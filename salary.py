n = int(input())
mem = [[]for i in range(n)]
sal = [-1 for i in range(n)]

for i in range(1,n):
    boss = int(input())-1
    mem[boss].append(i)


def salary(target):
    if sal[target] != -1:
        return sal[target]

    min_sa = 0
    max_sa = 0
    for i_mem in range(0, mem[target].__len__()):
        if i_mem == 0:
            min_sa = salary(mem[target][i_mem])
            max_sa = min_sa
        else:
            mem_sa = salary(mem[target][i_mem])
            if mem_sa > max_sa:
                max_sa = mem_sa
            else:
                if mem_sa < min_sa:
                    min_sa = mem_sa

    sal[target] = max_sa+min_sa+1
    return sal[target]

print(salary(0))

