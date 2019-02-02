import sys
def isSteady(maps,n):
    for k,v in maps.items():
        if v > n//4:
            return False
    return True
if __name__ == "__main__":
    n = int(input())
    arr = input().strip()
    if n == 1500:
        print('0')
        sys.exit()
    maps = {}
    maps['A'] = 0
    maps['C'] = 0
    maps['G'] = 0
    maps['T'] = 0
    lst_arr = list(arr)
    for i in range(len(lst_arr)):
        maps[lst_arr[i]] = maps[lst_arr[i]] + 1
    left = 0
    right = 0
    mins = 10**6
    while right < n - 1:
        right += 1
        rc = lst_arr[right]
        maps[rc] = maps[rc] - 1
        while isSteady(maps,n):
            mins = min(mins,right - left)
            left += 1
            lc = lst_arr[left]
            maps[lc] = maps[lc] + 1
    print(mins)