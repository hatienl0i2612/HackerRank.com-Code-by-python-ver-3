if __name__ == "__main__":
    n = int(input())
    arr_A = list(map(int,input().split()))
    arr_B = list(map(int,input().split()))
    da = {}
    db = {}
    ans = []
    for i in arr_A:
        if i in da:
            da[i] += 1
        else:
            da[i] = 1
            ans.append(i)
    for i in arr_B:
        if i in db:
            db[i] += 1
        else:
            db[i] = 1
    # print(da)
    # print(db)
    # print(ans)
    cost = 0
    for k in da:
        if k in db:
            cost += min(da[k],db[k])
    # print(cost)
    if cost == n:
        cost -= 1
    else:
        cost += 1
    print(cost)