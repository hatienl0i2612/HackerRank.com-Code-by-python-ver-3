if __name__ == '__main__':
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    diff= lst[1] - lst[0]
    res = [lst[0],lst[1]]
    for i in range(1,len(lst)-1):
        if lst[i+1] - lst[i] < diff:
            res = []
            res.append(lst[i])
            res.append(lst[i+1])
            diff = abs(lst[i+1] - lst[i])
        elif lst[i+1] - lst[i] == diff:
            res.append(lst[i])
            res.append(lst[i+1])
    print(*res)