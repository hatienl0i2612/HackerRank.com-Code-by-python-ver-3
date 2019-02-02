def solved(n,arr):
    ans = 10**6
    for x,y in zip(arr,arr[1:]):
        if abs(x - y) < ans:
            ans = abs(x - y)
    print(ans)
    
if __name__ == "__main__":
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    solved(n,arr)