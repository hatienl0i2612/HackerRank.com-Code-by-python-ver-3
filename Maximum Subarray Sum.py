def solved(n,m,arr):
    out = [-1] * n
    out[0] = [arr[0] % m,0]
    for i in range(1,n):
        out[i] = [(out[i - 1][0] + (arr[i] % m)) % m,i]
    out = sorted(out)
    mini = -1
    for i in range(0,n - 1):
        if out[i][1] > out[i + 1][1] and (out[i + 1][0] - out[i][0] < mini or mini == -1):
            mini = out[i + 1][0] - out[i][0]
    if out[n - 1][0] > m - mini:
        mini = m - out[n - 1][0]
    print(m - mini)
if __name__ == "__main__":
    for i in range(int(input())):
        n,m = map(int,input().split())
        arr = list(map(int,input().split()))
        solved(n,m,arr)