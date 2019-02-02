n = int(input())
arr = sorted(list(map(int,input().split())),reverse = True)
ans = 0
for index,value in enumerate(arr):
    # print(index,value)
    ans += (2**index * value)
print(ans)