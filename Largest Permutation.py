
def solved(n,m,arr,index):
    for i in range(len(arr)):
        index[arr[i]] = i
    print(arr)
    print(index)
    for i in range(n):
        if arr[i] == n - i:
            continue
        if m == 0:
            break
        arr[index[n - i]] = arr[i]
        index[arr[i]] = index[n - i]
        arr[i] = n - i
        index[n-i] = i
        m -= 1
    print(*arr)
    # i = 0
    # ma = 0
    # while True:
    #     if i == m:
    #         break
    #     ma = max(arr[i:])
    #     arr[arr.index(ma)],arr[i] = arr[i],arr[arr.index(ma)]
    #     i += 1
    # print(*arr)

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    index = [999999] * (n + 1)
    # if arr == sorted(arr,reverse = True):
    #     print(*arr)
    # else:
    solved(n,m,arr,index)