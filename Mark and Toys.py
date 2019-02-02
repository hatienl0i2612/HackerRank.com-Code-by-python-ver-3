if __name__ == "__main__":
    n,k = map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    # print(arr)
    p = arr[0]
    count = 0
    sums = 0
    for i in range(n):
        sums += arr[i]
        if sums < k:
            count += 1
    print(count)
