def define_line(s, e, h):
    line = [s]
    for i in range(0, h):
        line.append((e-s)/h*i)
    return line


def main():
    h = int(input())
    s, e = [int(i) for i in input().split()]
    wall = []
    for i in range(0, h+1):
        wall.append([int(i) for i in input().split() ])
    key = [[s, 0]]
    line = define_line(s, e, h)

    for i in range(1, h):
        if wall[i][0] > line[i]:
            key.append([wall[i][0], i])
            line[i:] = define_line(wall[i][0], e, h-i+1)
        elif wall[i][1] < line[i]:
            key.append([wall[i][1], i])
            line[i:] = define_line(wall[i][1], e, h-i+1)

    key.append([e,h])

    print(key)

main()
