def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr = quicksort(arr)
    ans = arr[n - 1] - arr[0]
    try:
        for i in range(n):
            if arr[i + k - 1] - arr[i] < ans:
                ans = arr[i + k - 1] - arr[i]
    except Exception as identifier:
        pass
    print(ans)