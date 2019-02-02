memo = [[]]


def adj(a, b, x, y, n):
    return filter(lambda v: v[0] >= 0
                            and v[1] >= 0
                            and v[0] < n
                            and v[1] < n,
                  [
                      [x + a, y + b],
                      [x + a, y - b],
                      [x - a, y + b],
                      [x - a, y - b],
                      [x + b, y + a],
                      [x + b, y - a],
                      [x - b, y + a],
                      [x - b, y - a],
                  ])


def move(a, b, n):
    global memo
    if memo[a][b] is not None:
        return memo[a][b]
    visited = [[False] * n for _ in range(n)]
    queue = [[0, 0, 0]]
    while len(queue) > 0:
        x, y, l = queue.pop()
        if x == n - 1 and y == n - 1:
            memo[a][b] = l
            memo[b][a] = l
            return l
        neighbors = [
            [x_i, y_i]
            for x_i, y_i in adj(a, b, x, y, n)
            if visited[y_i][x_i] == False
        ]

        for x_i, y_i in neighbors:
            visited[y_i][x_i] = True
            queue.insert(0, [x_i, y_i, l + 1])

    memo[a][b] = -1
    memo[b][a] = -1
    return -1

def knightlOnAChessboard(n):
    global memo
    memo = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    results = []
    for a in range(1, n):
        results.append([])
        for b in range(1, n):
            results[a - 1].append(move(a, b, n))
    return results


if __name__ == '__main__':
    n = int(input())

    result = knightlOnAChessboard(n)
    for i in result:
        print(*i)
