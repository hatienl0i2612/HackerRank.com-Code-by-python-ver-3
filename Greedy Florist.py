if __name__ == "__main__":
    n,k = map(int,input().split())
    arr = sorted(list(map(int,input().split())),reverse = True)
    # print(arr)
    if k == n:
        print(sum(arr))
    else:
        ans = 0
        count = n - k
        for i in range(n):
            ans += ((i//k) + 1) * arr[i]
        print(ans)