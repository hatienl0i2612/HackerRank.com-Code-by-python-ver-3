
if __name__ == '__main__':
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    count = 0
    arr = set(arr)
    for i in arr:
        x = i + k
        if x in arr:
            count += 1
    print(count)