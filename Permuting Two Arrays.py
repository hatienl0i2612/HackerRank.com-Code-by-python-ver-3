def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def oke(n,k,arr_A,arr_B):
    for i in range(len(arr_A)):
        if arr_A[i] + arr_B[i] < k:
            return False
    else:
        return True
if __name__ == "__main__":
    for _ in range(int(input())):
        n,k = map(int,input().split())
        arr_A = list(quicksort(list(map(int,input().split()))))
        arr_B = list(reversed(quicksort(list(map(int,input().split())))))
        if oke(n,k,arr_A,arr_B):
            print("YES")
        else:
            print("NO")