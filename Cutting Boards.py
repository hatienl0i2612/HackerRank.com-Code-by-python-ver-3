q = int(input().strip())

for i in range(q):
    inp = input().strip().split()
    m = int(inp[0])
    n = int(inp[1])
    arr = []
    xs = [(int(i), 'h') for i in input().strip().split()]
    ys = [(int(i), 'v') for i in input().strip().split()]

    arr.extend(xs)
    arr.extend(ys)
    arr.sort()

    X = 1
    Y = 1
    cost = 0

    while arr != []:
        p = arr.pop()

        if p[1] == 'h':
            X += 1
            cost += p[0] * Y
        else:
            Y += 1
            cost += p[0] * X

    print(cost%(10**9+7))