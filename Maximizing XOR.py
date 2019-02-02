if __name__ == "__main__":
    l = int(input())
    r = int(input())
    ans = 0
    for i in range(l,r+1,1):
        for j in range(l,r+1,1):
            ans = max(ans,i^j)
    print(ans)