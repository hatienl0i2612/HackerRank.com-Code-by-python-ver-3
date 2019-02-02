def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    n,k = map(int,input().split())
    arr = list(quicksort(list(map(int,input().split()))))
    ans = 0
    cover = 0
    mins = 0
    for i in range(n):
        if cover < arr[i]:
            mins = arr[i]
            ans += 1
            cover = mins + k
        elif arr[i] - mins <= k:
            cover = arr[i] + k
    print(ans)
