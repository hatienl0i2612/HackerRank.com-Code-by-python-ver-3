
if __name__ == "__main__":
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    # print(arr)
    p = arr[0]
    ans = 1
    for i in range(len(arr)):
        if arr[i] > p + 4:
            ans += 1
            p = arr[i]
    print(ans)