if __name__ == "__main__":
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    flag = False
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            for k in range(j-1,-1,-1):
                if arr[j] + arr[k] > arr[i]:
                    print(arr[k],arr[j],arr[i])
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if not flag:
        print(-1)
